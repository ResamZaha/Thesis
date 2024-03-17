SELECT 
    "Unnamed: 0",
    "valid_time_gmt",
    "temp",
    "wc",
    "wspd",
    "temp" - "wc" AS wind_chill_gap,
    CASE
        WHEN "wc" < "temp" THEN 'Wind Chill Lower'
        ELSE 'Temperature Lower or Equal'
    END AS temperature_comparison,
    CASE
        WHEN "wspd" > 25 THEN 'High Wind Speed'
        ELSE 'Normal Wind Speed'
    END AS wind_speed_status,
    "wx_phrase",
    "valid_date_time"
FROM 
    sf_weather;