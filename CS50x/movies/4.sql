SELECT COUNT(title) from movies where id IN (SELECT movie_id from ratings where rating=10.0);