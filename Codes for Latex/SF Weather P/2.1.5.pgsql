SELECT 
    "Unnamed: 0",
    "valid_time_gmt",
    "max_temp" + "min_temp" AS combined_temperature,
    "vis" / 2 AS half_visibility,
    CASE
        WHEN "max_temp" > 75 AND "min_temp" < 50 THEN 'Wide Temperature Range'
        WHEN "vis" < 5 THEN 'Foggy'
        ELSE 'Clear'
    END AS weather_prediction,
    "wx_phrase",
    "valid_date_time"
FROM 
    sf_weather;