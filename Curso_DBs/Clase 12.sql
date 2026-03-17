create table if not EXISTS bill_products(
  bill_product_id INTEGER unsigned primary key auto_increment,
  bill_id INTEGER unsigned not null,
  product_id INTEGER unsigned not null,
  quantity integer not null default 1,
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  FOREIGN KEY (bill_id) REFERENCES bills(bill_id)
    on delete CASCADE
    on update CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
    on delete CASCADE
    on update CASCADE
);


insert into clients(client_id, name, email, phone_number) values(10,'eduardo', 'eduardo@email.com', '0000000000');
insert into products(name, slug) values('cuaderno','slug-cuaderno');
insert into bills(client_id, total) values(10, 15.00);
insert into bill_products(product_id, bill_id) values(1,3);
