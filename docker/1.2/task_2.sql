--JOINS
explain select cust_name || ' ' || cust_surname as name, city, ph_number as phone
from customers c
inner join addresses a on a.address_id = c.address_id
inner join phones p on p.phone_id = c.phone_id
where p.ph_number like '38095555015%' and city like 'city1%';

select cust_name || ' ' || cust_surname as name, rent_period * price as total_sum, brand || ' ' || model as car
from customers c 
left join rents r on r.customer_id = c.customer_id 
left join cars ca on ca.car_id = r.car_id
order by total_sum;

select brand || ' ' || model as car, rent_period, br_name
from cars ca 
left join rents r on r.car_id = ca.car_id
left join branches b on b.branch_id = r.branch_id;

--Indexes 
explain select city
from addresses
where city like 'city1%';

create index idx_city on addresses(city);

drop index idx_city;

explain select ph_number
from phones
where ph_number = '380955550111';

create index idx_phone on phones(ph_number);

drop index idx_phone;

explain select rent_period * price as total_sum
from rents
where rent_period * price between 500 and 1000
order by total_sum;

create index idx_total_sum on rents(rent_period, price);

drop index idx_total_sum;

explain select brand || ' ' || model as car, price
from cars ca 
left join rents r on ca.car_id = r.car_id
where price = 100;

create index idx_rent_price on rents (price);

drop index idx_rent_price;

