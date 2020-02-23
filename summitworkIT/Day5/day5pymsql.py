# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:52:03 2020

@author: adjimagnan
"""
import pymysql
db = pymysql.connect("localhost","root","danken00","myday5")
cursor=db.cursor()

sql="""Create table country(
country_id varchar(5),
country_name varchar(50),
regionId int(4));"""

sqls="""insert into country values("c1", "United state",1001 );"""
# sql2="""insert into country(country_id, country_name) values("c4", "vietnam");
# sql2 = """insert into country (country_id, country_name)values("c5", "Indonesia");"""
#sql2 = """insert into country values("c2", "England", 1002 );"""
sql2="""insert into country values("c3", "Germany",1002 );"""

cursor.execute(sql2)
db.commit()
select="""select * from country; """
m=cursor.execute(select)
db.commit()
fetchall=cursor.fetchall()
[print(row) for row in fetchall ]