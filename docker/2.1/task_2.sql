alter table users add column phone_number INT;
select phone_number from users;

alter table users alter column phone_number type VARCHAR;
select phone_number from users;