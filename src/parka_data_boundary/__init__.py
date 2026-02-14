import json
from pathlib import Path

try:
    from importlib.metadata import version

    __version__ = version("parka-data-boundary")
except Exception:
    __version__ = "0.0.0"


def get_manifest() -> dict:
    """Load the asset manifest shipped with this package.

    Returns
    -------
    dict
        Manifest containing ``github_repo``, ``release_tag``, and ``assets``.
    """
    manifest_path = Path(__file__).parent / "manifest.json"
    return json.loads(manifest_path.read_text())
