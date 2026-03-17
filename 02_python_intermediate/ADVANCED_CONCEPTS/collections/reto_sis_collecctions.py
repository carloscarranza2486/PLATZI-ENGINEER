from enum import Enum
from collections import deque, defaultdict, Counter

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

class OrderManagementSystem:
    def __init__(self):
        self.inventory = defaultdict(int)
        
        self.orders_queue = deque()

    def add_inventory(self, products: list[str]):
        for product in products:
            self.inventory[product] += 1
        print("Inventario actualizado.")

    def place_order(self, customer_name: str, product_list: list[str]):
        order_counts = Counter(product_list)
        
        new_order = {
            "customer": customer_name,
            "items": order_counts,  # Guardamos el objeto Counter
            "status": OrderStatus.PENDING # Estado inicial usando tu Enum
        }
        
        self.orders_queue.append(new_order)
        print(f"📦 Pedido de {customer_name} recibido y puesto en cola (Pendiente).")

    # Función para procesar pedidos
    def process_next_order(self):
        if not self.orders_queue:
            print("No hay pedidos pendientes.")
            return

        current_order = self.orders_queue.popleft()
        customer = current_order['customer']
        items = current_order['items']

        print(f"\n--- Procesando pedido de {customer} ---")
        
        # Lógica de validación de Stock
        can_fulfill = True
        for product, quantity in items.items():
            if self.inventory[product] < quantity:
                print(f"Error: No hay suficiente stock de {product}.")
                can_fulfill = False
                break
        
        if can_fulfill:
            # Restamos del inventario
            for product, quantity in items.items():
                self.inventory[product] -= quantity
            
            # Cambiamos estado usando el ENUM
            current_order['status'] = OrderStatus.SHIPPED
            print(f"🚚 ¡Éxito! El pedido ha cambiado a: {current_order['status'].name}")
        else:
            print("⚠️ El pedido no se pudo procesar por falta de stock.")

# --- ZONA DE PRUEBAS ---

# 1. Instanciamos el sistema
sistema = OrderManagementSystem()

# 2. Llenamos el inventario (usando defaultdict)
productos_iniciales = ["Laptop", "Laptop", "Mouse", "Mouse", "Mouse", "Teclado"]
sistema.add_inventory(productos_iniciales)
print("Inventario actual:", dict(sistema.inventory))

# 3. Hacemos un pedido (usando Counter internamente)
pedido_carlos = ["Laptop", "Mouse", "Mouse"] 
sistema.place_order("Carlos", pedido_carlos)

# 4. Procesamos el pedido (validación y cambio de Enum)
sistema.process_next_order()

# 5. Verificamos inventario final
print("Inventario final:", dict(sistema.inventory))