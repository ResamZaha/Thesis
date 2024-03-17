SELECT 
    SUM(CASE WHEN "Primary Type" = 'THEFT' THEN 1 ELSE 0 END) AS theft_count,
    SUM(CASE WHEN "Primary Type" = 'ROBBERY' THEN 1 ELSE 0 END) AS robbery_count,
    SUM(CASE WHEN "Primary Type" = 'ASSAULT' THEN 1 ELSE 0 END) AS assault_count,
    SUM(CASE WHEN "Primary Type" = 'BATTERY' THEN 1 ELSE 0 END) AS battery_count,
    SUM(CASE WHEN "Primary Type" = 'CRIMINAL DAMAGE' THEN 1 ELSE 0 END) AS criminal_damage_count
FROM 
    chicago_crime;