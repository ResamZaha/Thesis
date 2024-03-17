from time import sleep
from os import system, name
import json
import urllib.request
import datetime

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
    return "data_chicago/weather_data_"+str(dt.year)+"_"+str(dt.month)+"_"+str(dt.day)+".json";

def logError(url, error):
    with open("error_chicago.log", "a") as myfile:
        myfile.write(url)
        # myfile.write(" "+error)
        myfile.write("\n")

# https://api.weather.com/v1/location/KMDW:9:US/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&startDate=20040501&endDate=20040531
while dt < end:
    url = "https://api.weather.com/v1/location/KMDW:9:US/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=m&startDate=" + \
        str(dt.year)+padDate(str(dt.month))+padDate(str(dt.day))
    print(url)
    dt += step
    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            with open(getFileName(dt), 'w') as fp:
                json.dump(data, fp)
    except RuntimeError as error:
        print(error)
        logError(url, error)
        continue
    except urllib.error.HTTPError as error:
        print(error)
        logError(url, error)
        continue
    except Exception as error:
        print(error)
        logError(url, error)
        continue
    clear()