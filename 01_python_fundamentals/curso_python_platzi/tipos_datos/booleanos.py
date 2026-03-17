v = True
f = False

print(v)
print(f)

print(5 > 3) # verdadero
print(3 > 5) # falso

print(type(v))

print(bool("Hola, mundo"))
print(bool(""))

# true

print(bool("abc"))
print(bool("123"))
print(bool(["manzana", "pera"]))

# False

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

x = 123
print(isinstance(x, int))