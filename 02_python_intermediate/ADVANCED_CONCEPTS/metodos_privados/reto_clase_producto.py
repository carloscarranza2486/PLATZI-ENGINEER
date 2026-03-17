class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price
    
    @property
    def stock(self):
        return self._stock
    
    @price.setter
    def price(self,new):
        if new < 0:
            raise ValueError("Price cannot be negative")
        self._price = new
    
    @stock.setter
    def stock(self, stock_change):
        if self._stock + stock_change < 0:
            raise ValueError("Total stock cannot be negative")
        self._stock += stock_change

    @price.deleter
    def price(self):
        try:  
            del self._price
            print(f"The price of {self.name} has been deleted")
        except AttributeError:
            print("Attributte not found")
        
    @stock.deleter
    def stock(self):
        try: 
            del self._stock
            print(f"The stock of {self.name} has been deleted")  
        except AttributeError:
            print("Attributte not found")

producto1 = Product("Chocolate",10,100)
producto2 = Product("Caramelo",5,150)
print(producto1.price)
producto1.price = 12
print(producto1.price)
producto1.stock = -20
print(producto1.stock)
del producto1.price
print(producto2.price)
producto2.price = 12
print(producto2.price)
producto2.stock = 200
print(producto2.stock)
producto2.price = 13
print(producto2.price)
del producto2.stock
del producto2.stock