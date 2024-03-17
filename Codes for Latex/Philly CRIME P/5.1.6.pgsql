SELECT 
    "objectid",
    "location_block",
    CASE
        WHEN "text_general_code" ILIKE '%Homicide%' THEN 'Homicide-related'
        WHEN "text_general_code" ILIKE '%Weapon%' THEN 'Weapon-related'
        WHEN "text_general_code" ILIKE '%drunkness%' THEN 'drunkness-related'
        ELSE 'Other'
    END AS "Type",
    ("text_general_code" ILIKE '%thefts%') AS "IsTheft",
    "dispatch_date_time"
FROM 
    philly_crime;