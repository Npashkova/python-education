--Views
create or replace view customer_activity
as
select cust_name || ' ' || cust_surname as name, purchase_date,
rent_period, price, brand || ' ' || model as car, br_name as branch
from rents r
join customers c on c.customer_id = r.customer_id 
join cars ca on ca.car_id = c.customer_id 
join branches b on b.branch_id = r.branch_id; 

select * from customer_activity;

create or replace view branch_info
as
select br_name as branch, city || ',' || street || ' ' || house as address, ph_number as phone
from branches b
join addresses a on b.address_id = a.address_id 
join phones p on p.phone_id = b.phone_id;

select * from branch_info;

create  materialized view branch_profit
as
select br_name as branch, sum(rent_period * price) as total 
from rents r
join branches b on b.branch_id = r.branch_id
group by br_name
order by total desc
with no data;

refresh materialized view branch_profit;

select * from branch_profit;

--dropping

drop view customer_activity cascade;

drop view branch_info cascade;

drop materialized view branch_profit;