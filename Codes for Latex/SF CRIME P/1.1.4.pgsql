SELECT 
    "IncidntNum",
    "location",
    "Time",
    "Resolution",
    "X",
    "Y",
    CASE
        WHEN "location" LIKE '%STREET%' THEN 'Street'
        WHEN "location" LIKE '%AVENUE%' THEN 'Avenue'
        ELSE 'Other'
    END AS location_type
FROM 
    sf_crimedata;