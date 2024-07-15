SELECT 
  dc.country, 
  SUM(fs.amount) AS totalsales 
FROM 
  "FactSales" fs 
  JOIN "DimCountry" dc ON fs.countryid = dc.countryid 
GROUP BY 
  dc.country