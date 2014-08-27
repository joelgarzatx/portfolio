SELECT A.FirstName, A.LastName, COUNT(P.CustomerID) as SongsPurchased
FROM ATunesCustomers as A
JOIN Purchases as P on (A.CustomerID = P.CustomerID)
GROUP BY A.CustomerID
ORDER BY SongsPurchased DESC
LIMIT 0,5
;