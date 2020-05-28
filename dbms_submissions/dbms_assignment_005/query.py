Q1 = """ SELECT pid as actor_id,COUNT(mid) as no_of_movies FROM cast group by pid;"""

Q2 = """ SELECT year,count(id) as count FROM Movie group by year ORDER BY year ASC;"""

Q3 = """ SELECT year,avg(rank) as avg_rank FROM Movie group by year having count(id)>10 order by year desc;"""

Q4 = """ SELECT  year,max(rank) as max_rank FROM Movie group by year order by year asc;"""

Q5 = """ SELECT rank,count(id) as no_of_movies FROM Movie where name like "a%" group by rank;"""



