--Triggers (first)

create table customers(
   id serial primary key,
   name varchar(100) not null,
   surname varchar(100) not null,
   city varchar(100) not null
);

create table customers_audit (
   id integer generated always as identity,
   customer_id integer not null,
   city varchar(100) not null,
   updated timestamp(6) not null
);

insert into customers(name, surname, city)
values 
('Igor', 'Popov', 'Dnipro'),
('Vlad', 'Shepeliuk', 'Kyiv'),
('Petro', 'Amanov', 'Kyiv'),
('Maria', 'Vlasova', 'Odessa'),
('Irina', 'Glazkova', 'Kharkiv');

select * from customers;
select * from customers_audit;

create or replace function log_city_changes()
returns trigger
language plpgsql
as
$$
begin
	if new.city != old.city and length(new.city) > 2 then
		insert into customers_audit(customer_id, city, updated)
		values(old.id, old.city, now());
	elsif length(new.city) < 2 then
		raise exception 'City must me more than 1 character';
	end if;
	return new;
end;
$$;

create trigger city_changes
before update 
on customers
for each row
execute procedure log_city_changes();

begin;

update customers
set city = 'Kharkiv'
where id = 2;

update customers 
set city = 'Lviv'
where id = 5;

select * from customers;

select * from customers_audit;

savepoint two_updates;

update customers 
set city = 'O'
where id = 4;

rollback to savepoint two_updates;

select * from customers;

release savepoint two_updates;

commit;

select * from customers;

drop trigger city_changes on customers;

--Triggers (second)

create table participants(
id serial primary key,
name varchar(100) not null,
surname varchar(100) not null,
birth_date date not null
);

insert into participants(name,surname,birth_date)
values
('Andrew', 'Makarov', '1999-12-16'),
('Mark', 'Chumak', '1993-05-29'),
('Egor', 'Osipov', '1998-03-21');

select * from participants;

create or replace function check_age()
returns trigger
language plpgsql
as
$$
begin
	if (select extract (year from age(current_date,new.birth_date))) < 18 then
		raise exception 'Participant must be 18 years old.';
	elsif length(new.name) < 2 then
		raise exception 'Name must be more than 1 character long.';
	end if;
	return new;
end;
$$;

create or replace trigger check_participants_age
before insert or update
on participants
for each row
execute procedure check_age();

begin;

insert into participants(name,surname,birth_date)
values
('OLga', 'Markova', '1996-10-06');

insert into participants(name,surname,birth_date)
values
('Angela', 'Surkova', '2001-07-26');

savepoint two_inserts;

insert into participants(name,surname,birth_date)
values
('A', 'Medova', '2002-07-26');

rollback to savepoint two_inserts;

insert into participants(name,surname,birth_date)
values
('Anna', 'Medova', '2005-07-26');

rollback to savepoint two_inserts;

select * from participants;

release savepoint two_inserts;

commit;

drop trigger check_participants_age on participants;
