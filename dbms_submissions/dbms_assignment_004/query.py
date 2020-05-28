Q1 = """ SELECT COUNT(name) FROM Movie WHERE year =2002 and name like "Ha%" and rank > 2;"""

Q2 = """ SELECT MAX(rank) FROM Movie WHERE (name like "Autom%") and (year =1983 or year= 1994) ;"""

Q3 = """ SELECT  COUNT(id) FROM Actor WHERE (gender = "M") and (fname like "%ei" or lname like "ei%");"""

Q4 = """ SELECT AVG(rank) FROM Movie WHERE (year= 1993 or year =1995 or year =2000) and (rank >= 4.2);"""

Q5 = """ SELECT SUM(rank) FROM Movie WHERE name like "%Hary%" and (year BETWEEN 1981 and 1984) and (rank < 9); """

Q6 = """ SELECT MIN(year) FROM Movie WHERE rank = 5;"""

Q7 = """ SELECT  COUNT(id ) FROM Actor WHERE fname = lname or (gender = "F");"""

Q8 = """SELECT DISTINCT fname FROM Actor WHERE lname like "%ei"  ORDER BY fname asc LIMIT 100;"""

Q9 = """SELECT  id,name as movie_title,year FROM Movie  WHERE  year IN (2001,2002,2005,2006) LIMIT 25 OFFSET 10;"""

Q10= """ SELECT DISTINCT lname FROM Director WHERE fname IN ("Yeud","Wolf","Vicky") ORDER BY lname asc LIMIT 5;"""

