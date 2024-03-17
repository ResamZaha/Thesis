SELECT 
    "Unnamed: 0",
    "expire_time_gmt",
    "valid_time_gmt",
    "temp",
    "wspd",
    "wx_phrase",
    "valid_date_time",
    "expire_date_time",
    "max_temp" - "min_temp" AS temperature_difference,
    CASE 
        WHEN "wspd" > 20 THEN 'High wind'
        ELSE 'Low wind'
    END AS wind_speed_category
FROM 
    chicago_weather;