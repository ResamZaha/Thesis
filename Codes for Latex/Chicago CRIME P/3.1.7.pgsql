SELECT 
    "ID",
    "Latitude",
    "Longitude",
    CASE
        WHEN "Latitude" BETWEEN 41.6 AND 42 THEN 'Northern Chicago'
        ELSE 'Other'
    END AS "Region",
    ("Latitude" < 41.6) AS "IsSouthOfNorthernChicago"
FROM 
    chicago_crime;