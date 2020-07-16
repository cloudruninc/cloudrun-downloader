# cloudrun-downloader

CLI tool to query Cloudrun forecasts and download output files.

## Getting started

### Install cloudrun-downloader

```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -U git+https://github.com/cloudruninc/cloudrun-downloader
```

### Set environment variables

* `CLOUDRUN_USER_ID`
* `CLOUDRUN_API_TOKEN`

Write to us at accounts@cloudrun.co to obtain your user ID and API token.

## Example use

### Help menu

```
cloudrun-downloader -h
usage: cloudrun-downloader [-h] [-n HOW_MANY] [-nc] [-g] [forecast]

cloudrun-downloader - Download your Cloudrun output files

positional arguments:
  forecast              Forecast to download

optional arguments:
  -h, --help            show this help message and exit
  -n HOW_MANY, --how-many HOW_MANY
                        How many forecasts to list
  -nc, --netcdf-only    Download NetCDF files only
  -g, --grib-only       Download GRIB files only
```

### List 10 most recent forecasts

To list 10 most recent forecasts and their statuses,
simply run `cloudrun-downloader` without any arguments.

```
cloudrun-downloader
Hawaii_2020071612 running
Hawaii_2020071600 complete
Hawaii_2020071512 complete
Hawaii_2020071500 stopped
SF_Bay_2020062800 complete
SF_Bay_2020062700 complete
SF_Bay_2020062600 complete
SF_Bay_2020062500 complete
Skyrim_2011111100 complete
Bahrein_2020061000 stopped
Showing 10/272 forecasts total 
```

### List N most recent forecasts

To list an arbitrary number of recent forecasts,
pass the `-n` or `--how-many` flag:

```
cloudrun-downloader -n 50
cloudrun-downloader --how-many 50
```

### Download output files from a forecast

Download GRIB and NetCDF output files:

```
cloudrun-downloader SF_Bay_2020062800
```

Download only GRIB files:

```
cloudrun-downloader -g SF_Bay_2020062800
cloudrun-downloader --grib-only SF_Bay_2020062800
```

Download only NetCDF files:

```
cloudrun-downloader -nc SF_Bay_2020062800
cloudrun-downloader --netcdf-only SF_Bay_2020062800
```

## Need help?

Write to as at help@cloudrun.co.
