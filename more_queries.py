#Here are some additional queries that a user
# in the database might find useful to make a wine choice

--TOP 10 Wine Producing Countries
CREATE VIEW "Top 10 Wine Producing Countries" AS
SELECT COUNT(country) AS "Country Count", country
FROM region
GROUP BY country
ORDER BY "Country Count" DESC LIMIT 10;

SELECT * FROM "Top 10 Wine Producing Countries";