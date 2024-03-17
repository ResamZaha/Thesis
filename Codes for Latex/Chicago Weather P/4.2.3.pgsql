SELECT 
    MIN("wspd") AS Min_Wind_Speed,
    MIN("vis") AS Min_Visibility
FROM 
    chicago_weather;