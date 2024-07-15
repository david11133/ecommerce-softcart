SELECT 
    dd."Year",
    dc.country,
    ROUND(AVG(amount), 1) AS average_sales
FROM 
    "FactSales" fs
JOIN "DimDate" dd ON fs.dateid = dd.dateid
JOIN "DimCountry" dc ON fs.countryid = dc.countryid
GROUP BY
    dd."Year",
    dc.country
ORDER BY 
    dd."Year",
    dc.country