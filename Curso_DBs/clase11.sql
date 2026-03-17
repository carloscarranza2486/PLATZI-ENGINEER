create table if not exists products (
  product_id INTEGER unsigned primary key auto_increment,
  name VARCHAR(100) not null,
  slug VARCHAR(200) not null unique,
  description text,
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);

create table if not EXISTS bills (
  bill_id INTEGER unsigned primary KEY auto_increment,
  client_id INTEGER not null,
  total float,
  status enum ('open', 'partial', 'lost') not null default 'open',
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);

create table bill_products (
  bill_product_id integer unsigned primary key auto_increment,
  bill_id integer unsigned not null,
  product_id INTEGER unsigned not null,
  quantity integer not null default 1,
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);


insert into clients (client_id, name, email) values (10, 'eduardo', "eduardo@mail.com');
insert into products (name, slug) values('cuaderno', 'slug-cuaderno');
insert into bills(client_id, total) values (10, 15.00);
insert into bill_products(product_id, bill_id) values(1,3);
