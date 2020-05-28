Q1 = """select a.id,a.fname,a.lname,a.gender from actor as a inner join cast  as c 
     on  a.id= c.pid inner join movie as m on m.id=c.mid where m.name like
     "Annie%";"""
     
Q2 = """select m.id,m.name,m.rank,m.year from movie as m
       inner join moviedirector as md on md.mid=m.id 
       inner join director as d on d.id=md.did
       where (d.fname="Biff" and d.lname="Malibu") and 
       (m.year IN (1994,1999,2003))
       order by m.rank desc,m.year asc;"""
      

Q3 = """  SELECT m.year, count(m.id) as no_of_movies
FROM movie  as m
GROUP BY m.year 
HAVING AVG(m.rank)>(SELECT AVG(m.rank)
                   FROM movie as m) order by year asc;"""       
       
       
Q4 = """  SELECT * FROM movie  as m  where m.year =2001 and
m.rank < (SELECT AVG(m.rank)
                  FROM movie as m where m.year=2001) 
                  order by m.rank desc limit 10;"""       
       

Q5 = """select m.id as movie_id,count("F") as no_of_female_actors,
    count("M") as no_of_male_actors 
    from actor as a inner join cast as c on a.id=c.pid 
    inner join movie as m on m.id=c.mid group by c.mid limit 100;"""


Q6 = """select distinct pid from cast group by mid,pid 
       having count(distinct role)>1 order by pid asc limit 100;"""


Q7 = """select d.fname ,count(d.id) from director as d group by d.fname 
having count(d.fname)>1;"""


# Q8 = """ select id,fname,lname from director as d 
#           inner join moviedirector as md on md.did=d.id
#           inner join cast as c on
#           md.did=d.id group by d.id having count(c.pid)>100;"""



Q8 = '''select * from director as d
            where exists (select md.did from cast c
            inner join moviedirector md on md.mid=c.mid
            where md.did=d.id group by md.did,md.mid having count(distinct c.pid) >=100)
            and not exists 
            (select md.did from cast c
            inner join moviedirector md on md.mid=c.mid
            where md.did=d.id group by md.did,md.mid having count(distinct c.pid) <100);'''