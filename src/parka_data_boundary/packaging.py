"""Build boundary data assets and generate manifest.json.

Usage::

    python -m parka_data_boundary.packaging build --tag v0.2.0 --output dist/

Reads ``assets.yaml``, creates ``.tar.gz`` archives for each entry,
computes SHA-256 checksums, and writes ``manifest.json`` into the
package source directory (so it ships with the wheel).
"""

import argparse
import hashlib
import json
import tarfile
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[2]  # repo root
_ASSETS_YAML = _ROOT / "assets.yaml"
_MANIFEST_DEST = Path(__file__).resolve().parent / "manifest.json"

_CHUNK_SIZE = 256 * 1024


def _sha256_file(path: Path) -> str:
    sha = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(_CHUNK_SIZE):
            sha.update(chunk)
    return sha.hexdigest()


def _build_tarball(name: str, source_dir: Path, output_dir: Path) -> tuple[Path, str, int]:
    """Create a .tar.gz from *source_dir* and return (path, sha256, size)."""
    archive_path = output_dir / f"{name}.tar.gz"
    with tarfile.open(archive_path, "w:gz") as tf:
        for item in sorted(source_dir.rglob("*")):
            if item.is_file():
                arcname = str(item.relative_to(source_dir))
                tf.add(item, arcname=arcname)
    sha = _sha256_file(archive_path)
    size = archive_path.stat().st_size
    return archive_path, sha, size


def build(tag: str, output_dir: Path, assets_yaml: Path | None = None) -> dict:
    """Build all assets and generate the manifest.

    Parameters
    ----------
    tag
        Git release tag (e.g. ``"v0.2.0"``).
    output_dir
        Directory to write ``.tar.gz`` files into.
    assets_yaml
        Path to assets.yaml (defaults to repo root).

    Returns
    -------
    dict
        The generated manifest.
    """
    assets_yaml = assets_yaml or _ASSETS_YAML
    with open(assets_yaml) as fh:
        config = yaml.safe_load(fh)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    repo_root = assets_yaml.parent

    manifest = {
        "github_repo": config["github_repo"],
        "release_tag": tag,
        "assets": {},
    }

    for name, entry in config["assets"].items():
        source_dir = repo_root / entry["path"]
        if not source_dir.is_dir():
            raise FileNotFoundError(f"Asset source directory not found: {source_dir}")

        archive_path, sha, size = _build_tarball(name, source_dir, output_dir)
        manifest["assets"][name] = {
            "file": archive_path.name,
            "sha256": sha,
            "size": size,
            "extract_to": entry["extract_to"],
        }
        print(f"  {name}: {archive_path.name} ({size / 1_000_000:.1f} MB, sha256={sha[:12]}…)")

    # Write manifest.json into the package source so it ships with the wheel
    _MANIFEST_DEST.parent.mkdir(parents=True, exist_ok=True)
    with open(_MANIFEST_DEST, "w") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    print(f"  manifest.json → {_MANIFEST_DEST}")

    return manifest


def main():
    parser = argparse.ArgumentParser(description="Build boundary data assets")
    sub = parser.add_subparsers(dest="command")

    build_cmd = sub.add_parser("build", help="Build .tar.gz assets and generate manifest.json")
    build_cmd.add_argument("--tag", required=True, help="Release tag (e.g. v0.2.0)")
    build_cmd.add_argument("--output", default="dist/", help="Output directory for archives")
    build_cmd.add_argument("--assets-yaml", default=None, help="Path to assets.yaml")

    args = parser.parse_args()
    if args.command == "build":
        assets_yaml = Path(args.assets_yaml) if args.assets_yaml else None
        build(tag=args.tag, output_dir=Path(args.output), assets_yaml=assets_yaml)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
