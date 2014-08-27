INSERT INTO Songs (AlbumID, TrackNumber, SongName) VALUES (1, 6, 'Bear Necessities');

DELETE FROM Songs WHERE AlbumID=1 AND SongName='Bear Necessities';

UPDATE Albums SET Title='Blood on the Tracks' WHERE Title='Blonde on Blonde';