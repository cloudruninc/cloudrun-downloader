import os
import requests
import sys

CLOUDRUN_USER_ID = os.environ['CLOUDRUN_USER_ID']
CLOUDRUN_API_TOKEN = os.environ['CLOUDRUN_API_TOKEN']

CLOUDRUN_API_URL = 'https://api.cloudrun.co/v1'
AUTH_HEADER = {'Authorization': 'Bearer ' + CLOUDRUN_API_TOKEN + '|' + CLOUDRUN_USER_ID}

MAX_FORECASTS = 10000 # sufficiently large number; fix later

def get_forecast(forecast_id: str) -> str:
    """Gets a forecast from Cloudrun API."""
    url = CLOUDRUN_API_URL + '/forecasts/' + forecast_id
    r = requests.get(url, headers=AUTH_HEADER)
    r.raise_for_status()
    return r.json()


def get_latest_forecasts(amount_to_get: int = 10):
    """Gets the latest forecasts."""
    url = CLOUDRUN_API_URL + '/forecasts/latest'
    data = {'user_id': CLOUDRUN_USER_ID, 'amount_to_get': amount_to_get}
    r = requests.get(url, data=data, headers=AUTH_HEADER)
    r.raise_for_status()
    resp_body = r.json()
    count, forecasts = int(resp_body['count']), resp_body['forecasts']
    return count, forecasts


def list_forecasts(amount_to_get: int = 10) -> None:
    """Lists a number of latest forecasts with their status."""
    count, forecasts = get_latest_forecasts(amount_to_get)
    for f in forecasts:
        print(f['name'], f['status'])
    forecasts_shown = amount_to_get if amount_to_get <= count else count
    print('Showing '  + str(forecasts_shown) + '/' + str(count) + ' forecasts total')


def download_file(forecast_id: str, filename: str, filesize: int) -> int:
    """Stream downloads a forecast output file."""
    CHUNK_SIZE = 1024**2
    n = 0
    url = CLOUDRUN_API_URL + '/forecasts/' + forecast_id + '/outputs/' + filename
    with requests.get(url, headers=AUTH_HEADER, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
                n += 1
                bytes_downloaded = n * CHUNK_SIZE
                percent_downloaded = (n * CHUNK_SIZE / filesize) * 100
                if percent_downloaded > 100:
                    percent_downloaded = 100
                sys.stdout.write('\r')
                sys.stdout.flush()
                sys.stdout.write('Downloading ' + filename + '... ' + '%.1f' % percent_downloaded + ' %')
                sys.stdout.flush()
    sys.stdout.write('\n')
    return os.stat(filename).st_size
