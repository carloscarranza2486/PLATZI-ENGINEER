| product_id  | int unsigned | NO   | PRI | NULL              | auto_increment                                |
| name        | varchar(100) | NO   |     | NULL              |                                               |
| slug        | varchar(200) | NO   | UNI | NULL              |                                               |
| description | text         | YES  |     | NULL              |                                               |
| created_at  | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at  | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+-------------+--------------+------+-----+-------------------+-----------------------------------------------+

INSERT IGNORE INTO products(name, slug) values('bolígrafo azul', 'pluma-azuls')
  ON DUPLICATE kEY UPDATE description = 10*price;

  concat('hola: ', values(slug));


INSERT INTO products(name, slug) values('bolígrafo roja', 'pluma-roja');

INSERT INTO products(name, slug, description) values
  ('bolígrafo negra', 'pluma-negra', 'esto es una pluma para vender'),
  ('bolígrafo rosa', 'pluma-rosa', 'esto es una pluma para vender')


alter TABLE products add COLUMN price float after slug;
