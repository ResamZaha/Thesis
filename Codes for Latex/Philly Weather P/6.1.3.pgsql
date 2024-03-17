SELECT 
    "Unnamed: 0",
    "valid_time_gmt",
    "temp" - "wc" AS realfeel_difference,
    "vis",
    CASE
        WHEN "vis" < 5 THEN 'Low Visibility'
        WHEN "vis" BETWEEN 5 AND 15 THEN 'Moderate Visibility'
        ELSE 'High Visibility'
    END AS visibility_status,
    CASE
        WHEN "temp" - "wc" > 20 THEN 'Significant Wind Chill Effect'
        ELSE 'Negligible Wind Chill Effect'
    END AS wind_chill_effect,
    "wx_phrase",
    "valid_date_time"
FROM 
    philly_weather;