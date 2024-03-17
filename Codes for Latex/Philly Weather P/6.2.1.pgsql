SELECT 
    COUNT(*) AS Total_Observations,
    COUNT(CASE WHEN heat_index > 90 THEN 1 END) AS High_Heat_Index_Count,
    COUNT(CASE WHEN rh >= 80 THEN 1 END) AS High_Humidity_Count,
    COUNT(CASE WHEN vis < 2 THEN 1 END) AS Low_Visibility_Count,
    COUNT(CASE WHEN pressure > 1020 THEN 1 END) AS High_Pressure_Count,
    COUNT(CASE WHEN wc < -20 THEN 1 END) AS Extreme_Wind_Chill_Count
FROM 
    philly_weather;