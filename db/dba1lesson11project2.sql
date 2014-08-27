-- Script for dba1 lesson11 project2

SELECT Title, SUBSTRING(AlbumDescription,1,50) as Description, 'NO' as QueryExpansion, 'guitars' as Query
FROM Albums
WHERE MATCH (AlbumDescription)
AGAINST ('guitars')
UNION ALL
SELECT Title, SUBSTRING(AlbumDescription,1,50) as Description, 'NO' as QueryExpansion, 'liverpool' as Query
FROM Albums
WHERE MATCH (AlbumDescription)
AGAINST ('liverpool')
UNION ALL
SELECT Title, SUBSTRING(AlbumDescription,1,50) as Description, 'YES' as QueryExpansion, 'guitars' as Query
FROM Albums
WHERE MATCH (AlbumDescription)
AGAINST ('guitars' WITH QUERY EXPANSION)
UNION ALL
SELECT Title, SUBSTRING(AlbumDescription,1,50) as Description, 'YES' as QueryExpansion, 'liverpool' as Query
FROM Albums
WHERE MATCH (AlbumDescription)
AGAINST ('liverpool' WITH QUERY EXPANSION)
;