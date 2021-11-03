-- Check cost of different operations without index
explain select * from products p 
order by price;

explain select * from products p 
where price between 50 and 200;

explain select * from products p 
where price < 100;

explain select * from products p 
where price = 150;

-- Check cost of order by with index using btree (uses seqscan again)
create index idx_products_price on products 
using btree (price);

explain select * from products p 
order by price;

--Check if index works for other operations (uses index for all operators below, but not for ">"(uses seqscan for ">")
explain select * from products p 
where price between 50 and 200;

explain select * from products p 
where price = 150;

explain select * from products p 
where price > 100;

explain select * from products p 
where price < 100;



