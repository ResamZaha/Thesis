SELECT 
    MAX("dispatch_date_time") AS earliest_crime_date,
    MAX("lat") AS min_latitude,
    MAX("lng") AS min_longitude
FROM 
    philly_crime;