USE alx_book_store;

SELECT `COLUMN_NAME`, `COLUMN_TYPE`, `IS_NULLABLE`, `COLUMN_KEY`, `EXTRA`
FROM `information_schema`.`columns`
WHERE `table_name` = 'books' AND `table_schema` = 'alx_book_store';
