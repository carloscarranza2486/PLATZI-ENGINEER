def add_order(order_id, product_name, quantity):
    print(f'Orden {order_id} procesada: {quantity} unidades de {product_name}.')

def get_order(order_id, product_name=None):
    print(f'Obteniendo detalles de la orden {order_id}...')
    # Aquí podrías agregar lógica para recuperar los detalles de la orden desde una base de datos o archivo.
    return {
        'order_id': order_id,
        'product_name': product_name if product_name else 'Producto desconocido',
        'quantity': 10
    }