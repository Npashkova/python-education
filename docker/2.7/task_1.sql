create function shipping_total_by_city_zero(x varchar)
returns table(order_id integer, shipping_total decimal, user_city varchar)
language plpgsql
as $$
begin
	update "Order" o
	set shipping_total = 0
	from carts c 
	join users u on u.user_id = c.users_user_id
	where o.carts_cart_id = c.cart_id  and u.city = x;

	if not found then
     raise 'User with city % not found', x;
    end if;
   
   	return query
   	select o.order_id, o.shipping_total, u.city from "Order" o
	join carts c on o.carts_cart_id = c.cart_id 
	join users u on u.user_id = c.users_user_id
	where u.city = x;
   	
end;
$$;

select * from shipping_total_by_city_zero('city 6');
select * from shipping_total_by_city_zero('city 8');

select o.order_id, o.shipping_total, u.city from "Order" o
join carts c on o.carts_cart_id = c.cart_id 
join users u on u.user_id = c.users_user_id;

select o.order_id, o.shipping_total, u.city from "Order" o
join carts c on o.carts_cart_id = c.cart_id 
join users u on u.user_id = c.users_user_id
where u.city = 'city 8';

drop function if exists shipping_total_by_city_zero(varchar);
