SELECT 
    COUNT(*) AS Total_Observations,
    SUM(CASE WHEN heat_index > 90 THEN heat_index ELSE 0 END) AS Total_Heat_Index_Over_90,
    SUM(CASE WHEN rh >= 80 THEN rh ELSE 0 END) AS Total_High_Humidity,
    SUM(CASE WHEN vis < 2 THEN 1 ELSE 0 END) AS Total_Low_Visibility_Events,
    SUM(CASE WHEN pressure > 1020 THEN pressure ELSE 0 END) AS Total_High_Pressure,
    SUM(CASE WHEN wc < -20 THEN 1 ELSE 0 END) AS Total_Extreme_Wind_Chill_Events
FROM 
    philly_weather;