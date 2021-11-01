select product_id, carts_cart_id
from products p
left join cart_product cp on p.product_id = cp.products_product_id 
where cp.carts_cart_id is null
order by product_id;

select distinct p.product_title
from products p
left join cart_product cp on cp.products_product_id = p.product_id
left join carts c on c.cart_id = cp.carts_cart_id
left join "Order" o on o.carts_cart_id = c.cart_id
where o.order_id is null
order by product_title;

select count(products_product_id) as top, products_product_id 
from cart_product cp 
group by products_product_id 
order by top desc
limit 10;

select count(products_product_id) as top, products_product_id 
from cart_product cp
join carts c on c.cart_id = cp.carts_cart_id 
join "Order" o on o.carts_cart_id = c.cart_id
group by products_product_id
order by top desc
limit 10;

select user_id, first_name
from "Order" o
join carts c on c.cart_id = o.carts_cart_id 
join users u on u.user_id = c.users_user_id 
order by o.total desc
limit 5;

select count(order_id) as top, u.user_id, u.first_name
from "Order" o 
join carts c on o.carts_cart_id  = c.cart_id 
join users u on u.user_id = c.users_user_id 
group by u.user_id
order by top desc
limit 5;

select u.first_name , u.last_name 
from users u 
join carts c on c.users_user_id  = u.user_id 
left join "Order" o on o.carts_cart_id  = c.cart_id 
where o.order_id is null 
order by u.user_id
limit 5






