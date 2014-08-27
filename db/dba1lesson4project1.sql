INSERT INTO Artists (ArtistID, ArtistName, BandWebURL) VALUES (1, 'Bob Dylan', 'www.bobdylan.com');
INSERT INTO Artists (ArtistID, ArtistName, BandWebURL) VALUES (2, 'Johnny Cash', 'www.johnnycash.com');
INSERT INTO Artists (ArtistID, ArtistName, BandWebURL) VALUES (3, 'The Beatles', 'www.thebeatles.com');
INSERT INTO Artists (ArtistID, ArtistName, BandWebURL) VALUES (4, 'Rolling Stones', 'www.rollingstones.com');
INSERT INTO Artists (ArtistID, ArtistName, BandWebURL) VALUES (5, 'The Time Lords', 'http://youtu.be/bdTELokKfCk');

INSERT INTO Albums (AlbumID, ArtistID, Title, YearReleased, Rating, NumberOfSongs) VALUES (1, 1, 'Blonde on Blonde', 1966, 5, 14);
INSERT INTO Albums (AlbumID, ArtistID, Title, YearReleased, Rating, NumberOfSongs) VALUES (2, 2, 'Man in Black', 1971, 5, 10);
INSERT INTO Albums (AlbumID, ArtistID, Title, YearReleased, Rating, NumberOfSongs) VALUES (3, 3, 'Let It Be', 1970, 5, 15);
INSERT INTO Albums (AlbumID, ArtistID, Title, YearReleased, Rating, NumberOfSongs) VALUES (4, 4, 'Let It Bleed', 1979, 5, 9);
INSERT INTO Albums (AlbumID, ArtistID, Title, YearReleased, Rating, NumberOfSongs) VALUES (5, 5, 'Doctorin'' the Tardis', 1988, 5, 1);

INSERT INTO Songs (SongID, AlbumID, TrackNumber, SongName) VALUES (1, 1, 1, 'Rainy Day Women #12 & 35');
INSERT INTO Songs (SongID, AlbumID, TrackNumber, SongName) VALUES (2, 1, 2, 'Pledging My Time');
INSERT INTO Songs (SongID, AlbumID, TrackNumber, SongName) VALUES (3, 1, 3, 'Visions of Johanna');
INSERT INTO Songs (SongID, AlbumID, TrackNumber, SongName) VALUES (4, 1, 4, 'One of Us Must Know (Sooner or Later)');
INSERT INTO Songs (SongID, AlbumID, TrackNumber, SongName) VALUES (5, 1, 5, 'I Want You');

INSERT INTO ATunesCustomers (CustomerID, FirstName, LastName, Address, EmailAddress, FavoriteArtistID) VALUES (1, 'Alice', 'Jones', '123 Ash Street', 'alice@home.com', 1);
INSERT INTO ATunesCustomers (CustomerID, FirstName, LastName, Address, EmailAddress, FavoriteArtistID) VALUES (2, 'Bob', 'Smith', '234 Birch Street', 'bob@home.com', 2);
INSERT INTO ATunesCustomers (CustomerID, FirstName, LastName, Address, EmailAddress, FavoriteArtistID) VALUES (3, 'Carol', 'Hernandez', '345 Conifer Street', 'carol@home.com', 2);
INSERT INTO ATunesCustomers (CustomerID, FirstName, LastName, Address, EmailAddress, FavoriteArtistID) VALUES (4, 'David', 'Goldsmith', '456 Date Palm Street', 'david@home.com', 4);
INSERT INTO ATunesCustomers (CustomerID, FirstName, LastName, Address, EmailAddress, FavoriteArtistID) VALUES (5, 'Eunice', 'Cho', '567 Evergreen Street', 'eunice@home.com', 1);

INSERT INTO Purchases (CustomerID, DateOfPurchase, SongID) VALUES (1, NOW(), 1);
INSERT INTO Purchases (CustomerID, DateOfPurchase, SongID) VALUES (1, NOW(), 2);
INSERT INTO Purchases (CustomerID, DateOfPurchase, SongID) VALUES (1, NOW(), 3);
INSERT INTO Purchases (CustomerID, DateOfPurchase, SongID) VALUES (5, NOW(), 2);
INSERT INTO Purchases (CustomerID, DateOfPurchase, SongID) VALUES (5, NOW(), 5);

INSERT INTO CustomerAccounts (CustomerID, CurrentCredit) VALUES (1, 0);
INSERT INTO CustomerAccounts (CustomerID, CurrentCredit) VALUES (2, 5);
INSERT INTO CustomerAccounts (CustomerID, CurrentCredit) VALUES (3, 10);
INSERT INTO CustomerAccounts (CustomerID, CurrentCredit) VALUES (4, 20);
INSERT INTO CustomerAccounts (CustomerID, CurrentCredit) VALUES (5, 40);



