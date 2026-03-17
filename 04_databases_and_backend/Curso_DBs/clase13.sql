create table test (
  test_id INTEGER unsigned PRIMARY KEY auto_increment,
  name VARCHAR(100) not NULL,
  qty integer,
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP
);

alter table test add column price FLOAT first;
alter table test drop COLUMN price;

alter table test modify column price decimal(10,3) not null;
alter table test rename column price to prices;
alter table test rename to tests;
