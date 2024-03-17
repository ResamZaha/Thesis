SELECT 
    "IncidntNum",
    "Category",
    "Descript",
    "DayOfWeek",
    "PdDistrict",
    "Current Police Districts 2 2" > "Current Supervisor Districts 2 2" AS police_greater_than_supervisor,
    "Neighborhoods 2" = 94 AS in_neighborhood_94,
    ("DELETE - Police Districts 2 2" = "DELETE - Supervisor Districts 2 2") AS delete_fields_equal
FROM 
    sf_crimedata;