--Create tables
create table cars(
car_id serial not null primary key,
brand varchar(30),
model varchar(50),
car_number varchar(8),
engine_id integer,
branch_id integer,
foreign key (engine_id) references engines(engine_id),
foreign key (branch_id) references branches(branch_id)
);

create table engines(
engine_id serial not null primary key,
eng_name varchar(30)
);

create table branches(
branch_id serial not null primary key,
br_name varchar(50),
address_id integer,
phone_id integer,
foreign key (address_id) references addresses(address_id),
foreign key (phone_id) references phones(phone_id)
);

create table rents(
rent_id serial not null primary key,
purchase_date text,
rent_period varchar(30),
price integer,
car_id integer,
branch_id integer,
customer_id integer,
foreign key (car_id) references cars(car_id),
foreign key (branch_id) references branches(branch_id),
foreign key (customer_id) references customers(customer_id)
);

create table customers(
customer_id serial not null primary key,
cust_name varchar(50),
cust_surname varchar(50),
address_id integer,
phone_id integer,
foreign key (address_id) references addresses(address_id),
foreign key (phone_id) references phones(phone_id)
);

create table addresses(
address_id serial not null primary key,
city varchar(50),
street varchar(50),
house integer
);

create table phones(
phone_id serial not null primary key,
ph_number varchar(30)
);

--Insert data

begin;
insert into cars(brand, model, car_number)
select 'brand' || b, 'model' || b, 'A' || b
from generate_series(1,500) as b;

select * from cars;

insert into customers(cust_name, cust_surname)
select 'name' || b, 'surname' || b
from generate_series(1,500) as b;

select * from customers;

insert into branches(br_name)
select 'branch' || b
from generate_series(1,50) as b;

select * from branches;

insert into engines(eng_name)
select 'engine' || b 
from generate_series(1,10) as b;

select * from engines;

insert into addresses(city,street,house)
select 'city' || b, 'street' || b, b 
from generate_series(1,550) as b;

select * from addresses;

insert into phones(ph_number)
select '380955550' || n 
from generate_series(100,649) as n;

select * from phones;

commit;

begin;

update branches b
set address_id = a.address_id
from addresses a
where a.address_id = b.branch_id;

select * from branches;

update branches b
set phone_id = p.phone_id
from phones p
where p.phone_id = b.branch_id;

commit;

begin;

update customers c
set phone_id = 50 + p.phone_id
from phones p
where p.phone_id = c.customer_id;

select * from customers;

update customers c
set address_id = a.address_id + 50
from addresses a
where a.address_id= c.customer_id;

commit;

begin;

select * from cars;

update cars c
set branch_id = b.branch_id
from branches b
where b.branch_id = c.car_id / 10;

savepoint my_point;

update cars c
set engine_id = e.engine_id
from engines e
where e.engine_id = c.car_id / 50;

update cars c
set engine_id = 10
where car_id between 1 and 49;

commit;

begin;

select * from rents;

insert into rents(purchase_date, rent_period, price)
select '2021-11-' || i, i, i * 10
from generate_series(1, 30) as i;

insert into rents(purchase_date, rent_period, price)
select '2021-12-' || i, i, i * 10
from generate_series(1, 30) as i;

insert into rents(purchase_date, rent_period, price)
select '2021-10-' || i, i, i * 10
from generate_series(1, 30) as i;

insert into rents(purchase_date, rent_period, price)
select '2021-09-' || i, i, i * 10
from generate_series(1, 30) as i;

commit;

begin;

update rents r
set car_id = c.car_id
from cars c
where c.car_id = r.rent_id;

update rents r
set branch_id = b.branch_id
from branches b
where b.branch_id = r.rent_id;

update rents r
set customer_id = c.customer_id
from customers c
where c.customer_id = r.rent_id;

select * from rents;

commit;


