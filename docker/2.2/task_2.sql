select * from "Order"
where order_status_order_status_id in (3,4)
order by order_id; 
 
select order_id, status_name
from "Order" o 
inner join "Order_status" os on o.order_status_order_status_id = os.order_status_id
where status_name in('Finished', 'Paid');