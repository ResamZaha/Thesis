from time import sleep
from os import system, name
import json
import urllib.request
import datetime
from urllib.error import HTTPError, URLError
import socket
dt = datetime.datetime(2004, 1, 1)
end = datetime.datetime(2023, 1, 1)

step = datetime.timedelta(days=1)

result = []


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def padDate(dtx):
    if(len(dtx) < 2):
        dtx = "0"+dtx
    return dtx


def getFileName(dt):
    return "data_sf/weather_data_"+str(dt.year)+"_"+str(dt.month)+"_"+str(dt.day)+".json"


while dt < end:
    # https://api.weather.com/v2/astro?apiKey=e1f10a1e78da46f5b10a1e78da96f525&geocode=37.62,-122.40&days=10&date=20050527&format=json
    url = "https://api.weather.com/v1/location/KSFO:9:US/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=m&startDate=" + \
        str(dt.year)+padDate(str(dt.month))+padDate(str(dt.day))
    print(url)
    dt += step
    try:
        with urllib.request.urlopen(url, timeout=5) as url:
            data = json.loads(url.read().decode())
            with open(getFileName(dt), 'w') as fp:
                json.dump(data, fp)
    except HTTPError as error:
        print(error)
        continue

    except URLError as error:
        if isinstance(error.reason, socket.timeout):
            continue
        else:
            continue
    except socket.timeout as error:
        continue
    clear()
    