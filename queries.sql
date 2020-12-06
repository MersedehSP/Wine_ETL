--search by wine name
SELECT wine_name, price, varietal 
FROM wine
WHERE wine_name LIKE ('%pino%') ;

--search by price 

SELECT wine_name, price, varietal 
FROM wine
WHERE price <= 10 AND price > 8 AND varietal = 'Malbec';

---search for malbecs less that 10$
SELECT w.wine_name, w.price, w.description, w.varietal, m.merchant_name
FROM wine AS w
INNER JOIN merchant_wine AS m ON w.wine_id = m.wine_id
WHERE price <= 10 AND varietal = 'Malbec';

---serach for all the info of wine less than 10$
SELECT w.wine_name, w.price, w.description, w.varietal, m.merchant_name, r.country, r.state, r.region
FROM wine AS w
INNER JOIN merchant_wine AS m ON w.wine_id = m.wine_id
INNER JOIN region AS r ON w.region_id = r.region_id
WHERE price <= 10;


SELECT w.wine_name, w.price, w.description, w.varietal, m.merchant_name, r.country, r.state, r.region, a.merchant_address
FROM wine AS w
INNER JOIN merchant_wine AS m ON w.wine_id = m.wine_id
INNER JOIN region AS r ON w.region_id = r.region_id
INNER JOIN merchant AS a ON m.merchant_name = a.merchant_name
WHERE price <= 10;




