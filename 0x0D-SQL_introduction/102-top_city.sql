-- Displays the top 3 of cities
SELECT city,
	ROUND(AVG(value), 4) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
