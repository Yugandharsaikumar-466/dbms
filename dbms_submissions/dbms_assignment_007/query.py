Q1 = """SELECT count(id) FROM MOVIE WHERE year < 2000;""" 

Q2 = """ SELECT AVG(rank) FROM MOVIE WHERE year = 1991;"""

Q3 = """ SELECT min(rank) FROM MOVIE WHERE year = 1991;"""

Q4 = """ SELECT fname, lname FROM actor inner join cast on id=pid where mid=27;"""

Q5 = """ SELECT count(distinct mid) FROM actor inner join cast on id=pid where fname="Jon" and lname="Dough";"""

Q6 = """ SELECT name FROM MOVIE where name like "Young Latin Girls%" and year between 2003 and 2006;"""

Q7= """ SELECT fname,lname FROM director  inner join moviedirector on director.id=moviedirector.did inner join movie  on movie.id=moviedirector.mid where name like "Star Trek%";"""

Q8 = """ SELECT movie.name FROM movie INNER JOIN moviedirector on `movie`.id = `moviedirector`.mid
         INNER JOIN   director on `director`.id=`moviedirector`.did   
         INNER JOIN cast on `moviedirector`.mid = `cast`.mid
         INNER JOIN Actor on `actor`.id=`cast`.pid
         WHERE actor.fname = "Jackie (I)" and director.fname="Jackie (I)" and 
         actor.lname = "Chan" and director.lname="Chan";   """
 
Q9 = """ SELECT d.fname,d.lname from director AS d INNER JOIN moviedirector AS md ON d.id=md.did
         INNER JOIN movie as m on m.id=md.mid where m.year =2001 group by d.id having count(m.id)>=4  ORDER BY fname asc,lname desc;"""

Q10 ="""select  gender,count(gender) from actor group by gender order by gender asc;"""


Q11 = """ SELECT distinct m1.name,m2.name,m1.rank,m1.year from movie as m1 INNER JOIN
          movie as m2 on m1.id>m2.id where m1.year=m2.year and m1.rank = m2.rank 
          order by m1.name asc limit 100;"""


Q12 = """ SELECT a.fname, m.year,m.rank from actor as a inner join cast as c on c.pid=a.id
      inner join  movie as m on m.id=c.mid order by a.fname asc,m.year desc limit 100;"""


Q13 = """ select a.fname,d.fname,avg(rank) as score from director as d inner join moviedirector
      as md on d.id=md.did inner join cast as c on c.mid=md.mid inner join movie as m on c.mid=m.id
       inner join actor as a on a.id=c.pid group by d.id,a.id having count(m.id)>=5 order by score desc,d.fname asc,a.fname desc limit 100; """