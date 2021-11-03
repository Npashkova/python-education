--Looking for indexes existing (output: only pk)
SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname;

--Try without index(0.00-98.50)
explain select * from users
where is_staff = 0;

--Create index and try is_staff = 0 (uses seqscan again)
create index idx_users_is_staff 
on users(is_staff);

explain select * from users
where is_staff = 0;

--Try select is_staff = 1 (uses index)
explain select * from users
where is_staff = 1;

--Drop index and make it with more conditions (uses seqscan again)
drop index idx_users_is_staff;

create index idx_users_not_staff
on users(is_staff)
where is_staff = 0;

explain select * from users
where is_staff = 0;

--Try to make seqscan off and watch results(index leads to worse cost)
SET enable_seqscan = OFF;

explain select * from users
where is_staff = 0;

--Try implement index for searching is_staff = 1 (uses index and cost is the lowest)
SET enable_seqscan = ON;

drop index idx_users_not_staff;

create index idx_users_is_staff
on users(is_staff)
where is_staff = 1;

explain select * from users
where is_staff = 1;

explain select * from users
where is_staff = 1 and users.city = 'city 3';

explain select * from users
where is_staff = 1 and users.city = 'city 3' and users.last_name = 'last_name 3';

--So, all queries that contain is_staff = 1 will perform with index.







