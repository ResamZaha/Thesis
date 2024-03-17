SELECT 
    "Unnamed: 0",
    "expire_date_time",
    "expire_time_gmt",
    "valid_date_time",
    "valid_time_gmt",
    "vis",
    "wx_phrase",
        CASE 
        WHEN "wdir" BETWEEN 0 AND 180 THEN 'Easterly Wind'
        ELSE 'Westerly Wind'
    END AS wind_direction,
    "temp",
    CASE 
        WHEN "temp" < 0 THEN 'Below freezing'
        ELSE 'Above freezing'
    END AS temperature_status
FROM 
    philly_weather;