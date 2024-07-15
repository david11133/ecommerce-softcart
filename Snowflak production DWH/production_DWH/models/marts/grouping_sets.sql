SELECT 
  co.country, 
  ca.category, 
  SUM(s.amount) AS totalsales 
FROM 
  public."FactSales" s 
  JOIN "DimCountry" co ON s.countryid = co.countryid 
  JOIN "DimCategory" ca ON s.categoryid = ca.categoryid
GROUP BY
  co.country, ca.category
ORDER BY
  SUM(s.amount)