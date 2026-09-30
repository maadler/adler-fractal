"""Adler radial construction. Geometry is independent of GUI and plotting libraries."""

from .core import Parameters, Segment, chaos_points, iter_endpoints, iter_segments

__version__ = "1.0.0"
__all__ = ["Parameters", "Segment", "chaos_points", "iter_endpoints", "iter_segments"]
