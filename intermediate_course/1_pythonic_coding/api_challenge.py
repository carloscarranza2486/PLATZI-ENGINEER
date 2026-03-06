import requests

# 1. Le decimos al mensajero que traiga datos (GET) de esta dirección
respuesta = requests.get('https://api.github.com')

# 2. Verificamos si la misión fue un éxito
if respuesta.status_code == 200:
    print("¡Misión exitosa! Código 200 OK")

    # 3. Extraemos el "paquete" y lo convertimos en un diccionario de Python
    datos = respuesta.json()
else:
    print(f"Algo falló. Código de error: {respuesta.status_code}")
