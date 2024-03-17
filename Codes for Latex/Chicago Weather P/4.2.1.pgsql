SELECT 
    COUNT(*) AS Total_Observations,
    COUNT(CASE WHEN wx_phrase = 'Mostly Cloudy' THEN 1 END) AS Mostly_Cloudy_Count,
    COUNT(CASE WHEN temp < 0 THEN 1 END) AS Below_Zero_Count,
    COUNT(CASE WHEN wspd >= 10 THEN 1 END) AS Windy_Conditions_Count,
    COUNT(CASE WHEN vis > 10 THEN 1 END) AS Good_Visibility_Count
FROM 
    chicago_weather;