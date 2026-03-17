class Order:
    global_discount = 10
    
    def __init__(self, amount):
        self.amount = amount
    
    @staticmethod
    def order_amount_check(amount):
        return amount >= 50
    
    @classmethod
    def create_order(cls, amount):
        if cls.order_amount_check(amount):
            final_amount = amount - (amount * cls.global_discount / 100)
            return cls(final_amount)
        else:
            print("Monto insuficiente para crear el pedido")
            return None
        
nuevo_pedido = Order.create_order(100)
if nuevo_pedido:
    print(f"Pedido creado con éxito. Monto final (con 10% dto): $ {nuevo_pedido.amount}")

