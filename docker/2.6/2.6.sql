--Look up all views we have now (nothing yet)
SELECT table_name
FROM INFORMATION_SCHEMA.views
WHERE table_schema = ANY(current_schemas(false));

--Creating view for table products
create or replace view product_handy_info
as
select product_id as id,
product_title as name,
in_stock as presence,
price
from products
where in_stock > 0
order by presence, price;

select * from product_handy_info;

--Creating views for tables order_status and order
create or replace view order_handy_info
as
select order_id as id,
carts_cart_id as cart,
status_name as status,
total as bill,
created_at as "date"
from "Order" o 
inner join "Order_status" os on os.order_status_id = o.order_status_order_status_id;

select * from order_handy_info;

create view canceled_orders
as
select * from order_handy_info
where status = 'Canceled';

select * from canceled_orders

create or replace view active_orders
as
select * from order_handy_info
where status not in ('Finished', 'Canceled');

select * from active_orders
order by bill;

--Creating views for tables products and categories
create view product_category
as
select product_id as id,
product_title as name,
product_description as description,
in_stock as presence, 
price,
category_title as category
from products p 
inner join categories c on p.category_id = c.category_id 
order by price;

select * from product_category;

create view product_food
as
select * from product_category
where category = 'Category 5';

select * from product_food;

--Materialized view
create materialized view income_per_product
as
select product_title, sum(price) as total_money
from cart_product cp
join products p on p.product_id = cp.products_product_id 
join carts c on c.cart_id = cp.carts_cart_id 
join "Order" o on o.carts_cart_id = c.cart_id
group by product_title, price
order by sum(price) desc
with no data;

select * from income_per_product;

refresh materialized view income_per_product;

--Look up all views we have now and drop them
SELECT table_name
FROM INFORMATION_SCHEMA.views
WHERE table_schema = ANY(current_schemas(false));

drop view order_handy_info cascade;

drop view product_handy_info cascade;

drop view product_category cascade;

drop materialized view income_per_product;
