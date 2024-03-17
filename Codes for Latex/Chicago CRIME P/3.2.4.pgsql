SELECT 
    MAX("Year") AS max_year,
    MAX("X Coordinate") AS max_x_coordinate,
    MAX("Y Coordinate") AS max_y_coordinate,
    MAX("Date") AS latest_crime_date
FROM 
    chicago_crime;