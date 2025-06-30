# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python data package (`parka-data-boundary`) that provides geographic boundary data files for the Raincoat/Parka system. It's a pure data distribution package that includes:

- Natural Earth boundary data (countries and states/provinces) in SQLite format across multiple versions (v4.1.0, v5.0.0, v5.1.2)
- Regional administrative boundary data for various countries including Latin America and Central Asia (Argentina, Bolivia, Brazil, Colombia, Dominican Republic, Guyana, Kyrgyzstan, Mexico, Panama, Puerto Rico, Tajikistan)

## Architecture

The package is structured as a setuptools-based Python package with the primary purpose of distributing geographic data files:

- `src/parka_data_boundary/`: Minimal Python package code (just version handling)
- `data/boundary/`: Core data files organized by source and region
  - `naturalearth/`: Natural Earth vector data in SQLite format by version
  - `region/`: Country-specific administrative boundary data as ZIP files
- `setup.py`: Custom data file packaging logic that maps `data//boundary/**/*.*` to `share/parka/`

## Development Commands

### Setup and Installation
```bash
pip install -e .
```

### Code Quality
```bash
ruff check .          # Lint code
ruff format .         # Format code
```

### Testing
```bash
pytest                # Run tests (basic pytest configuration present)
```

### Build and Distribution
```bash
python -m build --wheel           # Build wheel package
./deploy/upload.sh               # Upload to GitLab package registry
```

## Key Configuration

- **Ruff**: Configured for 120 character line length with numpy docstring convention
- **Setuptools**: Uses `setuptools_scm` for version management
- **Data Files**: Custom setup.py logic handles recursive data file inclusion from `data//boundary/` to `share/parka/`
- **Package Registry**: Configured to use GitLab package registry at `https://gitlab.com/api/v4/projects/20210002/packages/pypi/simple`

## Working with Data Files

The package's main functionality is data distribution. When adding new boundary data:

1. Place files in appropriate subdirectories under `data/boundary/`
2. Natural Earth data goes in `data/boundary/naturalearth/[version]/`
3. Regional data goes in `data/boundary/region/[country_code]/`
4. The custom `setup.py` will automatically include them in the package

## Development Notes

- This is primarily a data package with minimal Python code
- The main technical complexity is in the data file packaging logic in `setup.py`
- Version management is handled automatically by `setuptools_scm`
- The package is designed for installation via pip from a private GitLab registry
