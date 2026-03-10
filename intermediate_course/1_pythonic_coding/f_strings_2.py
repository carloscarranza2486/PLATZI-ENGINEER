bank_balance = 1200000000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.1f}"
print(text)
text = f"El valor del stock es: {stock_price:.2f}"
print(text)

user_id = 10000
text = f"Su id es: {user_id:04d}"
print(text)

product = "Laptop"
price = 1000

text = f"Producto: {product:>15} | price: ${price}"
print(text)
