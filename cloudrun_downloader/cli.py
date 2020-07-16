import argparse
from cloudrun_downloader.forecasts import download_file, get_forecast, get_latest_forecasts, list_forecasts, MAX_FORECASTS
import requests


def cli():

    parser = argparse.ArgumentParser(description='cloudrun-downloader - Download your Cloudrun output files')
    parser.add_argument('forecast', type=str, help='Forecast to download', nargs='?', default=None)
    parser.add_argument('-n','--how-many', type=int, help='How many forecasts to list', default=10)
    parser.add_argument('-nc', '--netcdf-only', action='store_true', help='Download NetCDF files only')
    parser.add_argument('-g', '--grib-only', action='store_true', help='Download GRIB files only')

    args = parser.parse_args()

    if not args.forecast:
        list_forecasts(args.how_many)
    else:

        if args.netcdf_only:
            file_extensions = ['zip']
        elif args.grib_only:
            file_extensions = ['grb']
        else:
            file_extensions = ['grb', 'zip']

        count, forecasts = get_latest_forecasts(MAX_FORECASTS)
        forecast_names = [f['name'] for f in forecasts]
        if args.forecast in forecast_names:
            forecast_ = next(f for f in forecasts if f['name'] == args.forecast)

            if not forecast_['status'] in ['complete', 'running_model']:
                print(args.forecast + ' did not start yet. Try again later.')
        
            if forecast_['status'] == 'running_model':
                print('Warning: ' + args.forecast + ' is running but not complete yet.')
                print('Only GRIB files in progress can be downloaded.')

            forecast = get_forecast(forecast_['id'])
            output_files = forecast['output_files']
            for output_file in output_files:
                if output_file['name'][-3:] in file_extensions:
                    download_file(forecast['id'], output_file['name'], output_file['size'])
        else:
            print('No forecast found under name ' + args.forecast)
