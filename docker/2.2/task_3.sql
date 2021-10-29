select product_id, price from products
where price between 80 and 150
order by price;
select product_id, price  from products
where price > 80 and price <= 150
order by price;

select order_id, created_at from "Order" o 
where created_at > '2020-10-01'
order by created_at;

select order_id, created_at from "Order" o 
where created_at between '2020-01-01' and '2020-06-30'
order by created_at;
select order_id, created_at from "Order" o 
where created_at >= '2020-01-01' and created_at < '2020-07-01'
order by created_at;

select product_id, product_title, category_title
from products p
inner join categories c on p.category_id = c.category_id
where category_title in ('Category 7', 'Category 11', 'Category 18');
select product_id, product_title, category_title
from products p
inner join categories c on p.category_id = c.category_id
where category_title = 'Category 7' or category_title = 'Category 11' or category_title = 'Category 18';

select order_id, status_name, created_at
from "Order" o 
inner join "Order_status" os on o.order_status_order_status_id = os.order_status_id
where status_name !='Finished' and created_at <= '2020-12-31';

select cart_id, order_id
from carts c
left join "Order" o on c.cart_id = o.carts_cart_id
where order_id is null
order by cart_id ;




