SELECT "Descript", MAX("Date") AS LatestDate
FROM sf_crimedata
GROUP BY "Descript";