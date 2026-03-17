import asyncio
import time
import random
import multiprocessing

#Función asíncrona para verificar el inventario

async def check_inventory(item):
    print(f'Verificando inventario para {item}...')
    await asyncio.sleep(random.randint(3,6))
    print(f'Inventario verificado para {item}')
    #Simular disponibiidad del producto
    return random.choice([True, False])

#Función asíncrona para procesar el pago

async def process_payment(order_id):
    print(f'Procesando pago para la orden {order_id}...')
    #Simular el tiempo de espera que tiene un servicio de pago
    await asyncio.sleep(random.randint(3,6))
    print(f'Pago procesado para la orden {order_id}')
    return True

# Función intensuva en CPU para calcular costo del pedido

def calculate_total(items):
    print(f'Calculando el costo total para {len(items)} artículos...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'El costo total calculado: {total}')
    return total

async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden {order_id}...')
    #Verificar inventario para cada artículo
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)

    if not all(inventory_results):
        print(f'Orden {order_id} cancelada: Producto no está disponible')

    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))

    #Procesar el pago asincrónicamente
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Orden {order_id} completada cpn éxito. Total: {total}')
    else:
        print(f'Error al procesar pago de la orden {order_id}')

async def main():
    orders = [
        {
            'oder_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'mouse'}]
        },
        {
            'oder_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'monitor'}]
        },
        {
            'oder_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'monitor'}]
        }
    ]

    #Processar múltiples órdenes concurrentemente

    task = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*task)

#Creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())