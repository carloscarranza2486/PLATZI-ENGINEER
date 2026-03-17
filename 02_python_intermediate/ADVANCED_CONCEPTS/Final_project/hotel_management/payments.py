import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    print(f"Procesando pago de {amount} para {customer_name}...")
    await asyncio.sleep(random.uniform(1, 3))  # Simula el tiempo de procesamiento
    print(f"Pago de {amount} para {customer_name} procesado con éxito.")
    return True

