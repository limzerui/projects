SELECT AVG(rating) from ratings where movie_id in (SELECT id from movies where year=2012);