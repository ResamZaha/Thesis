SELECT 
    "objectid",
    "dc_dist" + "hour" AS "DistrictPlushour",
    "point_x" - "point_y" AS "CoordinateDifference",
    "lat" * "lng" AS "longitudeTimeslatitude",
    ("lat" - "lng") AS "LatMinusLong",
    CASE 
        WHEN "text_general_code" = 'Thefts' THEN 1 
        ELSE 0 
    END AS "IsTheft"
FROM 
    philly_crime
WHERE 
    "dc_dist" BETWEEN 10 AND 20;