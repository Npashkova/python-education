--Creating first procedure
create temporary table shop(
	product_id serial not null primary key,
	product_title varchar(255),
	in_stock integer,
	price integer);

insert into shop(product_title, in_stock, price)
values 
('tea', 50, 39),
('coffee', 38, 120),
('sweets', 27, 98),
('bisquits', 30, 25),
('nuts', 40, 50),
('cake', 10, 40),
('chocolate', 15, 35)

create or replace procedure sell_product(product varchar, quantity integer)
language plpgsql    
as $$
declare
   r record;
   new_in_stock int;
begin
	for r in select * from shop 
	order by in_stock loop
		if r.in_stock = 0 then
			raise notice 'We need to order %', r.product_title;
		end if;
	end loop;
	update shop 
	set in_stock = in_stock - quantity
	where product_title = product
	returning in_stock into new_in_stock;
		if new_in_stock >= 0 then
			commit;
		else
			rollback;
		end if;
end
$$

call sell_product('cake', 10);
select * from shop;
call sell_product('coffee', 5);

--Creating second procedure

insert into shop(product_title, in_stock, price)
values('cigarettes', 20, 70), ('liquer', 15, 200);

alter table shop add column discounted_price integer

create or replace procedure discount(product varchar)
language plpgsql    
as $$
declare
	new_price integer;
	r record;
begin
	if product not in ('cigarettes', 'liquer') and (select price from shop where product_title = product) >= 50 then
		update shop s
		set discounted_price = price * 0.7
		where product = product_title
		returning discounted_price into new_price;
		raise notice 'The price on % was changed to %!', product, new_price;
		commit;
	elsif product in ('cigarettes', 'liquer') then
		raise notice 'We don`t make discounts on alcohol and cigatters!';
	else
		raise notice 'The price on % is low enough!', product;
	end if;
	for r in select * from shop loop
	if r.discounted_price is not null then
	raise notice 'We have discount on %', r.product_title;
	end if;
	end loop;
end
$$

select * from shop
order by price desc;
call discount('tea');
call discount('coffee');
call discount('cigarettes');
call discount('sweets');

--Drop procedures

drop procedure discount(varchar);
drop procedure sell_product(varchar, integer);