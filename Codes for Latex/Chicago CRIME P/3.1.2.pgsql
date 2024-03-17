SELECT 
    "ID",
    "Beat" + "District" AS "BeatPlusDistrict",
    "X Coordinate" - "Y Coordinate" AS "CoordinateDifference",
    "Community Area" * "Beat" AS "AreaTimesBeat",
    "Beat" / NULLIF("Community Area", 0) AS "BeatPerArea",  -- Avoid division by zero
    "District" - "Ward" AS "DistrictMinusWard"
FROM 
    chicago_crime;