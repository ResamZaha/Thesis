SELECT 
    MIN("dispatch_date_time") AS earliest_crime_date,
    MIN("point_x") AS min_point_x,
    MIN("point_y") AS min_point_y,
    MIN("lat") AS min_latitude,
    MIN("lng") AS min_longitude
FROM 
    philly_crime;