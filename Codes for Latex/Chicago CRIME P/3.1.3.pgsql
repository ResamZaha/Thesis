SELECT 
    "ID",
    CASE 
        WHEN "X Coordinate" > "Y Coordinate" THEN 'X greater'
        ELSE 'Y greater or equal'
    END AS "CoordinateComparison",
    CASE 
        WHEN "Beat" = "District" THEN 'Beat equals District'
        ELSE 'Beat not equal to District'
    END AS "BeatDistrictEquality",
    ("Latitude" > "Longitude") AS "LatGreaterThanLong"
FROM 
    chicago_crime;