SET sql_mode='traditional';
SET transaction isolation level serializable;

SELECT * FROM ATunesCustomers;

START TRANSACTION;

DELETE FROM ATunesCustomers WHERE CustomerID=1;

UPDATE ATunesCustomers SET FirstName="Barbara" WHERE CustomerID=2;

SELECT * FROM ATunesCustomers;

ROLLBACK;

SELECT * FROM ATunesCustomers;
