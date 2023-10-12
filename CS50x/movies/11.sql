Select title from movies
join stars ON movies.id=stars.movie_id
join ratings ON ratings.movie_id=stars.movie_id
join people ON people.id=stars.person_id
where name = "Chadwick Boseman"
order by rating desc
limit 5;