x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor a y ó x es menor a z")
elif x == y:
    print("X es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumplió")
    
    
a = "Python"
b = "Javasript"
c = "Python"
 
if a == c:
    if a == b:
        print("a es igual a c pero es distinto a b")
    else:
        print("Estoy saliendo por el else del if interno")     
else:
    print("a no es igual a b")
    
    
e = 10
f = 10
    
if e == f:
    pass