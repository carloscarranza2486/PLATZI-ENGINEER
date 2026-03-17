# ind    01234
texto = "Este es un texto"

print(texto[5:-2])

curso = "este curso es de Javascript"
print(curso.replace("Javascript","Python"))

textoDividido = texto.split(" ")
print(textoDividido)

# Normalización

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas".lower() in texto2.lower())