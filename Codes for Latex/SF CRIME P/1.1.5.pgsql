SELECT 
    "IncidntNum",
    "Incident Code",
    ("X" > "Y") AS is_x_greater_than_y,
    "Date",
    "Time",
    ("Incident Code" BETWEEN 20000 AND 30000) AS is_code_in_range,
    ("location" ILIKE '%STREET%') AS is_on_street
FROM 
    sf_crimedata;