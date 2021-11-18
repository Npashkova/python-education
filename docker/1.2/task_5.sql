create or replace procedure discount()
language plpgsql
as $$
begin
    update rents
    set price = price * 0.5
    where rent_period > 20;
    commit;
end;$$;

select * from rents;

call discount();

create or replace procedure insert_rent(
date varchar, period int, price integer, car_id int, branch_id int, customer_id int)
language plpgsql
as $$
begin
    insert into rents(purchase_date, rent_period, price, car_id, branch_id, customer_id)
    values(date, period, price, car_id, branch_id, customer_id);
    commit;
end;$$;

select * from rents;

call insert_rent ('2021-07-22', 7, 230, 10, 5, 17);

