-- Create view for project 2

CREATE VIEW Customers_Limited 
AS 
select 
C.customerNumber as customerNumber, 
C.customerName as customerName, 
C.contactLastName as contactLastName, 
C.contactFirstName as contactFirstname, 
C.phone as phone, 
C.addressLine1 as addressLine1, 
C.addressLine2 as addressLine2, 
C.city as city, 
C.state as state, 
C.postalCode as postalCode, 
C.country as country, 
C.salesRepEmployeeNumber as salesRepEmployeeNumber, 
C.creditLimit as creditLimit 
from Customers as C 
join Employees as E on (C.salesRepEmployeeNumber = E.employeeNumber) 
where substring_index(E.Email,'@',1) = substring_index(user(),'@',1);
