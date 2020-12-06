#Here are some additional queries that a user
# in the database might find useful to make a wine choice

--TOP 10 Wine Producing Countries
CREATE VIEW "Top 10 Wine Producing Countries" AS
SELECT COUNT(country) AS "Country Count", country
FROM region
GROUP BY country
ORDER BY "Country Count" DESC LIMIT 10;

SELECT * FROM "Top 10 Wine Producing Countries";

--AVG Varietal Price/Frequency
CREATE VIEW "Varietal Price/Frequency" AS
SELECT ROUND(AVG(price),2) AS "AVG Price for a bottle",
varietal, COUNT(varietal) AS "Varietal Count"
FROM wine
GROUP BY varietal
;
SELECT * FROM "Varietal Price/Frequency";

--5 AVG Most Expansive bottle throughout all stores
CREATE VIEW "Most Expansive Bottle" AS
SELECT wine_name, ROUND(AVG(price),2) AS "AVG Wine Price"
FROM wine
GROUP BY wine_name
ORDER BY "AVG Wine Price" DESC
LIMIT 5;

SELECT * FROM "Most Expansive Bottle";

--Wine budget = $15
CREATE VIEW "$15 Budget Wine" AS
SELECT wine.wine_name AS "Wine Name", wine.price, region.country, merchant_wine.merchant_name,
merchant.merchant_address
FROM wine
INNER JOIN region ON wine.region_id = region.region_id
INNER JOIN merchant_wine ON wine.wine_id = merchant_wine.wine_id
INNER JOIN merchant ON merchant_wine.merchant_name = merchant.merchant_name
WHERE price < 15
ORDER BY "price" DESC
LIMIT 50;

SELECT * FROM "$15 Budget Wine";

--AVG Wine Price per store & Total Wine bottle data/rows
CREATE VIEW "AVG Wine Price Per Store" AS
SELECT merchant_name, COUNT(merchant_name) AS "Merchant Count", ROUND(AVG(price),2)
FROM merchant_wine
INNER JOIN wine ON wine.wine_id = merchant_wine.wine_id
GROUP BY merchant_name
ORDER BY "Merchant Count" DESC;

SELECT * FROM "AVG Wine Price Per Store";

-- AVG Wine Count by country and avg price of bottle per country
CREATE VIEW "AVG Wine Price by Country" AS
SELECT country AS "Country", COUNT(country) AS "Country Count", ROUND(AVG(price),2) AS "AVG Price"
FROM region
INNER JOIN wine ON wine.region_id = region.region_id
GROUP BY Country
ORDER BY "Country Count" DESC;

SELECT * FROM "AVG Wine Price by Country";