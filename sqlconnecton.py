import mysql.connector
a=mysql.connector.connect(host="localhost",user="root")
print(a)
b=a.cursor()
#without try and except
'''
b.execute("create database sandeep")
b.execute("use sandeep")
b.execute("create table Employee(rollno int,ename varchar(20),id int(20),primary key(id))")
b.execute("insert into Employee values(1,'apple',10)")
b.execute("insert into Employee values(2,'mango',20)")
b.execute("insert into Employee values(3,'chili',30)")
b.execute("insert into Employee values(4,'mili',40)")
b.execute("select * from Employee")
'''
#with try and except
try:
    b.execute("create database sandeep1")
    b.execute("use sandeep1")
    b.execute("create table Employee(rollno int,ename varchar(20),id int(20),primary key(id))")
    b.execute("insert into Employee values(1,'apple',10)")
    b.execute("insert into Employee values(2,'mango',20)")
    b.execute("insert into Employee values(3,'chili',30)")
    b.execute("insert into Employee values(4,'mili',40)")
    b.execute("select * from Employee")
    print(b)
except:
    a.rollback()
for i in b:
    print(i)
