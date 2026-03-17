select p.product_id as pid, p.name, p.price, i.investment,
  round(i.investment / p.price) as inv_calculated,
  p.stock,
  if(round(i.investment / p.price) = p.stock, 'perfecto', 'error') as status
from investment as i
LEFT JOIN products as p
  on p.product_id = i.product_id
where investment > 100000
  and investment_id % 10 = 0
limit 10


-- Personal exercise

select p.name, p.product_id, i.price, round(i.investment / i.price) as total_stock,
p.stock as compared_stock
from products as p
left join investment as i
  on i.product_id = p.product_id
where p.stock > 5 and i.price > 10
order by total_stock desc
limit 1
