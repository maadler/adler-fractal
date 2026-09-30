"""Build the release ZIP for the current commit.

Run from a clean git checkout: python3 scripts/package_release.py

The archive dist/Adler_Fraktal_v<version>.zip contains every tracked file
except hidden ones, plus a MANIFEST.sha256 that exists only inside the ZIP.
Entries are sorted and carry the time of the packaged commit, so building the
same commit twice gives the same archive.
"""
from pathlib import Path
import hashlib
import subprocess
import sys
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from adler_fractal import __version__


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout


if git("status", "--porcelain").strip():
    sys.exit("The working tree has uncommitted changes; commit them first.")

names = sorted(n for n in git("ls-files", "-z").split("\0")
               if n and not any(part.startswith(".") for part in Path(n).parts))
files = [(n, (ROOT / n).read_bytes()) for n in names]
manifest = "".join(f"{hashlib.sha256(data).hexdigest()}  {n}\n" for n, data in files)
stamp = time.gmtime(int(git("log", "-1", "--format=%ct")))[:6]
prefix = f"adler_fractal_v{__version__}"

dest = ROOT / "dist" / f"Adler_Fraktal_v{__version__}.zip"
dest.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(dest, "w") as z:
    for n, data in files + [("MANIFEST.sha256", manifest.encode("utf-8"))]:
        info = zipfile.ZipInfo(f"{prefix}/{n}", date_time=stamp)
        info.external_attr = 0o644 << 16
        z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
with zipfile.ZipFile(dest) as z:
    bad = z.testzip()
    if bad:
        raise RuntimeError(f"Corrupted ZIP entry: {bad}")
print(f"Created {dest.relative_to(ROOT)}: {len(files) + 1} files, {dest.stat().st_size:,} bytes")
print(f"SHA-256 {hashlib.sha256(dest.read_bytes()).hexdigest()}")
