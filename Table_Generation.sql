-- SQL for generating tables in UPSC.TH Postgres Schema

--Grants
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA TH TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA TH TO postgres;

--Main Table and its sequence
CREATE TABLE TH.Article_urls (
  URL_id SERIAL PRIMARY KEY,
  Url_dt TEXT,
  Url TEXT
);

CREATE SEQUENCE TH.Article_urls_seq
  start 1
  increment 1;

commit; 


--Strings Table

CREATE TABLE TH.Article_url_strings (
  Url_string TEXT
);

INSERT INTO TH.Article_url_strings ( Url_string )
SELECT  substring( reverse(substring( reverse(url) , strpos(reverse(url),'/') +1 ,300)) ,38 ,300)  URL_String
FROM    TH.Article_urls ;  

commit; 
