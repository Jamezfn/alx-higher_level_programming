-- Displays the average temperature
SELECT city,
	ROUND(AVG(value), 4) AS avg_temp FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC
