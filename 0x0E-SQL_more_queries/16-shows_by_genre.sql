-- List shows and genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
LEFT JOIN tv_genres ON  tv_show_genres.genre_id = tv_genres.id
ORDER BY  title ASC, name ASC;
