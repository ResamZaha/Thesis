SELECT 
    "ID",
    "Location Description",
    CASE
        WHEN "Location Description" ILIKE '%SCHOOL%' THEN 'School-related'
        WHEN "Location Description" ILIKE '%RESIDENCE%' THEN 'Residential'
        ELSE 'Other'
    END AS "LocationType",
    ("Location Description" ILIKE '%STREET%') AS "IsOnStreet"
FROM 
    chicago_crime;