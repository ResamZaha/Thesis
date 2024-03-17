SELECT 
    "text_general_code",
    "location_block",
    "dispatch_date",
    "dispatch_time"
FROM 
    philly_crime
WHERE 
    "dc_dist" < 25
ORDER BY 
    "dispatch_date" DESC;