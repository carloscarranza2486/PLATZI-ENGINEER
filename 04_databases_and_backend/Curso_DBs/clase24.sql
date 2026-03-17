select
  b.bill_id,
  b.status,
  c.name,
  count(bp.bill_product_id) as stock,
  round(sum(bp.quantity * p.price * (1 - bp.discount/100))) as total

select concat('el cliente ' , c.name, 'tiene una cuenta ', b.status, ' con ', count(bp.bill_product_id),
' productos y suma $', round(sum(bp.quantity * p.price * (1 - bp.discount/100)))) as resultado
from bills as b
left join clients as C
  on b.client_id = c.client_id
left join bill_products as bp
  on bp.bill_id = b.bill_id
left join products as p
  on p.product_id = bp.product_id
GROUP BY b.bill_id
