"""Exact construction rules implemented with floating-point coordinates.

All directions use the same global coordinate system. The trace preserves
repeated drawing commands; an endpoint enumeration preserves address multiplicity.
No function deduplicates or estimates a fractal dimension from pixels.
"""

from dataclasses import dataclass
import math
import random
from typing import Iterator

from ._version import __version__


@dataclass(frozen=True)
class Parameters:
    spokes: int = 72
    iterations: int = 2
    length: float = 200.0
    scale: float = 1.0
    phase_degrees: float = 0.0
    origin: complex = 0j

    def __post_init__(self) -> None:
        if type(self.spokes) is not int or self.spokes < 3:
            raise ValueError("spokes must be an integer >= 3")
        if type(self.iterations) is not int or self.iterations < 0:
            raise ValueError("iterations must be a nonnegative integer")
        if not math.isfinite(self.length) or self.length <= 0:
            raise ValueError("length must be finite and positive")
        if not math.isfinite(self.scale) or not 0 < self.scale <= 1:
            raise ValueError("scale must satisfy 0 < scale <= 1")
        if not math.isfinite(self.phase_degrees):
            raise ValueError("phase_degrees must be finite")
        if not (math.isfinite(self.origin.real) and math.isfinite(self.origin.imag)):
            raise ValueError("origin must have finite coordinates")
        if not math.isfinite(self.radius):
            raise ValueError("coordinate range overflows floating point")

    @classmethod
    def from_angle(cls, angle: int, **kwargs) -> "Parameters":
        """Regular directions matching range(0, 360, angle) for integer divisors.

        The original also accepts other positive integer angles, but those do
        not produce the equally spaced cyclic direction set of this specification.
        """
        if type(angle) is not int or angle <= 0 or 360 % angle != 0:
            raise ValueError("angle must be a positive integer divisor of 360")
        return cls(spokes=360 // angle, **kwargs)

    @property
    def directions(self) -> tuple[complex, ...]:
        return tuple(
            complex(math.cos(a), math.sin(a))
            for a in (
                math.radians(self.phase_degrees + 360.0 * j / self.spokes)
                for j in range(self.spokes)
            )
        )

    @property
    def segment_count(self) -> int:
        m = self.spokes
        return m * (m ** self.iterations - 1) // (m - 1)

    @property
    def endpoint_count(self) -> int:
        return self.spokes ** self.iterations

    @property
    def radius(self) -> float:
        if self.scale == 1:
            return self.length * self.iterations
        # expm1 avoids cancellation for scale close to one.
        return self.length * (-math.expm1(self.iterations * math.log(self.scale))) / (1 - self.scale)

    @property
    def limiting_radius(self) -> float:
        return self.length / (1 - self.scale) if self.scale < 1 else math.inf

    @property
    def similarity_dimension(self) -> float | None:
        if self.scale == 1:
            return None
        return math.log(self.spokes) / -math.log(self.scale)

    @property
    def separation_threshold(self) -> float:
        s = math.sin(math.pi / self.spokes)
        return s / (1 + s)

    @property
    def certified_endpoint_dimension(self) -> float | None:
        """A dimension claim only in explicitly proved cases.

        The disk criterion is sufficient, not necessary. The special cases at
        scale 1/2 are the Sierpinski triangle and, for every even number of
        directions, the filled regular polygon.
        """
        if self.scale < self.separation_threshold:
            return self.similarity_dimension
        if self.scale == 0.5 and self.spokes == 3:
            return self.similarity_dimension
        if self.scale == 0.5 and self.spokes % 2 == 0:
            return 2.0
        return None


@dataclass(frozen=True)
class Segment:
    start: complex
    end: complex
    generation: int


def _budget(count: int, maximum: int | None) -> None:
    if maximum is not None and (type(maximum) is not int or maximum < 0):
        raise ValueError("max_elements must be a nonnegative integer or None")
    if maximum is not None and count > maximum:
        raise ValueError(f"{count:,} elements exceed the budget of {maximum:,}; increase --max-elements explicitly")


def iter_segments(p: Parameters, max_elements: int | None = 1_000_000) -> Iterator[Segment]:
    """Draw all spokes of a node, then visit its children in angle order.

    This matches the original Turtle traversal. An explicit stack avoids
    Python's recursion limit. Pending traversal uses O(spokes * iterations)
    space; drawing/rendering time remains exponential in iterations.
    """
    _budget(p.segment_count, max_elements)
    if p.iterations == 0:
        return
    directions = p.directions
    stack = [(p.origin, p.length, 1)]
    while stack:
        start, length, generation = stack.pop()
        ends = [start + length * u for u in directions]
        for end in ends:
            yield Segment(start, end, generation)
        if generation < p.iterations:
            stack.extend((end, length * p.scale, generation + 1) for end in reversed(ends))


def iter_endpoints(p: Parameters, max_elements: int | None = 1_000_000) -> Iterator[complex]:
    """Enumerate depth-n addresses in lexicographic order, with multiplicity."""
    _budget(p.endpoint_count, max_elements)
    directions = p.directions
    stack = [(p.origin, p.length, 0)]
    while stack:
        start, length, depth = stack.pop()
        if depth == p.iterations:
            yield start
        else:
            stack.extend(
                (start + length * u, length * p.scale, depth + 1)
                for u in reversed(directions)
            )


def chaos_points(p: Parameters, samples: int = 100_000, seed: int = 20260930,
                 burn_in: int | None = None, max_elements: int | None = 1_000_000) -> Iterator[complex]:
    """Reproducible chaos-game sample of the compact endpoint IFS, not the trace.

    Iteration count is irrelevant here. This is a finite stochastic sample,
    never an exact plot of the attractor. Burn-in defaults to a bound making
    the initial-position error <= 1e-12 times its limiting radius.
    """
    if not 0 < p.scale < 1:
        raise ValueError("chaos mode requires 0 < scale < 1")
    if type(samples) is not int or samples < 0:
        raise ValueError("samples must be a nonnegative integer")
    _budget(samples, max_elements)
    if burn_in is None:
        burn_in = max(1, math.ceil(math.log(1e-12) / math.log(p.scale)))
    if type(burn_in) is not int or burn_in < 0:
        raise ValueError("burn_in must be a nonnegative integer")
    rng = random.Random(seed)
    offsets = tuple(p.length * u for u in p.directions)
    x = 0j
    for _ in range(burn_in):
        x = p.scale * x + rng.choice(offsets)
    for _ in range(samples):
        x = p.scale * x + rng.choice(offsets)
        yield p.origin + x


def statistics(p: Parameters) -> dict:
    d = p.certified_endpoint_dimension
    total = 0.0
    q = p.spokes * p.scale
    term = p.spokes * p.length
    for _ in range(p.iterations):
        total += term
        term *= q
    return {
        "software_version": __version__,
        "spokes": p.spokes, "iterations": p.iterations,
        "angle_degrees": 360 / p.spokes,
        "length": p.length, "scale": p.scale,
        "phase_degrees": p.phase_degrees,
        "origin": [p.origin.real, p.origin.imag],
        "drawing_commands": p.segment_count,
        "endpoint_addresses": p.endpoint_count,
        "radius_bound": p.radius,
        "total_length_with_multiplicity": total if math.isfinite(total) else None,
        "similarity_dimension": p.similarity_dimension,
        "certified_endpoint_Hausdorff_dimension": d,
        "certified_closed_trace_Hausdorff_dimension": max(1.0, d) if d is not None else None,
        "sufficient_separation_threshold": p.separation_threshold,
        "dimension_note": "Similarity dimension is not a measured dimension; an uncertified value is null. Closed-trace dimension refers to infinite contractive closure, not a finite drawing.",
    }
