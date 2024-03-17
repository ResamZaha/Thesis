SELECT 
    "District",
    AVG("Year") AS Average_Year,
    AVG("X Coordinate") AS Avg_X_Coordinate,
    AVG("Y Coordinate") AS Avg_Y_Coordinate,
    AVG("Latitude") AS Avg_Latitude,
    AVG("Longitude") AS Avg_Longitude
FROM 
    chicago_crime
GROUP BY 
    "District"
ORDER BY 
    "District";