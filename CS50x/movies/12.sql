
SELECT title from movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
where name="Johnny Depp"
and title in
(SELECT title from movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
where name="Helena Bonham Carter"

);


