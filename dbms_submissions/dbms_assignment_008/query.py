Q1= """select id,fname from director 
where exists(select md.did  from moviedirector
as md inner join movie as m on md.mid = m.id where 
m.year >2000 and md.did = director.id)
and not exists(select md.did from moviedirector 
as md inner join movie as m on md.mid = m.id  where 
m.year <2000 and md.did=director.id) order by director.id asc;"""


# Q2 = """ select d.fname,m.name from movie as m,
#  (select max(rank) from movie group by moviedirector.did order by name asc) 
#           inner join moviedirector as md on md.mid=m.id 
#           inner join director as d on md.did=d.id limit 30;"""



# inner join movie as m on m.id=d.id,(select name,max(rank)
#           from movie as m inner join moviedirector as md on m.id=md.mid
#           where md.did group by md.did order by name asc) limit 1 ;"""


# Q2 = """ select d.fname,movie.name,(select m.name  from movie as m 
#           inner join moviedirector as md on m.id=md.mid 
#           inner join director as d on d.id=md.did and m.id = md.did 
#           order by m.rank desc) as name  from director as d limit 10;"""  


Q2 = """ select di.fname,(select m.name  from movie as m 
          inner join moviedirector as md on m.id=md.mid 
          where md.did=di.id
          order by m.rank desc,m.name ASC limit 1)from director as di limit 100;"""  
                    
          
#inner join director as d on di.id=md.did and di.id = d.id

Q3 ="""select * from actor as a where not exists(select m.id from movie as m 
        inner join cast as c on c.mid=m.id where a.id=c.pid and m.year between 
        1990 and 2000) order by a.id desc limit 100;"""