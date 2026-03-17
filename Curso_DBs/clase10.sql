create table if not exists clients (
  client_id integer primary key auto_increment,
  name varchar(100) not null,
  email VARCHAR(100) not null unique,
  phone_number VARCHAR(15) not null,
  created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);
