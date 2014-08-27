-- Create four new users
create user 'wpatterson'@'localhost' identified by 'oreillySTDBA2';
create user 'gbondur'@'localhost' identified by 'oreillySTDBA2';
create user 'abow'@'localhost' identified by 'oreillySTDBA2';
create user 'ljennings'@'localhost' identified by 'oreillySTDBA2';

-- Set up privileges
grant select,insert,update,delete on classicmodels.OrderDetails to 'wpatterson'@'localhost';
grant select,insert,update,delete on classicmodels.Orders to 'wpatterson'@'localhost';
grant select,insert,update,delete on classicmodels.Payments to 'wpatterson'@'localhost';

grant select,insert,update,delete on classicmodels.OrderDetails to 'gbondur'@'localhost';
grant select,insert,update,delete on classicmodels.Orders to 'gbondur'@'localhost';
grant select,insert,update,delete on classicmodels.Payments to 'gbondur'@'localhost';

grant select,insert,update,delete on classicmodels.OrderDetails to 'abow'@'localhost';
grant select,insert,update,delete on classicmodels.Orders to 'abow'@'localhost';
grant select,insert,update,delete on classicmodels.Payments to 'abow'@'localhost';

grant select,insert on classicmodels.OrderDetails to 'ljennings'@'localhost';
grant select,insert on classicmodels.Orders to 'ljennings'@'localhost';
grant select,insert on classicmodels.Payments to 'ljennings'@'localhost';