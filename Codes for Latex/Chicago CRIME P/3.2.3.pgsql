SELECT 
    MIN("Year") AS min_year,
    MIN("X Coordinate") AS min_x_coordinate,
    MIN("Y Coordinate") AS min_y_coordinate,
    MIN("Date") AS earliest_crime_date,
    MIN("Latitude") AS min_latitude,
    MIN("Longitude") AS min_longitude
FROM 
    chicago_crime;