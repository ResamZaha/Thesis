SELECT 
    "objectid",
    "location_block",
    CASE
        WHEN "dc_dist" < 10 THEN 'Single digit area'
        WHEN "dc_dist" BETWEEN 10 AND 99 THEN 'Double digit area'
        ELSE 'Triple digit area or unknown'
    END AS "DistSize",
    "dispatch_date_time"
FROM 
    philly_crime;