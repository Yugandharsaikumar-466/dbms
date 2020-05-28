Q1= """ select fname, lname from actor as a inner join cast as c on a.id = c.pid where mid=12148;"""

Q2= """ select count(mid) from actor inner join cast on id = pid where fname="Harrison (I)" and lname="Ford";"""

Q3= """ select distinct pid from cast inner join movie on id == mid where name like "young latin girls%";"""

Q4= """ select count(distinct pid) from cast inner join movie on id == mid where year between 1990 and 2000;"""


