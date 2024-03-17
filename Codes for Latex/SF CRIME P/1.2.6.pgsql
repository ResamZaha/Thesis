SELECT "PdDistrict", AVG("Y") AS AvgLatitude
FROM sf_crimedata
GROUP BY "PdDistrict";