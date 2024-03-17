SELECT 
    "objectid",
    "lat",
    "lng",
    "psa",
    "dispatch_date_time",
    "dc_key",
    CASE
        WHEN "lat" BETWEEN 41.6 AND 42 THEN 'Northern philadelphia'
        ELSE 'Other'
    END AS "Region",
    ("lat" < 41.6) AS "IsSouthOfNorthernPhiladelphia"
FROM 
    philly_crime;