--Window function

create temporary table product_categories(
	category_id serial primary key,
	category_name varchar(255) not null
);

create temporary table products(
	product_id serial primary key,
	product_title varchar(255) not null,
	price integer,
	category_id int not null,
	foreign key (category_id) references product_categories (category_id)
);

insert into product_categories (category_name)
values
	('Fruits'),
	('Vegetables'),
	('Berries');

insert into products (product_title,price, category_id)
values
	('Apple', 20, 1),
	('Orange', 40, 1),
	('Mango', 100, 1),
	('Pineapple', 120, 1),
	('Banana', 30, 1),
	('Tomato', 38, 2),
	('Potato', 12, 2),
	('Cucumber', 58, 2),
	('Strawberry', 69, 3),
	('Blueberry', 101, 3),
	('Raspberry', 94, 3);

select * from products;

select category_name, product_title, price, 
avg(price) over (partition by category_name)
from products p 
join product_categories using(category_id);