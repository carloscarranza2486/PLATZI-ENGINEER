print("hola, 'mundo'")

ingles = "I'm Carlos"

multiples = """hola
mundo
desde
las
comillas
triples"""

print(ingles)
print(multiples)

palabra = "murciélago"
print(len(palabra))

texto = " Este curso es  de fundamentos de Python"
estaIncluida = "Python" in texto
noEstaIncluida = "Javascript" not in texto

print(estaIncluida)
print(noEstaIncluida)

mayuscula = texto.upper()
minuscula = texto.lower()

texto2 = texto.upper
texto2 = texto.lower

print(mayuscula)
print(minuscula)
print(texto2)

espacios = "      este es el texto        "
sinEspacios = espacios.strip()

print(sinEspacios)