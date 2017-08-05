with alfa as (
select 
url_string,
strpos(url_string,'/') first_slash,
substring(url_string,0,strpos(url_string,'/')) t_1,
substring(url_string,strpos(url_string,'/')+1,300) tr_1


from 
th.article_url_strings
--limit 10
),

beta as (
select 
url_string,
first_slash,
t_1,
tr_1,

strpos(tr_1,'/') second_slash,
substring(tr_1,0,strpos(tr_1,'/')) t_2,
substring(tr_1,strpos(tr_1,'/')+1,300) tr_2

from 
alfa
)


select t_1, t_2 from beta 
group by t_1, t_2
order by t_1, t_2

--select count(tr_2)c , count(distinct tr_2)cd from beta 

-- to find distinct key words
select distinct t_1 from beta union
select distinct t_2 from beta
