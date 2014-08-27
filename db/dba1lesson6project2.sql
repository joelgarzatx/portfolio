SELECT A.CustomerID,A.FirstName,A.LastName,A.Address,A.EmailAddress,A.FavoriteArtistID,C.CurrentCredit,P.DateOfPurchase,P.SongID
FROM ATunesCustomers as A
LEFT JOIN Purchases as P on (A.CustomerID=P.CustomerID) 
LEFT JOIN CustomerAccounts as C on (A.CustomerID=C.CustomerID);