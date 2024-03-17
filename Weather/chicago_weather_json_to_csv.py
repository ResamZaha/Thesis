import datetime
import json
import pandas as pd

dt = datetime.datetime(2004, 1, 1)
end = datetime.datetime(2023, 1, 1)

step = datetime.timedelta(days=1)


def padDate(dtx):
    if(len(dtx) < 2):
        dtx = "0"+dtx
    return dtx


def getFileName(dt):
    return "data_chicago/weather_data_"+str(dt.year)+"_"+str(dt.month)+"_"+str(dt.day)+".json"


def processDate(dt):
    step_temp = datetime.timedelta(hours=1)
    if(dt.minute > 30):
        dt += step_temp
    dt = dt.replace(minute=0)
    return dt


alldata = []
idx = 0
prev = None 
while dt < end:
    filename = getFileName(dt)
    try:
        f = open(filename)
        data = json.load(f)
        print(filename)
    except FileNotFoundError as error:
        data = prev
    
    prev = data
    for i in data['observations']:
        i_date_time_expire = processDate(
            datetime.datetime.fromtimestamp(i["expire_time_gmt"]))
        i_date_time_valid = processDate(
            datetime.datetime.fromtimestamp(i["valid_time_gmt"]))
        tempobj = {
            "expire_time_gmt": i["expire_time_gmt"],
            "valid_time_gmt": i["valid_time_gmt"],
            "temp": i["temp"],
            "wx_phrase": i["wx_phrase"],
            "heat_index": i["heat_index"],
            "rh": i["rh"],
            "pressure": i["pressure"],
            "vis": i["vis"],
            "wc": i["wc"],
            "wdir": i["wdir"],
            "wspd": i["wspd"],
            "max_temp": i["max_temp"],
            "min_temp": i["min_temp"],
            "expire_date_time": i_date_time_expire.strftime("%d/%m/%Y %H:%M:%S"),
            "valid_date_time": i_date_time_valid.strftime("%d/%m/%Y %H:%M:%S"),
        }
        alldata.append(tempobj)
    dt += step

pd.DataFrame(alldata).to_csv("../dataset/weather_data_chicago_2004_2023.csv")
