#Importa funciones de los modulos dentro del paquete

from ecommerce.sales.orders import add_order, get_order

add_order(1, 'Laptop', 2)
get_order(1, 'Mouse')