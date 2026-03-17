CREATE TABLE Clients (
  client_id INTEGER unsigned PRIMARY KEY auto_increment,
  name VARCHAR(100),
  email VARCHAR(60) not null UNIQUE,
  phone_number VARCHAR(15) not null,
  created_at TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
  modified_at TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);
