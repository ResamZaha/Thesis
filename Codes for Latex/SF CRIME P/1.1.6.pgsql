SELECT 
    "IncidntNum",
    "Address",
    "X",
    "Y",
    "PdDistrict",
    "Resolution",
    CASE 
        WHEN "Y" > 37.7749 THEN 'Northern' 
        ELSE 'Southern' 
    END AS city_region,
    "Date"
FROM 
    sf_crimedata;