retazos = [0.8, 3.5, 1.2, 4.0, 0.5, 2.1, 0.9, 3.0]

descartados = []
sillas = []
sofás = []

for retazo in retazos:
    if retazo < 1.0:
        descartados.append(retazo)
        print(f"Retazo de {retazo} metros descartado por ser muy pequeño.")
    elif retazo >= 1.0 and retazo < 3.0:
        sillas.append(retazo)
        print(f"El retazo de {retazo} metros sirve para una silla")
    else:
        print(f"Retazo de {retazo} metros sirve para un sofá.")
        sofás.append(retazo)

print(f"Retazos descartados: {len(descartados)}")
print(f"Retazos para sillas: {len(sillas)}")
print(f"Retazos para sofás: {len(sofás)}")
# Ejercicio 1 de la clase
