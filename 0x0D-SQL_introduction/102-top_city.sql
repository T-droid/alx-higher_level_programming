-- displays top 3 cities
SELECT city, AVG(value) as avg_temp
WHERE month = 7 OR month = 8
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
