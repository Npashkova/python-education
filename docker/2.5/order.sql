-- Check how much search costs without index
explain select * from "Order" o 
where total > 500 and created_at between '2018-01-01' and '2019-12-31';

--Create index and check with it (uses seqscan again)
create index idx_order_total_created_at on "Order"(total, created_at);
explain select * from "Order" o 
where total > 500 and created_at between '2018-01-01' and '2019-12-31';

-- Try different query ("> >"does not use index, "> =" uses, "= >" uses, "between >" uses, "< >" uses)
explain select * from "Order" o 
where total > 500 and created_at > '2019-12-31';

explain select * from "Order" o 
where total > 500 and created_at = '2018-01-01';

explain select * from "Order" o 
where total = 500 and created_at > '2019-01-01';

explain select * from "Order" o 
where total between 100 and 300 and created_at > '2018-01-01';

explain select * from "Order" o 
where total < 300 and created_at > '2018-01-01';

explain select * from "Order" o 
where total < 300 and created_at < '2018-01-01'
order by total;

explain select * from "Order" o 
where total < 100 and created_at > '2019-01-01'
order by created_at;