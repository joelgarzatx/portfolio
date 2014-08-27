-- Script for dba1 lesson8 project2

-- create the view as BigAlbums
CREATE VIEW BigAlbums AS
  SELECT A.ArtistName, B.Title, B.NumberOfSongs as Songs
  FROM Artists as A
  JOIN Albums as B on (A.ArtistID = B.ArtistID)
  WHERE B.NumberOfSongs = (SELECT MAX(NumberOfSongs) FROM Albums)
;
  
-- Display view
-- SELECT * FROM BigAlbums;  

-- drop the view
DROP VIEW IF EXISTS BigAlbums;

-- create the view as LongAlbums
CREATE VIEW LongAlbums AS
  SELECT A.ArtistName, B.Title, B.NumberOfSongs as Songs
  FROM Artists as A
  JOIN Albums as B on (A.ArtistID = B.ArtistID)
  WHERE B.NumberOfSongs = (SELECT MAX(NumberOfSongs) FROM Albums)
;

-- Display view
-- SELECT * FROM LongAlbums;  