select AVG(total) as average_total
from "Order" o
inner join "Order_status" os on o.order_status_order_status_id = os.order_status_id 
where status_name = 'Finished'

select max(total)
from "Order" o 
where updated_at between '2020-07-01' and '2020-09-30';

select max(total)
from "Order" o 
where updated_at >= '2020-07-01' and updated_at <= '2020-09-30';