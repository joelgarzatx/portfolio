-- DBA 1 FINAL PROJECT

DROP TABLE IF EXISTS ArticleAuthors;
CREATE TABLE ArticleAuthors
(
  AuthorID int AUTO_INCREMENT NOT NULL,
  FirstName varchar(50),
  LastName varchar(50),
  Email varchar(50),
  Bio text,
  PRIMARY KEY (AuthorID)
) ENGINE=INNODB;

INSERT INTO ArticleAuthors (FirstName, LastName, Email, Bio)
  VALUES ('Abby','Adelaid','abby@atunes.com','I like to fish.');
INSERT INTO ArticleAuthors (FirstName, LastName, Email, Bio)
  VALUES ('Bobby','Biddily','bobby@atunes.com','I like cats.');
INSERT INTO ArticleAuthors (FirstName, LastName, Email, Bio)
  VALUES ('Carry','Caruso','carry@atunes.com','Muffins are my thing.');
INSERT INTO ArticleAuthors (FirstName, LastName, Email, Bio)
  VALUES ('Dorry','Dorado','dorry@atunes.com','No muffin top for me, fitness drives me.');
INSERT INTO ArticleAuthors (FirstName, LastName, Email, Bio)
  VALUES ('Emmit','Elizondo','emmit@atunes.com','All about the shoes for me!');
  
EXPLAIN ArticleAuthors;
SELECT * FROM ArticleAuthors;

  
DROP TABLE IF EXISTS ArticleCategories;
CREATE TABLE ArticleCategories
(
  CategoryID int AUTO_INCREMENT NOT NULL,
  CategoryText varchar(25),
  PRIMARY KEY (CategoryID)
) ENGINE=INNODB;

INSERT INTO ArticleCategories (CategoryText) VALUES ('MySQL');
INSERT INTO ArticleCategories (CategoryText) VALUES ('Oracle');
INSERT INTO ArticleCategories (CategoryText) VALUES ('SQL Server');
INSERT INTO ArticleCategories (CategoryText) VALUES ('Queries');
INSERT INTO ArticleCategories (CategoryText) VALUES ('Stored Procedures');
INSERT INTO ArticleCategories (CategoryText) VALUES ('NoSQL');

EXPLAIN ArticleCategories;
SELECT * FROM ArticleCategories;


DROP TABLE IF EXISTS Commenters;
CREATE TABLE Commenters
(
  CommenterID int AUTO_INCREMENT NOT NULL,
  FirstName varchar(50),
  LastName varchar(50),
  Email varchar(50),
  PRIMARY KEY (CommenterID)
) ENGINE=INNODB;

EXPLAIN Commenters;

DROP TABLE IF EXISTS Articles;
CREATE TABLE Articles
(
  ArticleID int AUTO_INCREMENT NOT NULL,
  Title varchar(100) NOT NULL,
  Blurb varchar(200),
  ArticleText text,
  PostDate datetime,
  AuthorID int,
  CategoryID int,
  PRIMARY KEY (ArticleID)
) ENGINE=MyISAM;

ALTER TABLE Articles ADD FULLTEXT(Title, ArticleText);

INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with MySQL', 'About my work with MySQL', 'MySQL is a relational database, or RDBMS. RDBMS stands for Relational Database Management System. It is an open source RDBMS.', NOW(), 1, 1);
INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with Oracle', 'About my work with Oracle', 'Oracle is a relational database. Oracle has been selling the RDBMS since the early 90s.', NOW(), 2, 2);
INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with SQL Server', 'About my work with SQL Server', 'SQL Server is a relational database.', NOW(), 3, 3);
INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with NoSQL', 'About my work with NoSQL', 'A NoSQL or Not Only SQL database provides a mechanism for storage and retrieval of data that is modeled in means other than tabular.', NOW(), 4, 6);
INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with MongoDB', 'About my work with MongoDB', 'MongoDB is a NoSQL DB.', NOW(), 5, 6);
INSERT INTO Articles (Title, Blurb, ArticleText, PostDate, AuthorID, CategoryID)
  VALUES ('Experience with Stored Procedures', 'About my work with Stored Procedures', 'Store procedures are very useful.', NOW(), 5, 5);  

EXPLAIN Articles;
SELECT * FROM Articles;


DROP TABLE IF EXISTS Comments;
CREATE TABLE Comments
(
  CommentID int AUTO_INCREMENT NOT NULL,
  CommentText text,
  ArticleID int,
  CommenterID int,
  PRIMARY KEY (CommentID)
) ENGINE=INNODB;

EXPLAIN Comments;

DROP TABLE IF EXISTS ArticleViews;
CREATE TABLE ArticleViews
(
  ArticleID int,
  DateViewed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=INNODB;

INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (1, NOW());
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (2, NOW());
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (3, NOW());
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (4, NOW());
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (5, DATE_SUB(NOW(),INTERVAL 15 DAY) );
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (6, DATE_SUB(NOW(),INTERVAL 15 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (1, DATE_SUB(NOW(),INTERVAL 15 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (1, DATE_SUB(NOW(),INTERVAL 25 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (1, DATE_SUB(NOW(),INTERVAL 25 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (2, DATE_SUB(NOW(),INTERVAL 25 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (2, DATE_SUB(NOW(),INTERVAL 25 DAY));
INSERT INTO ArticleViews (ArticleID, DateViewed) VALUES (3, DATE_SUB(NOW(),INTERVAL 25 DAY));

EXPLAIN ArticleViews;

DROP VIEW IF EXISTS ArticleDisplay;
CREATE VIEW ArticleDisplay AS
  SELECT a.Title,a.ArticleText,a.PostDate, CONCAT(aa.FirstName,' ',aa.LastName) as AuthorName, ac.CategoryText
  FROM Articles a
  JOIN ArticleAuthors aa on (a.AuthorID = aa.AuthorID)
  JOIN ArticleCategories ac on (a.CategoryID = ac.CategoryID);
  
EXPLAIN ArticleDisplay;
SELECT * FROM ArticleDisplay;

DROP PROCEDURE IF EXISTS AddComment;

DELIMITER //
CREATE PROCEDURE AddComment (
  article_ID int,
  first_name varchar(50),
  last_name varchar(50),
  email varchar(50),
  comment_text text
  )
  BEGIN
    DECLARE commenter_id int;
    DECLARE commenter_check int DEFAULT 0;
    
    SELECT DISTINCT COUNT(*) INTO commenter_check
    FROM Commenters c
    WHERE c.Email = email;
    
    IF (commenter_check = 0) THEN
      INSERT INTO Commenters (FirstName, LastName, Email) VALUES (first_name, last_name, email);
      SELECT LAST_INSERT_ID() INTO commenter_id; 
    ELSE    
      SELECT CommenterID INTO commenter_id
      FROM Commenters c
      WHERE c.Email = email;  
    END IF;

    INSERT INTO Comments (CommentText, ArticleID, CommenterID) VALUES (comment_text, article_id, commenter_id);
  END;
//
DELIMITER ;

CALL AddComment(1,'Frank','Federici','frank@commentistador.com','Great article.');
CALL AddComment(2,'Greta','Grabowski','greta@commentistador.com','How did you like it?');
CALL AddComment(3,'Han','Hernandez','han@commentistador.com','Thanks for posting!!');
CALL AddComment(3,'Ingrid','Ingleton','ingrid@commentistador.com','Invest in timeshares.');
CALL AddComment(4,'Joe','Joblowski','joe@commentistador.com','This really helped!!');
CALL AddComment(5,'Frank','Federici','frank@commentistador.com','Great article.');

SELECT * FROM Comments;
SELECT * FROM Commenters;



-- Queries

-- Full text index on Articles
SELECT Title, 'rdbms' AS QueryString, MATCH(Title, ArticleText) AGAINST ('rdbms') AS RELEVANCE
FROM Articles
WHERE MATCH(Title, ArticleText) AGAINST ('rdbms' WITH QUERY EXPANSION);

SELECT Title FROM Articles WHERE MATCH(Title, ArticleText) AGAINST ('FileMaker');

-- Pivot Articles View
SELECT a.Title,
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateViewed) >= 0) AND (DATEDIFF(NOW(), DateViewed) <= 10)) THEN 1 ELSE 0 END) AS 'D10',
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateViewed) > 10) AND (DATEDIFF(NOW(), DateViewed) <= 20)) THEN 1 ELSE 0 END) AS 'D20',
  SUM(CASE WHEN ((DATEDIFF(NOW(), DateViewed) > 20) AND (DATEDIFF(NOW(), DateViewed) <= 30)) THEN 1 ELSE 0 END) AS 'D30'
FROM Articles a
JOIN ArticleViews as av ON (a.ArticleID = av.ArticleID)
GROUP BY a.Title
;

-- Show most popular article (most rows in ArticleViews)
SELECT vc.ArticleID, MAX(vc.ViewCount) as MostViews
FROM (SELECT ArticleID, COUNT(1) as ViewCount
      FROM ArticleViews
      GROUP BY ArticleID) as vc
      
  
