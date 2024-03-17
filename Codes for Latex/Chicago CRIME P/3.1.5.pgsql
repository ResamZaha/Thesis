SELECT 
    "ID",
    "Community Area",
    CASE
        WHEN "Community Area" < 10 THEN 'Single digit area'
        WHEN "Community Area" BETWEEN 10 AND 99 THEN 'Double digit area'
        ELSE 'Triple digit area or unknown'
    END AS "AreaSize",
    "Arrest" AS "WasThereAnArrest"
FROM 
    chicago_crime;