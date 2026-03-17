# función: Es un bloque de código que solo se ejecuta cuando la llamamos. periten organizar y modularizar el código (reutilización)

def saludar(nombre, nacionalidad="colombia"): # argumentos
    print("Hola, ", nombre,"de", nacionalidad)
    
# saludar("Carlos", "España") # parametros
# saludar("John") # parametros

def sumar(a,b):
    return a+b

def resta(a,b):
    return a-b
    
def multiplicar(a, b):
    return a * b

def division(a, b):
    return a / b

Resultados = sumar(10,5),resta(10,5), multiplicar(10,5), division(10,5)
print(Resultados)