SELECT 
    SUM("wspd") AS Total_Wind_Speed,
    SUM(CASE WHEN "temp" < 0 THEN "wspd" ELSE 0 END) AS Sum_Wind_Speed_Below_Zero
FROM 
    chicago_weather;