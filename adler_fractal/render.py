"""Headless SVG export (standard library), plus optional Matplotlib PNG export."""

from html import escape
from pathlib import Path
from .core import Parameters, chaos_points, iter_endpoints, iter_segments


COLORS = ("#243d55", "#23858b", "#ad6036", "#655394", "#55854a")


def write_svg(path, p: Parameters, mode="trace", samples=100_000, seed=20260930,
              max_elements=1_000_000, stroke_width=0.45) -> None:
    if mode not in ("trace", "endpoints", "chaos"):
        raise ValueError("mode must be trace, endpoints, or chaos")
    if stroke_width <= 0:
        raise ValueError("stroke_width must be positive")
    radius = p.limiting_radius if mode == "chaos" else p.radius
    radius = max(radius, p.length / 100) * 1.04
    title = f"Adler construction: {mode}; m={p.spokes}, n={p.iterations}, L={p.length:g}, r={p.scale:g}"
    # Prime the iterator before creating a file so budget/parameter errors do
    # not leave a partial export behind.
    if mode == "trace":
        iterator = iter_segments(p, max_elements)
    elif mode == "endpoints":
        iterator = iter_endpoints(p, max_elements)
    else:
        iterator = chaos_points(p, samples, seed, max_elements=max_elements)
    first = next(iterator, None)
    from itertools import chain
    items = chain((), iterator) if first is None else chain((first,), iterator)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1600" viewBox="{-radius:g} {-radius:g} {2*radius:g} {2*radius:g}">\n')
        f.write(f"<title>{escape(title)}</title>\n")
        f.write(f'<rect x="{-radius:g}" y="{-radius:g}" width="{2*radius:g}" height="{2*radius:g}" fill="#faf9f5"/>\n')
        f.write('<g transform="scale(1,-1)">\n')
        if mode == "trace":
            for s in items:
                a, b = s.start - p.origin, s.end - p.origin
                color = COLORS[(s.generation - 1) % len(COLORS)]
                f.write(f'<path d="M {a.real:.12g} {a.imag:.12g} L {b.real:.12g} {b.imag:.12g}" stroke="{color}" stroke-width="{stroke_width:g}" fill="none" opacity="0.65"/>\n')
        else:
            point_radius = radius / 900
            for x in items:
                x -= p.origin
                f.write(f'<circle cx="{x.real:.12g}" cy="{x.imag:.12g}" r="{point_radius:.12g}" fill="#23858b" opacity="0.55"/>\n')
        f.write("</g></svg>\n")


def draw_axes(ax, p: Parameters, mode="trace", samples=100_000, seed=20260930,
              max_elements=1_000_000, linewidth=0.35, alpha=0.65) -> None:
    from matplotlib.collections import LineCollection
    radius = p.limiting_radius if mode == "chaos" else p.radius
    radius = max(radius, p.length / 100) * 1.035
    if mode == "trace":
        groups = {}
        for s in iter_segments(p, max_elements):
            a, b = s.start - p.origin, s.end - p.origin
            groups.setdefault(s.generation, []).append(((a.real, a.imag), (b.real, b.imag)))
        for k, lines in groups.items():
            ax.add_collection(LineCollection(lines, colors=COLORS[(k - 1) % len(COLORS)], linewidths=linewidth, alpha=alpha))
    else:
        if mode == "endpoints":
            points = iter_endpoints(p, max_elements)
        elif mode == "chaos":
            points = chaos_points(p, samples, seed, max_elements=max_elements)
        else:
            raise ValueError("mode must be trace, endpoints, or chaos")
        xy = [x - p.origin for x in points]
        ax.scatter([x.real for x in xy], [x.imag for x in xy], s=0.12, color=COLORS[1], alpha=alpha, edgecolors="none", rasterized=True)
    ax.set(xlim=(-radius, radius), ylim=(-radius, radius), aspect="equal")
    ax.set_axis_off()
    ax.set_facecolor("#faf9f5")


def write_png(path, p: Parameters, **kwargs) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#faf9f5")
    draw_axes(ax, p, **kwargs)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=240, facecolor=fig.get_facecolor())
    plt.close(fig)
