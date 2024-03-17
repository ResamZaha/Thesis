from flask import Flask, json, jsonify, request, session
from flask_cors import CORS

import time
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from Models import CrimeModel, WeatherModel
'''
Should move db code to other file
'''
app = Flask(__name__)
CORS(app)

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db = client.test


def currentTime():
    return time.time()


def findChicagoCrime(crime):
    return db.crime.chicago.find_one({"id": crime.id})


def hasChicagoCrime(crime):
    return findChicagoCrime(crime) is not None


def addChicagoCrime(crime):
    return (db.crime.chicago.insert_one(crime.__dict__))


def findSFCrime(crime):
    return db.crime.sf.find_one({"id": crime.id})


def hasSFCrime(crime):
    return findChicagoCrime(crime) is not None


def addSFCrime(crime):
    return (db.crime.sf.insert_one(crime.__dict__))


def findChicagoWeather(weather):
    return db.weather.chicago.find_one({"id": weather.id})


def hasChicagoWeather(weather):
    return findChicagoWeather(weather) is not None


def addChicagoWeather(weather):
    return (db.weather.chicago.insert_one(weather.__dict__))


def findSFWeather(weather):
    return db.weather.sf.find_one({"id": weather.id})


def hasSFWeathet(weather):
    return findChicagoWeather(weather) is not None


def addSFWeather(weather):
    return (db.weather.sf.insert_one(weather.__dict__))


@app.route("/query/aggregate/", methods=['GET'])
def queryAggregate():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/aggregate/crime", methods=['GET'])
def queryAggregateCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/aggregate/chicago/crime", methods=['GET'])
def queryAggregateChicagoCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.chicago.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/aggregate/sf/crime", methods=['GET'])
def queryAggregateSFCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.sf.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/find/chicago/crime", methods=['GET'])
def queryChicagoCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.chicago.find(result)
    res = []
    for x in data:
        x.pop('_id')
        res.append(x)
    return jsonify(res)


@app.route("/query/find/SF/crime", methods=['GET'])
def querySFCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.sf.find(result)
    res = []
    for x in data:
        x.pop('_id')
        res.append(x)
    return jsonify(res)


@app.route("/query/unique/chicago/crime", methods=['GET'])
def queryUniqueChicagoCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.chicago.distinct(result['field'])
    return jsonify(data)


@app.route("/query/unique/SF/crime", methods=['GET'])
def queryUniqueSFCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.crime.sf.distinct(result['field'])
    return jsonify(data)


@app.route("/add/crime", methods=['POST'])
def addCrime():
    result = (json.loads(request.get_data(parse_form_data=True)))

    chicago_crime = bool(result['chicago_crime'])
    # id = int(result['id'])
    # case_number = result['case_number']
    day = result['day']
    month = result['month']
    year = result['year']
    hour = result['hour']
    minute = result['minute']

    # iucr = str(result['iucr'])
    primary_type = result['primary_type']
    description = result['description']
    # location_description = result['location_description']
    arrest = bool(result['arrest'])
    district = int(result['district'])
    x_coordinate = float(result['x_coordinate'])
    y_coordinate = float(result['y_coordinate'])

    if (chicago_crime == True):
        crime = CrimeModel(day, month, year, hour, minute, primary_type,
                           description, arrest, district, x_coordinate, y_coordinate)
        if (hasChicagoCrime(crime) == False):
            addChicagoCrime(crime)
            return jsonify(True)
        else:
            return jsonify(False)
    else:
        crime = CrimeModel(day, month, year, hour, minute, primary_type,
                           description, arrest, district, x_coordinate, y_coordinate)
        if (hasSFCrime(crime) == False):
            addSFCrime(crime)
            return jsonify(True)
        else:
            return jsonify(False)


@app.route("/query/aggregate/weather", methods=['GET'])
def queryAggregateWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/aggregate/chicago/weather", methods=['GET'])
def queryAggregateChicagoWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.chicago.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/aggregate/sf/weather", methods=['GET'])
def queryAggregateSFWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.sf.aggregate(result)
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        res.append(x)

    return jsonify(res)


@app.route("/query/find/chicago/weather", methods=['GET'])
def queryChicagoWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.chicago.find(result)
    res = []
    for x in data:
        x.pop('_id')
        res.append(x)
    return jsonify(res)


@app.route("/query/find/sf/weather", methods=['GET'])
def querySFWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.sf.find(result)
    res = []
    for x in data:
        x.pop('_id')
        res.append(x)
    return jsonify(res)


@app.route("/query/unique/chicago/weather", methods=['GET'])
def queryUniqueChicagoWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.chicago.distinct(result['field'])
    return jsonify(data)


@app.route("/query/unique/sf/weather", methods=['GET'])
def queryUniqueSFWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))
    print("check", result)
    data = db.weather.sf.distinct(result['field'])
    return jsonify(data)


@app.route("/add/weather", methods=['POST'])
def addWeather():
    result = (json.loads(request.get_data(parse_form_data=True)))

    chicago_weather = bool(result['chicago_weather'])
    expire_time_gmt = int(result['expire_time_gmt'])
    valid_time_gmt = int(result['valid_time_gmt'])
    temp = float(result['temp'])
    wx_phrase = str(result['wx_phrase'])
    heat_index = float(result['heat_index'])
    rh = int(result['rh'])
    pressure = float(result['pressure'])
    vis = float(result['vis'])
    wc = float(result['wc'])
    wdir = int(result['wdir'])
    wspd = int(result['wspd'])
    max_temp = float(result['max_temp'])
    min_temp = float(result['min_temp'])

    if (chicago_weather == True):
        weather = WeatherModel(expire_time_gmt, valid_time_gmt, temp, wx_phrase,
                               heat_index, rh, pressure, vis, wc, wdir, wspd, max_temp, min_temp)
        if (hasChicagoWeather(weather) == False):
            addChicagoCrime(weather)
            return jsonify(True)
        else:
            return jsonify(False)
    else:
        weather = WeatherModel(expire_time_gmt, valid_time_gmt, temp, wx_phrase,
                               heat_index, rh, pressure, vis, wc, wdir, wspd, max_temp, min_temp)
        if (hasSFCrime(weather) == False):
            addSFCrime(weather)
            return jsonify(True)
        else:
            return jsonify(False)

@app.route("/", methods=['GET'])
def index():
    return "Welcome to Data warehouse System"


"""if __name__ == '__main__':
    app.run(debug=True)"""


# # # Combined

@app.route("/test", methods=['GET'])
def test_route():
    return jsonify({"message": "Test route is working!"})





@app.route("/query/sf/crime-weather", methods=['GET'])
def querySFCrimeWeather():
    pipeline = json.loads(request.get_data(parse_form_data=True))
    print("received pipeline:", pipeline)
    # Adding a $lookup stage to the pipeline for joining with SF weather data
    pipeline.append({
        "$lookup": {
            "from": "crime.sf",  # Replace with your SF weather collection name
            "localField": "Incident Date",  # Common field in SF crime data
            "foreignField": "valid_date_time",  # Common field in SF weather data
            "as": "weather_info"
        }
    })
    pipeline.append({
        "$unwind": {
            "path": "$weather_info",
            "preserveNullAndEmptyArrays": False  # Adjust based on your data
        }
    })

    # Execute the modified pipeline
    data = db.crime.sf.aggregate(pipeline)  # Replace 'sf_crime' with your SF crime collection name

    # Process and return the results
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        if 'weather_info' in x:
            x['weather_info'] = {k: v for k, v in x['weather_info'].items() if k != '_id'}
        res.append(x)

    return jsonify(res)
    
    
@app.route("/query/chicago/crime-weather", methods=['GET'])
def queryChicagoCrimeWeather():
    pipeline = json.loads(request.get_data(parse_form_data=True))
    print("received pipeline:", pipeline)

    # Adding a $lookup stage to the pipeline for joining with Chicago weather data
    pipeline.append({
        "$lookup": {
            "from": "weather.chicago",  # Chicago weather collection
            "localField": "Date",  # Common field in Chicago crime data
            "foreignField": "valid_date_time",  # Common field in Chicago weather data
            "as": "weather_info"
        }
    })
    pipeline.append({
        "$unwind": {
            "path": "$weather_info",
            "preserveNullAndEmptyArrays": True
        }
    })

    # Execute the modified pipeline
    data = db.crime.chicago.aggregate(pipeline)  # Replace 'chicago_crime' with your Chicago crime collection name

    # Process and return the results
    res = []
    for x in data:
        x['_id'] = str(x['_id'])
        if 'weather_info' in x:
            x['weather_info'] = {k: v for k, v in x['weather_info'].items() if k != '_id'}
        res.append(x)

    return jsonify(res)

"""@app.route("/query/weather/chicago-sf", methods=['GET'])
def queryChicagoSfWeather():
    pipeline = json.loads(request.get_data(parse_form_data=True))

    # Query Chicago weather data
    chicago_weather_data = db.weatherchicago.kom.aggregate(pipeline)

    # Query San Francisco weather data
    sf_weather_data = db.weathersf.kom.aggregate(pipeline)

    # Rename columns and combine the results
    renamed_chicago_weather_data = [
        {"{}_chicago".format(key): value for key, value in record.items()} for record in chicago_weather_data
    ]
    renamed_sf_weather_data = [
        {"{}_sf".format(key): value for key, value in record.items()} for record in sf_weather_data
    ]

    combined_weather_data = renamed_chicago_weather_data + renamed_sf_weather_data

    # Convert ObjectIds to string
    res = []
    for record in combined_weather_data:
        record['_id'] = str(record.get('_id', ''))
        res.append(record)

    return jsonify(res)"""

@app.route("/query/weather/chicago-sf", methods=['GET'])
def queryChicagoSfWeather():
    pipeline = json.loads(request.get_data(parse_form_data=True))

    # Query and aggregate Chicago weather data
    chicago_weather_data = list(db.weatherchicago.kom.aggregate(pipeline))
    # Query and aggregate San Francisco weather data
    sf_weather_data = list(db.weathersf.kom.aggregate(pipeline))

    # Combine the data
    combined_weather_data = {data['_id']: {'chicago_temp': data['avg_temp']} for data in chicago_weather_data}
    for data in sf_weather_data:
        if data['_id'] in combined_weather_data:
            combined_weather_data[data['_id']]['sf_temp'] = data['avg_temp']
        else:
            combined_weather_data[data['_id']] = {'sf_temp': data['avg_temp']}

    return jsonify(combined_weather_data)


if __name__ == '__main__':
    app.run(debug=True)