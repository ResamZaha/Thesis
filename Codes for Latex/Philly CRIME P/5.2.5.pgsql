SELECT 
    "dc_dist",
    AVG("point_x") AS Avg_Point_X,
    AVG("point_y") AS Avg_Point_Y,
    AVG("lat") AS Avg_Latitude,
    AVG("lng") AS Avg_Longitude
FROM 
    philly_crime
GROUP BY 
    "dc_dist"
ORDER BY 
    "dc_dist";