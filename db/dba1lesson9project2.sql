-- script to create stored procedure AddNewAlbum

DROP PROCEDURE IF EXISTS AddNewAlbum;

DELIMITER //

CREATE PROCEDURE AddNewAlbum(
  NameOfArtist varchar(50),
  AlbumName varchar(50),
  YearReleased year(4),
  NumberOfSongs int
  )
  
  BEGIN
    DECLARE artist_id int;
    DECLARE artist_count int;
    
    SELECT DISTINCT COUNT(*) INTO artist_count
    FROM Artists
    WHERE ArtistName = NameOfArtist;
    
    IF (artist_count = 0) THEN
      INSERT INTO Artists (ArtistName) VALUES (NameOfArtist);
      SELECT LAST_INSERT_ID() into artist_id;
    ELSE
      SELECT ArtistID INTO artist_id
      FROM Artists
      WHERE ArtistName = NameOfArtist;      
    END IF;
    
    INSERT INTO Albums (ArtistID, Title, YearReleased, NumberOfSongs)
    VALUES (artist_id, AlbumName, YearReleased, NumberOfSongs);
  END;
//
  
DELIMITER ;