SELECT A.ArtistName, B.Title, B.NumberOfSongs as Songs
FROM Artists as A
JOIN Albums as B on (A.ArtistID = B.ArtistID)
WHERE B.NumberOfSongs = (SELECT MAX(NumberOfSongs) FROM Albums)
;