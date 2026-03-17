create table investment (
  investment_id integer unsigned primary key auto_increment,
  product_id integer unsigned not null,
  investment integer not null default 0
)

insert into investment(product_id, investment)
select product_id, stock * price from products
