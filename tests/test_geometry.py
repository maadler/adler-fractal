import ast
import itertools
import math
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
import xml.etree.ElementTree as ET

from adler_fractal import Parameters, chaos_points, iter_endpoints, iter_segments
from adler_fractal.core import statistics
from adler_fractal.render import write_svg
from turtle_reference import draw_fractal

ROOT = Path(__file__).resolve().parents[1]


class RecordingTurtle:
    """Minimal independent recorder for the original script's Turtle calls."""
    def __init__(self):
        self.position = 0j
        self.heading = 0.0
        self.down = False
        self.lines = []

    def penup(self):
        self.down = False

    def pendown(self):
        self.down = True

    def goto(self, x, y):
        end = complex(x, y)
        if self.down:
            self.lines.append((self.position, end))
        self.position = end

    def setheading(self, angle):
        self.heading = angle

    def forward(self, length):
        a = math.radians(self.heading)
        end = self.position + length * complex(math.cos(a), math.sin(a))
        if self.down:
            self.lines.append((self.position, end))
        self.position = end

    def pos(self):
        return self.position.real, self.position.imag


class GeometryTests(unittest.TestCase):
    def test_original_commands_and_traversal(self):
        tree = ast.parse((ROOT / "original/eagle_fractal.py").read_text())
        fn = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == "draw_fractal")
        recorder = RecordingTurtle()
        # No global Turtle is provided: the function has to draw with the one it is given.
        ns = {"turtle": SimpleNamespace(Turtle=RecordingTurtle)}
        exec(compile(ast.Module(body=[fn], type_ignores=[]), "original/eagle_fractal.py", "exec"), ns)
        ns["draw_fractal"](recorder, (0, 0), ang=5, lng=200, iterations=2)
        reference = list(iter_segments(Parameters()))
        self.assertEqual(len(recorder.lines), 5256)
        self.assertEqual(len(reference), len(recorder.lines))
        for actual, expected in zip(reference, recorder.lines):
            self.assertLess(abs(actual.start - expected[0]), 1e-10)
            self.assertLess(abs(actual.end - expected[1]), 1e-10)

    def test_endpoint_formula_independent_product(self):
        p = Parameters(spokes=5, iterations=4, length=3, scale=.37,
                       origin=2-4j, phase_degrees=17)
        actual = list(iter_endpoints(p))
        for point, word in zip(actual, itertools.product(range(5), repeat=4)):
            expected = p.origin + sum(p.length * p.scale ** k * p.directions[j] for k, j in enumerate(word))
            self.assertLess(abs(point - expected), 1e-12)
        self.assertEqual(len(actual), 5 ** 4)

    def test_counts_lengths_and_tight_radius(self):
        for scale in (1, .5, .03):
            p = Parameters(spokes=8, iterations=3, length=2, scale=scale)
            lines = list(iter_segments(p))
            self.assertEqual(len(lines), 8 + 64 + 512)
            for s in lines:
                self.assertAlmostEqual(abs(s.end - s.start), 2 * scale ** (s.generation - 1), places=12)
                self.assertLessEqual(abs(s.end), p.radius + 1e-12)
            self.assertAlmostEqual(max(abs(x) for x in iter_endpoints(p)), p.radius, places=12)

    def test_dihedral_endpoint_invariance(self):
        p = Parameters(spokes=8, iterations=3, length=1, scale=.25)
        points = list(iter_endpoints(p))
        key = lambda x: (round(x.real, 10), round(x.imag, 10))
        expected = set(map(key, points))
        rotation = p.directions[1]
        self.assertEqual({key(x * rotation) for x in points}, expected)
        self.assertEqual({key(x.conjugate()) for x in points}, expected)

    def test_original_second_level_unique_endpoints(self):
        points = list(iter_endpoints(Parameters()))
        self.assertEqual(len({(round(x.real, 8), round(x.imag, 8)) for x in points}), 2593)
        self.assertEqual(sum(abs(x) < 1e-9 for x in points), 72)

    def test_origin_adapter_and_parameter_not_global(self):
        recorder = RecordingTurtle()
        draw_fractal(recorder, (2, -3), ang=120, lng=7, iterations=2, scale=.4)
        p = Parameters(spokes=3, iterations=2, length=7, scale=.4, origin=2-3j)
        for recorded, expected in zip(recorder.lines, iter_segments(p)):
            self.assertLess(abs(recorded[0] - expected.start), 1e-12)
            self.assertLess(abs(recorded[1] - expected.end), 1e-12)
        self.assertEqual(len(recorder.lines), 12)

    def test_zero_depth(self):
        p = Parameters(iterations=0)
        self.assertEqual(list(iter_segments(p)), [])
        self.assertEqual(list(iter_endpoints(p)), [0j])
        self.assertEqual(p.radius, 0)

    def test_invalid_parameters_and_nonregular_legacy_angle(self):
        for kwargs in ({"spokes": 0}, {"spokes": True}, {"iterations": -1},
                       {"length": 0}, {"length": math.nan}, {"scale": 0},
                       {"scale": 1.01}, {"phase_degrees": math.inf}):
            with self.assertRaises(ValueError):
                Parameters(**kwargs)
        with self.assertRaises(ValueError):
            Parameters.from_angle(7)
        self.assertEqual(Parameters.from_angle(5).spokes, 72)

    def test_budget_preflight_and_no_partial_svg(self):
        p = Parameters(iterations=4)
        self.assertEqual(p.segment_count, 27252360)
        with self.assertRaises(ValueError):
            next(iter_segments(p))
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "not_created.svg"
            with self.assertRaises(ValueError):
                write_svg(target, p)
            self.assertFalse(target.exists())

    def test_svg_xml_and_element_count(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "test.svg"
            p = Parameters(spokes=5, iterations=2, length=1, scale=.25)
            write_svg(target, p)
            tree = ET.parse(target)
            self.assertEqual(len(tree.findall(".//{http://www.w3.org/2000/svg}path")), 30)

    def test_chaos_determinism_range_and_rejection(self):
        p = Parameters(spokes=8, scale=.25, origin=2-1j)
        a = list(chaos_points(p, samples=1000, seed=42))
        self.assertEqual(a, list(chaos_points(p, samples=1000, seed=42)))
        self.assertNotEqual(a, list(chaos_points(p, samples=1000, seed=43)))
        self.assertTrue(all(abs(x - p.origin) <= p.limiting_radius + 1e-12 for x in a))
        with self.assertRaises(ValueError):
            next(chaos_points(Parameters(), samples=10))

    def test_certified_dimensions_and_overlap_discipline(self):
        self.assertAlmostEqual(Parameters(spokes=8, scale=.25).certified_endpoint_dimension, 1.5)
        self.assertAlmostEqual(Parameters(spokes=3, scale=.5).certified_endpoint_dimension, math.log(3)/math.log(2))
        self.assertEqual(Parameters(spokes=4, scale=.5).certified_endpoint_dimension, 2)
        self.assertEqual(Parameters(spokes=72, scale=.5).certified_endpoint_dimension, 2)
        self.assertIsNone(Parameters(spokes=5, scale=.5).certified_endpoint_dimension)
        self.assertIsNone(Parameters(spokes=72, scale=.4).certified_endpoint_dimension)
        self.assertIsNone(Parameters().similarity_dimension)
        self.assertEqual(statistics(Parameters())["drawing_commands"], 5256)
        # Even m at scale 1/2: the endpoints fill the regular polygon, so each of
        # its points lies within the Hausdorff bound of the depth-n endpoints.
        p = Parameters(spokes=6, iterations=5, length=1, scale=.5)
        ends = list(iter_endpoints(p))
        bound = p.length * p.scale ** p.iterations / (1 - p.scale)
        corners = [p.limiting_radius * u for u in p.directions]
        for z in (0j, corners[0] / 3, (corners[0] + corners[1]) / 2,
                  (corners[0] + corners[1] + corners[3]) / 3):
            self.assertLessEqual(min(abs(z - e) for e in ends), bound + 1e-12)


if __name__ == "__main__":
    unittest.main()
