# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`parka-data-boundary` is a thin manifest package for geographic boundary data. The actual data files are packaged as GitHub Release assets and downloaded on-demand by the `parka` library.

### Data included

- **Natural Earth** boundary data (countries and states/provinces) in SQLite format — versions v4.1.0, v5.0.0, v5.1.2
- **Regional administrative boundaries** for: Argentina, Bolivia, Brazil, Colombia, Dominican Republic, Guyana, Kyrgyzstan, Mexico, Panama, Puerto Rico, Tajikistan

## Architecture

- `assets.yaml` — declarative registry of all boundary datasets (source paths, extract targets)
- `src/parka_data_boundary/` — thin Python package exposing `get_manifest()` with checksums, sizes, download URLs
- `src/parka_data_boundary/packaging.py` — CLI to build `.tar.gz` archives and generate `manifest.json`
- `data/boundary/` — source data files (region shapefiles, Natural Earth SQLite)
- `.github/workflows/release.yml` — tag push → build assets → GitHub Release + wheel

## Development Commands

```bash
pip install -e .                    # Install in dev mode
ruff check . && ruff format .       # Lint and format
pytest                              # Run tests
```

### Building assets locally

```bash
PYTHONPATH=src python -m parka_data_boundary.packaging build --tag v0.2.0 --output dist/
```

### Adding new boundary data

1. Place files in `data/boundary/region/{country_code}/` or `data/boundary/naturalearth/v{version}/`
2. Add an entry to `assets.yaml`
3. Tag a new release — CI builds the archives and publishes them

## Key Configuration

- **Ruff**: 120 character line length, numpy docstring convention
- **Setuptools**: Uses `setuptools_scm` for version management
- **Manifest**: `manifest.json` is generated at build time and shipped in the wheel
