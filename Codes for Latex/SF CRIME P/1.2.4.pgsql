SELECT "Category", MIN("Date") AS EarliestDate
FROM sf_crimedata
GROUP BY "Category";