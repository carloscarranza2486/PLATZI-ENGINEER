SELECT [columnas, variables, operaciones y funciones]
FROM [table/s]
WHERE [Condiciones]
GROUP BY
HAVING
ORDER BY
LIMIT [1 o 2 valores]

select product_id, name, price, stock,
(price*stock) as total
from PRODUCTS
order by total desc
limit 2, 10


select name, product_id, price, stock
(round(price*stock)) as total
from PRODUCTS
order by total asc
limit 10
