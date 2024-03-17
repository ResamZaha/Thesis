SELECT 
    "ID",
    "District" + "Ward" AS "DistrictPlusWard",
    "X Coordinate" - "Y Coordinate" AS "CoordinateDifference",
    "Arrest"::int AS "ArrestFlag",
    "Community Area" * "Beat" AS "AreaTimesBeat",
    ("Latitude"::numeric - "Longitude"::numeric) AS "LatMinusLong",
    "Year" % 10 AS "YearLastDigit",
    CASE 
        WHEN "Primary Type" = 'ASSAULT' THEN 1 
        ELSE 0 
    END AS "IsAssault"
FROM 
    chicago_crime
WHERE 
    "District" BETWEEN 10 AND 20
ORDER BY 
    "ID";