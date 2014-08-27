SELECT A.ArtistName, COUNT(B.Title) as Albums
FROM Artists as A
JOIN Albums as B on (A.ArtistID = B.ArtistID)
GROUP BY A.ArtistName;