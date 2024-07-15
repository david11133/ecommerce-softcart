SELECT
    dd."Year",
    dc.country,
    SUM(fs.amount) AS totalsales 
FROM 
    "FactSales" fs
JOIN "DimDate" dd on fs.dateid = dd.dateid
JOIN "DimCountry" dc on fs.countryid = dc.countryid 
GROUP BY
    dd."Year", dc.country
ORDER BY 
    dd."Year"