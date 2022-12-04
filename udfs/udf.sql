create or replace database udf_db;
use database udf_db;
create schema if not exists udf_schema_public;
use schema udf_schema_public;

create or replace table udf_db.udf_schema_public.sales 
  as
    (select * from SFSALESSHARED_SFC_SAMPLES_EU_FRANKFURT_SAMPLE_DATA.TPCDS_SF10TCL.store_sales limit 1000);

create function udf_max()
  returns NUMBER(7,2)
  as
  $$
    select max(SS_LIST_PRICE) from udf_db.udf_schema_public.sales
  $$
  ;

select udf_max();

create or replace function
udf_db.udf_schema_public.get_market_basket(input_item_sk number(38))
returns table (input_item NUMBER(38,0), basket_item_sk NUMBER(38,0),
num_baskets NUMBER(38,0))
as
 'select input_item_sk, ss_item_sk basket_Item, count(distinct
ss_ticket_number) baskets
from udf_db.udf_schema_public.sales
where ss_ticket_number in (select ss_ticket_number from udf_db.udf_schema_public.sales where ss_item_sk = input_item_sk)
group by ss_item_sk
order by 3 desc, 2';

drop database if exists udf_db;