# parka-data-boundary

Administrative boundary data for the [parka](https://github.com/teamraincoat/parka) geospatial library. This is a thin manifest package — the actual data files (~291 MB) are hosted as GitHub Release assets and downloaded on-demand.

## Installation

```bash
pip install parka-data-boundary
```

The boundary data is downloaded lazily when first accessed by parka and cached locally at `~/.cache/parka/boundary/`.

## Data Sources and Licensing

This package redistributes publicly available administrative boundary datasets. All data is sourced from authoritative government agencies and international organizations.

### Regional Administrative Boundaries

Most regional boundaries come from [OCHA Common Operational Datasets (COD-AB)](https://cod.unocha.org/) distributed through the [Humanitarian Data Exchange (HDX)](https://data.humdata.org/).

| Region | Source Agency | Distribution | License |
|--------|-------------|-------------|---------|
| Argentina (ar) | UNHCR | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-arg) | CC BY-IGO |
| Bolivia (bo) | Government of Bolivia / ITOS | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-bol) | CC BY-IGO |
| Brazil (br) | IBGE (Brazilian Institute of Geography and Statistics) | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-bra) | CC BY-IGO |
| Colombia (co) | Government of Colombia | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-col) / [WFP GeoNode](https://geonode.wfp.org/) | CC BY-IGO |
| Dominican Republic (do) | ONE (Oficina Nacional de Estadistica) | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-dom) | CC BY-IGO |
| Guyana (gy) | OCHA | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-guy) | CC BY-IGO |
| Kyrgyzstan (kg) | Ministry of Emergency Situations / ITOS | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-kgz) | CC BY-IGO |
| Mexico (mx) | Government of Mexico | [HDX COD-AB](https://data.humdata.org/dataset/mexican-administrative-level-0-country-1-estado-and-2-municipio-boundary-polygons) | CC BY-IGO |
| Panama (pa) | GADM / OCHA | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-pan) | CC BY-IGO |
| Puerto Rico (pr) | OCHA | [HDX COD-AB](https://data.humdata.org/dataset/cod-ab-pri) | CC BY-IGO |
| Tajikistan (tj) | geoBoundaries / geoLab, William & Mary | [geoBoundaries](https://www.geoboundaries.org/) | CC BY 4.0 |

**CC BY-IGO**: [Creative Commons Attribution for Intergovernmental Organisations](https://creativecommons.org/licenses/by/3.0/igo/). Requires attribution to the source agency and OCHA.

**CC BY 4.0**: Requires attribution and citation:

> Runfola, D. et al. (2020) geoBoundaries: A global database of political administrative boundaries. *PLoS ONE* 15(4): e0231866. https://doi.org/10.1371/journal.pone.0231866

### Natural Earth Data

| Version | Source | License |
|---------|--------|---------|
| v4.1.0, v5.0.0, v5.1.2 | [Natural Earth](https://www.naturalearthdata.com/) | **Public Domain** |

Natural Earth provides 1:10m cultural vectors for country boundaries (admin 0) and states/provinces (admin 1). All Natural Earth data is in the public domain — free to use for any purpose without restriction.

## How It Works

1. `parka-data-boundary` ships a `manifest.json` listing all available assets with SHA-256 checksums
2. When parka needs boundary data for a country, it checks the local cache
3. If not cached, it downloads the `.tar.gz` archive from the GitHub Release and extracts it
4. Integrity is verified via SHA-256 checksum

## Adding New Data

1. Place boundary files in `data/boundary/region/{country_code}/`
2. Add an entry to `assets.yaml`
3. Tag a new data release to build and upload assets
4. Bump the package version to ship the updated manifest

## License

The packaging code in this repository is MIT licensed. The boundary data files are distributed under their respective licenses as documented above.
