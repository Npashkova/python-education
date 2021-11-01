create table potential_customers(
id int not null primary key,
email VARCHAR(255),
name VARCHAR(255),
surname VARCHAR(255),
second_name VARCHAR(255),
city VARCHAR(255)
);

insert into potential_customers(id, email, "name", surname, second_name, city)
select user_id, email, first_name, last_name, middle_name, city
from users limit 100;

insert into potential_customers(id, email, "name", surname, second_name, city)
values (101, 'vladik101@gmail.com', 'Vlad', 'Shepel', 'Bogdanovych', 'Kyiv');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (102, 'denis102@gmail.com', 'Denis', 'Mironov', 'Olexandrovich', 'Moscow');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (103, 'nastia103@gmail.com', 'Nastia', 'Pashkova', 'Sergeevna', 'Donetsk');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (104, 'zarina104@gmail.com', 'Zarina', 'Bondar', 'Olegivna', 'Irpin');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (105, 'sergey105@gmail.com', 'Sergey', 'White', 'Andriyovich', 'Dnipro');

select * from potential_customers 
order by id desc
limit 5;

select users.first_name, users.email, potential_customers."name", potential_customers.email
from users, potential_customers 
where users.city = 'city 17' and potential_customers.city = 'city 17';

