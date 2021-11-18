create or replace function discount_by_brand (x varchar)
returns table(rent_id integer, brand varchar, price integer)
language plpgsql
as $$
begin
	update rents r
	set price = 20
	from cars c
	where c.car_id = r.car_id and c.brand = x;

	if not found then
     raise 'Car with brand % not found', x;
    end if;

   	return query
    select r.rent_id, c.brand, r.price from rents r
    join cars c on c.car_id = r.car_id 
	where c.brand = x;

end;
$$;

select r.rent_id, c.brand, r.price from rents r 
join cars c on c.car_id = r.car_id;

select * from discount_by_brand('brand10'); 

drop function discount_by_brand(varchar);

--other one

create or replace function get_customer(c_city varchar)
returns text as $$
declare
	 names text default '';
	 cur_names cursor(c_city varchar)
		 for select cust_name, city
		 from customers c
		 join addresses a on a.address_id = c.address_id 
		 where city = c_city;
begin
   open cur_names(c_city);
   names := 'Name: ';
   loop
      fetch cur_names into names;
      exit when not found;
   end loop;
   close cur_names;
   return names;
end; $$
language plpgsql;

select * from get_customer('city100');
