SELECT 
    MAX(temp) AS Max_Temperature,
    MAX(CASE WHEN wspd >= 10 THEN wspd ELSE NULL END) AS Max_Wind_Speed_Over_10,
    MAX(CASE WHEN heat_index > 90 THEN heat_index ELSE NULL END) AS Max_Heat_Index_Over_90,
    MAX(CASE WHEN rh >= 80 THEN rh ELSE NULL END) AS Max_Relative_Humidity_Over_80,
    MAX(CASE WHEN vis < 2 THEN vis ELSE NULL END) AS Max_Visibility_Under_2,
    MAX(CASE WHEN pressure > 1020 THEN pressure ELSE NULL END) AS Max_Pressure_Over_1020,
    MAX(wc) AS Max_Wind_Chill
FROM 
    philly_weather;