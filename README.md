# Adler Fractal

Seventy-two spokes from one point — and the same seventy-two again from the tip of every spoke.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23057944.svg)](https://doi.org/10.5281/zenodo.23057944)
[![tests](https://github.com/maadler/adler-fractal/actions/workflows/tests.yml/badge.svg)](https://github.com/maadler/adler-fractal/actions/workflows/tests.yml)

<p align="center">
  <img src="figures/adler_original.png" width="560" alt="The original drawing: 72 directions, two generations, 5,256 line segments">
</p>

That is all the drawing rule does. I wrote it in September 2026 as a short Python Turtle script ([`original/eagle_fractal.py`](original/eagle_fractal.py) — *Adler* is German for eagle), liked the picture, and wanted to know what I had actually drawn. This repository is the long answer: a precise definition, proofs, a reference implementation that needs no Turtle window, and a nine-page [report](docs/Adler_Fractal_Manuscript.pdf).

The short answer is more modest than the name. The finite drawing is a union of line segments, so its dimension is 1. Continued forever with spokes of equal length, the endpoints come arbitrarily close to every point of the plane — there is no bounded limit figure. Only when the spokes shrink from generation to generation does a classical fractal limit appear, and that limit is a well-known one: a regular polygon iterated function system. So I claim no new fractal family and no priority. *Adler Fractal* is simply my name for this drawing rule and its variants.

## Results at a glance

| Object | Result |
| --- | --- |
| Original: 72 directions, length 200, depth 2 | 5,256 drawing commands, outer radius 400 |
| Endpoints of the second generation | 5,184 addresses, but only 2,593 distinct points |
| Depth 3 / depth 4 | 378,504 / 27,252,360 drawing commands |
| Any finite drawing of positive depth | Hausdorff dimension 1 |
| Equal-length original, all generations together | Endpoints dense in the plane; the closure of the lines is the whole plane |
| Shrinking spokes, `0 < r < 1`: the endpoints | Compact attractor of the maps `f_j(x) = L·u_j + r·x`, which are contractions about the corners of a regular polygon |
| Shrinking spokes: the closure of all lines | The endpoint attractor plus the countably many drawn segments; dimension `max(1, dim K)` |
| Three directions, `r = 1/2` | Sierpinski triangle, dimension log 3 / log 2 ≈ 1.585 |
| An even number of directions, `r = 1/2` | The whole filled polygon, dimension 2 — for 72 directions a filled 72-gon |

A scale factor below 1 alone does not make a set of fractional dimension, as the last row shows. And a picture being finite is no argument either way: every fractal is drawn as a finite approximation. What the report analyzes is the rule and the sets it defines.

## Try it

Python 3.10 or newer is enough for the geometry, the tests and the SVG export; nothing has to be installed. Run the commands from the project folder. (The `python3` that ships with macOS can still be 3.9.)

```bash
python3 -m adler_fractal --output adler_original.svg
python3 -m adler_fractal --angle 5 --iterations 2 --length 200 --scale 1 --stats
python3 -m adler_fractal --spokes 8 --iterations 4 --scale 0.25 --output octagonal_trace.svg
python3 -m adler_fractal --spokes 8 --scale 0.25 --mode chaos --samples 100000 --output octagonal_endpoints.svg
python3 -m unittest discover -s tests -v
```

There are three modes. `trace` draws every segment down to the given depth. `endpoints` draws only the endpoints of the last generation, once per address. `chaos` draws a reproducible random sample of the infinite endpoint set of a shrinking variant; the depth plays no role there.

PNG output and the figures of the report need Matplotlib. The pinned versions require Python 3.11 or newer; the figures were produced with Python 3.12 and reproduced with 3.14.

```bash
python3 -m pip install -r requirements.txt
python3 -m adler_fractal --output adler_original.png
python3 scripts/make_figures.py
```

`make_figures.py` rewrites the files in `figures/`.

For a Turtle window, on a machine with Tk:

```bash
python3 original/eagle_fractal.py
python3 turtle_reference.py
```

The first is my original script, the second draws the output of the reference implementation with a real Turtle.

The report is built with [Tectonic](https://tectonic-typesetting.github.io/):

```bash
tectonic docs/Adler_Fractal_Manuscript.tex
```

With a fixed `SOURCE_DATE_EPOCH` two builds give the same file, byte for byte.

## What is where

| Path | What it is |
| --- | --- |
| `original/eagle_fractal.py` | My original Turtle script. Version 1.0.1 fixes one thing in it, see below |
| `adler_fractal/` | Reference implementation: geometry and SVG export, standard library only |
| `turtle_reference.py` | The reference implementation drawn with a real Turtle |
| `tests/` | 12 tests, among them a comparison of all 5,256 segments with the original script |
| `docs/Adler_Fractal_Manuscript.pdf` | The report, in English, with its LaTeX source next to it |
| `docs/SPEZIFIKATION.md` | The mathematical specification, in German |
| `docs/LITERATURPRUEFUNG.md` | What the literature check covered and what it did not, in German |
| `figures/` | The figures of the report and two SVG exports |
| `scripts/make_figures.py` | Regenerates the figures |
| `scripts/package_release.py` | Builds the release ZIP with SHA-256 checksums |
| `CITATION.cff`, `CHANGELOG.md` | Citation data and version history |
| `LICENSE`, `LICENSE_DOCUMENTATION.md` | MIT for the software, CC BY 4.0 for text and figures |

The fix in the original script: `draw_fractal` was handed a turtle but drew with a global one, so it only worked when run as a script. It now uses the turtle it is given. The drawing is the same, line for line; the file as first published is kept under the tag `v1.0.0`.

## Reproducibility and limits

The mathematical definition is exact; the generator computes with Python floats. Colors, stroke width, resolution and overdraw change how a rendering looks, not the set it shows. Address multiplicity and repeated segments are preserved on purpose, and rounded coordinates that coincide numerically are not a proof that two points are equal.

With the pinned Matplotlib and NumPy the PNG figures come out pixel-identical on my machine. The SVG export matches except for floating-point noise around 1e-14 in a handful of coordinates.

By default the export refuses to draw or sample more than one million elements. The original at depth 4 has 27 million commands and is rejected before anything is written; `--max-elements` raises the limit. Matplotlib collects the geometry in memory, SVG is written as a stream. No optimization removes the exponential growth of the fully written-out recursion.

## Citing

> Marcus Adler: *The Adler Fractal: A Recursive Radial Drawing and Its Polygon-IFS Limits.* Technical report, version 1.0.1. Zenodo, 2026. https://doi.org/10.5281/zenodo.23057944

This DOI always resolves to the latest version; every version also has a DOI of its own on Zenodo. Machine-readable data is in [`CITATION.cff`](CITATION.cff).

## License

The software is under the [MIT license](LICENSE), the text and the figures under CC BY 4.0. [`LICENSE_DOCUMENTATION.md`](LICENSE_DOCUMENTATION.md) says which file belongs where.

## How this was made

The drawing rule, the original script and the name are mine. The formalization, the proofs, the text of the report and the reference implementation were prepared with AI assistance (OpenAI ChatGPT; revised with Anthropic Claude for version 1.0.1). The numbers are covered by the tests and the references were checked against the sources, but there has been no independent mathematical review. If you find a mistake, please open an issue.

## Versions

- **1.0.1** — corrected original script and revised report; details in the [changelog](CHANGELOG.md).
- **1.0.0** — first public version, DOI [10.5281/zenodo.23057945](https://doi.org/10.5281/zenodo.23057945).
