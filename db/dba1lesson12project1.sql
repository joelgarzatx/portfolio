-- Script for dba1 lesson12 project1

DELIMITER //

DROP PROCEDURE IF EXISTS QuerySchema //

CREATE PROCEDURE QuerySchema
  (
    SelectedSchema varchar(10)
  )
  BEGIN
    IF SelectedSchema = 'tables' THEN SELECT table_name, table_type, engine FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='jgarza';
    ELSEIF SelectedSchema = 'columns' THEN SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='Products' AND table_schema='jgarza';
    ELSEIF Selectedschema = 'views' THEN SELECT table_name, is_updatable, substring(view_definition,27,50) AS definition FROM INFORMATION_SCHEMA.VIEWS WHERE table_schema='jgarza';
    ELSEIF SelectedSchema = 'routines' THEN SELECT routine_name, routine_type, routine_definition FROM INFORMATION_SCHEMA.ROUTINES;
    ELSE SELECT 'INVALID ARGUMENT' as Error_Message;
    END IF;
  END //
  
DELIMITER ;


call QuerySchema('tables');
call QuerySchema('columns');
call QuerySchema('views');
call QuerySchema('routines')\G

-- Unknown argument
call QuerySchema('routies');
