select
  case
    when email like '%@gmail.com' then 'gmail'
    when email like '%@hotmail.com' then 'hotmail'
    when email like '%@yahoo.com' then 'yahoo'
    when email like '%@kozey.com' then 'kozey'
    else 'otro proveedor de correo'
  end as proveedor,
  count(*) as total_clientes
from clients
GROUP by proveedor
HAVING total_clientes between 100 and 17000
order by total_clientes asc



case
  when [condition] then 'print'
  else 'print'
end
