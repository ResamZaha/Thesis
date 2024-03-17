SELECT 
    "IncidntNum",
    "Incident Code",
    "X" - "Y" AS coordinate_difference,
    CASE 
        WHEN "Incident Code" > 20000 THEN 'High Code'
        ELSE 'Low Code'
    END AS code_level
FROM 
    sf_crimedata;