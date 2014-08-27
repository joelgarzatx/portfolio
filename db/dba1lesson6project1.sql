SELECT A.ArtistID, A.ArtistName, A.BandWebURL, B.AlbumID, B.Title, B.YearReleased, B. Rating, B.NumberOfSongs
FROM Artists as A
JOIN Albums as B on (A.ArtistID = B.ArtistID);