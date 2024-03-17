SELECT 
    "objectid",
    "psa",
    CASE 
        WHEN "point_x" > "point_y" THEN 'X greater'
        ELSE 'Y greater or equal'
    END AS "CoordinateComparison",
    CASE 
        WHEN "ucr_general" = "dc_key" THEN 'Beat greater District'
        ELSE 'Beat less than District'
    END AS "UCR_KEYrelation",
    ("lat" > "lng") AS "LatGreaterThanLong"
FROM 
    philly_crime;