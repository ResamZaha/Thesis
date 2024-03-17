SELECT "PdDistrict",
    SUM("Incident Code") AS TotalValue
FROM sf_crimedata
GROUP BY "PdDistrict";