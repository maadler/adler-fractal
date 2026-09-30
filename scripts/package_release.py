"""Build a distributable ZIP and SHA-256 manifest after tests and PDF review.

Run from the project root: python3 scripts/package_release.py
Generated Python caches and intermediate TeX build files are excluded.
"""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT.parent / "Adler_Fraktal_v1.0.0.zip"


def files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and "__pycache__" not in p.parts
                  and p.name != "MANIFEST.sha256"
                  and p.suffix not in (".pyc", ".aux", ".log", ".out", ".xdv"))


items = files()
manifest = ROOT / "MANIFEST.sha256"
manifest.write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n" for p in items), encoding="utf-8")
with zipfile.ZipFile(DEST, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in items + [manifest]:
        z.write(p, arcname=f"{ROOT.name}/{p.relative_to(ROOT).as_posix()}")
with zipfile.ZipFile(DEST) as z:
    bad = z.testzip()
    if bad:
        raise RuntimeError(f"Corrupted ZIP entry: {bad}")
print(f"Created {DEST.name}: {len(items)+1} files, {DEST.stat().st_size:,} bytes")
