-- script to create stored procedure AddNewAlbum
DELIMITER //

CREATE PROCEDURE AddNewAlbum(
  NameOfArtist varchar(50),
  AlbumName varchar(50),
  YearReleased year(4),
  NumberOfSongs int
  )
  
  BEGIN
    DECLARE artist_id int;
    
    SELECT ArtistID into artist_id
    FROM Artists
    WHERE ArtistName = NameOfArtist;
    
    INSERT INTO Albums (ArtistID, Title, YearReleased, NumberOfSongs)
    VALUES (artist_id, AlbumName, YearReleased, NumberOfSongs);
  END;
//
  
DELIMITER ;