SELECT A.Title, 
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateOfPurchase) >= 0) AND (DATEDIFF(NOW(), DateOfPurchase) <= 30)) THEN 1 ELSE 0 END) AS 'D30', 
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateOfPurchase) >= 31) AND (DATEDIFF(NOW(), DateOfPurchase) <= 60)) THEN 1 ELSE 0 END) AS 'D60',
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateOfPurchase) >= 61) AND (DATEDIFF(NOW(), DateOfPurchase) <= 90)) THEN 1 ELSE 0 END) AS 'D90'
FROM Albums as A
JOIN Songs as S on (A.AlbumID = S.AlbumID)
JOIN Purchases as P on (S.SongID = P.SongID)
GROUP BY A.Title
;