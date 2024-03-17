SELECT 
    SUM(CASE WHEN "text_general_code" = 'Homicide - Criminal' THEN 1 ELSE 0 END) AS homicide_count,
    SUM(CASE WHEN "text_general_code" = 'All Other Offenses' THEN 1 ELSE 0 END) AS other_count,
    SUM(CASE WHEN "text_general_code" = 'Weapon Violations' THEN 1 ELSE 0 END) AS weapon_related_count,
    SUM(CASE WHEN "text_general_code" = 'Public Drunkenness' THEN 1 ELSE 0 END) AS drunkness_related_count,
    SUM(CASE WHEN "text_general_code" = 'VANDALISM' THEN 1 ELSE 0 END) AS criminal_damage_count
FROM 
    philly_crime;