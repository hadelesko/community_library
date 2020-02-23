show databases;
create database training;
use training;
Create table country(
country_id varchar(5),
country_name varchar(50),
regionId int(4)
);
select * from country;
Drop table  country;
insert into country values("c1", "United state",1001 );
insert into country(Country_id, country_name) values("c4", "vietnam");
insert into country (Country_id, country_name)values("c5", "Indonesia");
insert into country values("c2", "England", 1002 );
insert into country values("c3", "Germany",1002 );

select * from country where regionid=1002; 
select * from country where country_name!="England";
select * from country where country_name <> "England";
select * from country where regionid<1002;
select * from country where country_name not in ('England','Germany');
select * from country where country_name in ('England','Germany', 'Indonesia');
select * from country where regionid between 1002 and 1003;
select * from country where regionid=1002 or regionid=1003;
select * from country where regionid is null;
select * from country where regionid is not null;


use dynamicinventory;
explain select * from eflow;
select * from eflow;


Create database day3exercise;
use day3exercise;
Create table country(
country_id varchar(5),
country_name varchar(50),
region_id int(4)
);

insert into country values("C1", "United state",1001 );
insert into country values("C2", "Canada",1002 );
insert into country values("c1", "Australia",1003 );


select * from country where region_id = 1001;
select * from country where region_id >= 1002;

truncate table country;
insert into country values("c1", "United state",1001 );
insert into country(Country_id, country_name) values("c4", "vietnam");
insert into country (Country_id, country_name)values("c5", "Indonesia");
insert into country values("c2", "England", 1002 );
insert into country values("c6", "Brazil",1003 );
insert into country values("c3", "Netherland",1002);
insert into country values("c7", "Poland",1004 );
select * from country where country_name not like '%land';