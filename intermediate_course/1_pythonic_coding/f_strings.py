"""Ejemplos y explicaciones de f-strings en Python."""

from datetime import datetime

name = "Ana"
year = 2020
text = f"Hola {name}"
text_2 = "Hola"

text_calculo = f"Hola, {name}, tu edad es: {2025 - year} años"
print(text_calculo)
text_func = f"HOLA {name.upper()}"
print(text_func)
edad = 16
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad"
print(text_if)
bank_balance = 1200000000
user_id = 10000
text = f"Su id es: {user_id:04d}"
print(text)
product = "Laptop"
price = 1000

text = f"Producto: {product:<15} | Precio: {price:>10}"

print(f"{text}\n{text}")

date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
