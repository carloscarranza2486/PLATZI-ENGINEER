create table if not exists products (
  product_id integer unsigned PRIMARY KEY auto_increment,
  sku VARCHAR(20) not null unique,
  name VARCHAR(50) not null,
  slug varchar(50) not null unique,
  description text,
  created_at TIMESTAMP not null default current_timestamp,
  modified_at TIMESTAMP not null default current_timestamp
    on update CURRENT_TIMESTAMP
);

alter table products add column price double(10, 2) after slug;
