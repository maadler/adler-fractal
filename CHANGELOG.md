# Changelog

## 1.0.1 — 2026-09-30

A corrected edition. The definitions and the three propositions of the report are unchanged. Zenodo DOI [10.5281/zenodo.23063185](https://doi.org/10.5281/zenodo.23063185).

**Original script**

- `original/eagle_fractal.py`: `draw_fractal` now draws with the turtle it is given instead of a module-level global `turt`, so it also works when imported. Type hints say `float` where floats arrive. The drawing is the same; the test still compares all 5,256 segments in order.
- The file as first published (SHA-256 `235b6e65737b24535ded79af19b89842ed5864e2b3e8ac2b24b80c17d10bd85d`) stays available under the tag `v1.0.0` and in the Zenodo record of version 1.0.0.

**Report**

- Section 5 no longer states that the closed trace always differs from the endpoint attractor. The two coincide exactly when the initial star lies in the attractor, for example for four directions at scale 1/2.
- The case of 72 directions at scale 1/2 is no longer "undetermined": for an even number of directions at scale 1/2 the endpoint attractor is the whole filled polygon, of dimension 2 (new subsection in Section 4). The last panel of Figure 4 got a new title; its pale center is a sampling effect.
- Typesetting: the number 1,051,200 on page 3, the list of output modes on page 8, the empty band under Figure 3.
- Smaller precisions of wording, an updated title block, and a text that speaks in my own voice instead of about me.
- The LaTeX source no longer depends on fonts installed in the system and builds with Tectonic.

**Software**

- `certified_endpoint_dimension` returns 2 for an even number of directions at scale 1/2.
- The version number lives in one place, `adler_fractal/_version.py`.
- `pyproject.toml` requires setuptools 77 or newer; with the older versions it allowed before, the package did not build.
- `scripts/package_release.py` packs the tracked files of a clean checkout; `scripts/make_figures.py` also writes `figures/octagonal_trace.svg`.

**Repository**

- README rewritten in English. The formulas in `docs/SPEZIFIKATION.md` now render on GitHub.
- Removed working notes from before the publication (`docs/VEROEFFENTLICHUNG.md`, `docs/PUBLIKATIONSMETADATEN.json`, `scripts/verification_report.json`) and the checked-in `MANIFEST.sha256`, which is now written into the release ZIP only.
- Added `.gitignore` and a test run on GitHub for Python 3.10 to 3.14.

## 1.0.0 — 2026-09-30

First public version. Zenodo DOI [10.5281/zenodo.23057945](https://doi.org/10.5281/zenodo.23057945).
