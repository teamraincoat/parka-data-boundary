import json
from importlib.metadata import version
from pathlib import Path

__version__ = version("parka-data-boundary")


def get_manifest() -> dict:
    """Load the asset manifest shipped with this package.

    Returns
    -------
    dict
        Manifest containing ``github_repo``, ``release_tag``, and ``assets``.
    """
    manifest_path = Path(__file__).parent / "manifest.json"
    return json.loads(manifest_path.read_text())
