select name
from products
WHERE
price between 500 and 700


select * from bill_products
WHERE discount > 0


select * from bill_products
WHERE
  date_added between '2024-09-24' and '2024-09-30 14:50:00'
  and product_id in (825, 500, 1986)


select name, email, phone_number from clients
WHERE email like '%.biz'



update clients
set phone_number = '+575512345678'
where client_id = 6
limit 1

select name, phone_number, client_id from clients
WHERE
  name like 'laura%'
  or name like 'claire%'


  update clients
  set phone_number = null
  where
    (name like 'laura%'
    or name like 'claire%')
    and phone_number is not null

8 - 91

UPDATE PRODUCTS set stock = stock - 3 where product_id = 8
