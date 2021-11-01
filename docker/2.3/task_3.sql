select category_title, sum(in_stock)
from products p
inner join categories c on p.category_id = c.category_id 
group by c.category_id 
order by sum(in_stock) DESC;
