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