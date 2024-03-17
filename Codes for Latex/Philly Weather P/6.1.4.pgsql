SELECT 
    "Unnamed: 0",
    "valid_time_gmt",
    "wdir" + 180 AS opposite_wdir,
    "wc" - 5 AS reduced_wind_chill,
    "temp" * "wspd" AS wind_temperature_factor,
    ("temp" + "wspd") / 2 AS comfort_index,
    CASE
        WHEN "temp" > 85 THEN 'Too Hot'
        WHEN "temp" < 32 THEN 'Too Cold'
        ELSE 'Comfortable'
    END AS comfort_status,
    CASE
        WHEN "wc" < 0 THEN 'Extreme Cold'
        WHEN "wc" BETWEEN 0 AND 32 THEN 'Chilly'
        ELSE 'Not Chilly'
    END AS wind_chill_status,
    "wx_phrase",
    "valid_date_time"
FROM 
    philly_weather;