CREATE TABLE customers_audits (
   id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT NOT NULL,
   cust_surname VARCHAR(40) NOT NULL,
   changed_on TIMESTAMP(6) NOT NULL
);

CREATE OR REPLACE FUNCTION log_surname_change()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.cust_surname <> OLD.cust_surname THEN
		 INSERT INTO customers_audits(customer_id,cust_surname,changed_on)
		 VALUES(OLD.customer_id,OLD.cust_surname,now());
	END IF;

	RETURN NEW;
END;$$;

CREATE or replace TRIGGER surname_changes
  AFTER UPDATE
  ON customers
  FOR EACH ROW
  EXECUTE PROCEDURE log_surname_change();
 
 update customers
 set cust_surname = 'Galkin'
 where customer_id = 1;

select * from customers;

select * from customers_audits;

CREATE OR REPLACE FUNCTION check_rents()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF new.rent_period <= 0 or new.rent_period is null THEN
		RAISE EXCEPTION 'The rent period can not be 0';
	END IF;
	RETURN NEW;
END;$$;

CREATE or replace TRIGGER rent_check
  before insert or update
  ON rents
  FOR EACH ROW
  EXECUTE PROCEDURE check_rents();
 
call insert_rent ('2021-07-22', 0, 230, 10, 5, 17);