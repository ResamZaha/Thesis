SELECT 
    "Primary Type",
    "Description",
    "Date",
    "Arrest"
FROM 
    chicago_crime
WHERE 
    "Domestic" = true AND "Community Area" < 10
ORDER BY 
    "Date" DESC;