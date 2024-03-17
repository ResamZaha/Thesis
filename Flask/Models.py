class CrimeModel:
    def __init__(self, day=-1,month=-1,year=-1,
                 hour=-1,minute=-1, primary_type="", 
                 description="", arrest=False,
                 district=-1, x_coordinate=-1, y_coordinate=-1):
        
        # self.id = int(id)
        # self.case_number = str(case_number)
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.hour = int(hour)
        self.minute = int(minute)
        # self.iucr = str(iucr)
        self.primary_type = primary_type
        self.description = description
        # self.location_description = location_description
        self.arrest = bool(arrest)
        self.district = int(district)
        self.x_coordinate = float(x_coordinate)
        self.y_coordinate = float(y_coordinate)
        self.year = int(year)

class WeatherModel:
    def __init__(self, expire_time_gmt, valid_time_gmt, temp, wx_phrase, heat_index, rh, pressure, vis, wc, wdir, wspd, max_temp, min_temp):
        self.expire_time_gmt = int(expire_time_gmt)
        self.valid_time_gmt = int(valid_time_gmt)
        self.temp = float(temp)
        self.wx_phrase = str(wx_phrase)
        self.heat_index = float(heat_index)
        self.rh = int(rh)
        self.pressure = float(pressure)
        self.vis = float(vis)
        self.wc = float(wc)
        self.wdir = int(wdir)
        self.wspd = int(wspd)
        self.max_temp = float(max_temp)
        self.min_temp = float(min_temp)