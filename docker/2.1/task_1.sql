create table Users(
user_id INT not null primary key,
email VARCHAR(255),
password VARCHAR(255),
first_name VARCHAR(255),
last_name VARCHAR(255),
middle_name VARCHAR(255),
is_staff INT,
country VARCHAR(255),
city VARCHAR(255),
address TEXT);

create table Products(
product_id INT not null primary key,
product_title VARCHAR(255),
product_description text,
in_stock INT,
price FLOAT,
slug VARCHAR(45),
category_id INT NOT null);

create table Categories(
category_id INT not null primary key,
category_title VARCHAR(255),
category_description text);

create table Cart_product(
carts_cart_id INT not null,
products_product_id INT not null);

create table Carts(
cart_id INT not null primary key,
Users_user_id INT NOT null,
subtotal DECIMAL,
total DECIMAL,
timestamp TIMESTAMP(2));

create table "Order"(
order_id INT not null primary key,
Carts_cart_id INT NOT null,
Order_status_order_status_id INT NOT null,
shipping_total DECIMAL,
total DECIMAL,
created_at TIMESTAMP(2),
updated_at TIMESTAMP(2));

create table "Order_status"(
order_status_id INT not null primary key,
status_name VARCHAR(255));

alter table Cart_product
add constraint FK_Cart_product_carts_cart_id_TO_Carts foreign key (carts_cart_id)
references Carts(cart_id);

alter table Cart_product
add constraint FK_Cart_product_products_product_id_TO_Products foreign key (products_product_id)
references Products(product_id);

alter table Products
add constraint FK_Products_category_id_TO_Categories foreign key (category_id)
references Categories(category_id);

alter table Carts
add constraint FK_Carts_Users_user_id_TO_Users foreign key (Users_user_id)
references Users(user_id);

alter table "Order"
add constraint FK_Order_Carts_cart_id_TO_Carts foreign key (Carts_cart_id)
references Carts(cart_id);

alter table "Order"
add constraint FK_Order_Order_status_order_status_id_TO_Order_status foreign key (Order_status_order_status_id)
references "Order_status"(order_status_id);

select * from users u;
select * from products p;
select * from categories c;
select * from carts;
select * from cart_product;
select * from "Order_status" os;
select * from "Order" o;




