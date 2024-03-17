SELECT 
    "Unnamed: 0",
    "valid_time_gmt",
    "max_temp" - "min_temp" AS temp_range,
    "wspd" + 10 AS adjusted_wspd,
    CASE
        WHEN "wspd" > 20 THEN 'Windy'
        WHEN "temp" < 32 THEN 'Freezing'
        ELSE 'Mild'
    END AS weather_condition,
    "wx_phrase",
    "valid_date_time"
FROM 
    sf_weather;