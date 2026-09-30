import argparse
import json
from pathlib import Path
from .core import Parameters, statistics
from .render import write_png, write_svg


def main() -> None:
    ap = argparse.ArgumentParser(description="Adler radial construction v1.0.0 (headless)")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--spokes", type=int)
    group.add_argument("--angle", type=int, help="positive integer divisor of 360; e.g. 5")
    ap.add_argument("--iterations", type=int, default=2)
    ap.add_argument("--length", type=float, default=200)
    ap.add_argument("--scale", type=float, default=1)
    ap.add_argument("--phase", type=float, default=0)
    ap.add_argument("--mode", choices=("trace", "endpoints", "chaos"), default="trace")
    ap.add_argument("--samples", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=20260930)
    ap.add_argument("--max-elements", type=int, default=1_000_000)
    ap.add_argument("--stats", action="store_true", help="print statistics without rendering")
    ap.add_argument("--output", type=Path, default=Path("adler_original.svg"))
    args = ap.parse_args()
    try:
        values = dict(iterations=args.iterations, length=args.length, scale=args.scale, phase_degrees=args.phase)
        p = Parameters.from_angle(args.angle, **values) if args.angle is not None else Parameters(spokes=72 if args.spokes is None else args.spokes, **values)
        if args.stats:
            print(json.dumps(statistics(p), ensure_ascii=False, indent=2, allow_nan=False))
            return
        if args.output.suffix.lower() == ".svg":
            write_svg(args.output, p, args.mode, args.samples, args.seed, args.max_elements)
        elif args.output.suffix.lower() == ".png":
            write_png(args.output, p, mode=args.mode, samples=args.samples, seed=args.seed, max_elements=args.max_elements)
        else:
            raise ValueError("output suffix must be .svg or .png")
    except (ValueError, OverflowError) as exc:
        ap.error(str(exc))
    except ImportError:
        ap.error("PNG export needs matplotlib; install requirements.txt or export SVG")
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
