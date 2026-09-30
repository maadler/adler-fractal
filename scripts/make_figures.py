"""Reproduce all figures in the manuscript. Run from the project root."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from adler_fractal import Parameters
from adler_fractal.render import draw_axes, write_png, write_svg

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def panel_file(fig, name):
    fig.savefig(FIG / (name + ".png"), dpi=240, facecolor=fig.get_facecolor())
    fig.savefig(FIG / (name + ".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)


original = Parameters()
write_svg(FIG / "adler_original.svg", original)
write_png(FIG / "adler_original.png", original, linewidth=.24, alpha=.52)

fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.65), facecolor="#faf9f5")
for ax, n in zip(axes, (1, 2, 3)):
    p = Parameters(spokes=12, iterations=n, length=1)
    draw_axes(ax, p, linewidth=.37, alpha=.6)
    ax.set_title(f"m = 12, r = 1, n = {n}\n{p.segment_count:,} drawing commands", fontsize=10, pad=11)
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.82, wspace=.14)
panel_file(fig, "equal_length_stages")

fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), facecolor="#faf9f5")
p = Parameters(spokes=3, iterations=8, length=1, scale=.5, phase_degrees=90)
draw_axes(axes[0], p, linewidth=.25, alpha=.72)
draw_axes(axes[1], p, mode="chaos", samples=100_000, seed=20260930, alpha=.75)
axes[0].set_title("Accumulated trace A8\nRoot spokes remain present", fontsize=11, pad=12)
axes[1].set_title("Endpoint-attractor sample K\nSierpinski triangle; 100,000 samples", fontsize=11, pad=12)
fig.subplots_adjust(left=.025, right=.975, bottom=.025, top=.83, wspace=.17)
panel_file(fig, "trace_vs_endpoints")

fig, axes = plt.subplots(2, 3, figsize=(10.8, 7.4), facecolor="#faf9f5")
variants = [
    (Parameters(spokes=3, length=1, scale=.5, phase_degrees=90), "Sierpinski triangle", "dim H = 1.584963"),
    (Parameters(spokes=4, length=1, scale=.5, phase_degrees=45), "Filled square", "dim H = 2"),
    (Parameters(spokes=8, length=1, scale=.25), "Separated octagonal IFS", "dim H = 1.5"),
    (Parameters(spokes=8, length=1, scale=.1), "Separated endpoint dust", "dim H = 0.903090"),
    (Parameters(spokes=72, length=1, scale=.03), "72-direction separated IFS", "dim H = 1.219619"),
    (Parameters(spokes=72, length=1, scale=.5), "Overlapping 72-direction IFS", "dim H not established here"),
]
for ax, (p, title, dim) in zip(axes.flat, variants):
    draw_axes(ax, p, mode="chaos", samples=120_000, seed=20260930, alpha=.65)
    ax.set_title(f"{title}\nm = {p.spokes}, r = {p.scale:g}\n{dim}", fontsize=9.3, pad=9)
fig.subplots_adjust(left=.015, right=.985, bottom=.025, top=.885, wspace=.17, hspace=.52)
panel_file(fig, "endpoint_variants")
print("Generated original SVG/PNG and three PNG/PDF figure pairs.")
