SELECT 
    "dc_key",
    "ucr_general" + "dc_dist" AS "ucrGenralPlusDistrict",
    "point_x" - "point_y" AS "CoordinateDifference",
    "hour" * "dc_key" AS "hourTimesDcKey",
    "dc_dist" - "hour" AS "DistrictMinushour"
FROM 
    philly_crime;