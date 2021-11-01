-- INSERT potential_customers;

begin;

select * from potential_customers pc
order by id desc limit 10;

insert into potential_customers(id, email, "name", surname, second_name, city)
values (106, 'valerio106@gmail.com', 'Valerii', 'Balan', 'Bogdanovych', 'Kyiv');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (107, 'glebo107@gmail.com', 'Gleb', 'Zalevskiy', 'Mykhailovych', 'Lviv');

savepoint two_inserts;


insert into potential_customers(id, email, "name", surname, second_name, city)
values (108, 'kate108@gmail.com', 'Kate', 'Bale', 'Marco', 'London');


insert into potential_customers(id, email, "name", surname, second_name, city)
values (109, 'grt109@gmail.com', 'Artur', 'Gorn', 'Mykhailovych', 'Madrid');

rollback to savepoint two_inserts;

commit;

--UPDATE potential_customers;

begin;

select * from potential_customers pc
order by id desc limit 10;

update potential_customers 
set surname = 'Abidi'
where id = 104;

rollback;

--INSERT AND DELETE potential_customers;

begin;

select * from potential_customers pc
order by id desc limit 10;

insert into potential_customers(id, email, "name", surname, second_name, city)
values (108, 'kate108@gmail.com', 'Kate', 'Bale', 'Marco', 'Kyiv');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (109, 'grt109@gmail.com', 'Artur', 'Gorn', 'Mykhailovych', 'Lviv');

savepoint inserts;

delete from potential_customers where city = 'Kyiv';

rollback to savepoint inserts;

delete from potential_customers where city = 'Irpin';

commit;

--UPDATE AND DELETE potential_customers;

begin;

select * from potential_customers pc
order by id desc limit 10;

update potential_customers 
set city = 'Kharkiv'
where id = 103;

savepoint updates;

delete from potential_customers where city = 'Kharkiv';

rollback to savepoint updates;

delete from potential_customers where city = 'Dnipro';

release savepoint updates;

commit;

--Products

begin;

select * from products
order by product_id desc limit 15;

insert into products(product_id, product_title, product_description, in_stock, price, slug, category_id)
values (4001, 'Ice-cream', 'Food', 10, 20, 'Ice-cream!', 5);

savepoint inserting;

delete from products where product_title = 'Ice-cream';

rollback to savepoint inserting;

update products
set in_stock = 30
where product_title = 'Ice-cream';

savepoint updating30;

delete from products where product_description = 'Food';

rollback to savepoint updating30;
release savepoint inserting;

update products
set in_stock = in_stock + 20
where product_title = 'Ice-cream';

commit;

--Products2

begin;

select product_id, product_title, price from products
order by price;

update products
set price = price * 1.1;

savepoint higherprice;

update products
set price = price * 0.5;

rollback to savepoint higherprice;

rollback;

--Order_status

begin;
 
select * from "Order_status" os;

insert into "Order_status"(order_status_id, status_name)
values (6, 'Delivered')

commit;

set transaction isolation level repeatable read;
begin;

select * from "Order_status" os 

alter table "Order_status" add column time TIMESTAMP;

rollback;

--Order_status2

begin;

select * from "Order_status" os; 

update "Order_status" 
set status_name = 'Done-well'
where order_status_id = 6

delete from "Order_status" 
where order_status_id = 6;

commit;

