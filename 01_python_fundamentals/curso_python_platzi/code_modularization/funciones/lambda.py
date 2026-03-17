# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero solo una expresión

# sintaxis lambda argumentos : expresión 

# x = lambda a,b : a + b

# print(x(2,3))

def mi_funcion(n):
    return lambda a : a * n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)
quintuplicador = mi_funcion(5)

print(duplicador(5))
print(triplicador(5))
print(quintuplicador(5))