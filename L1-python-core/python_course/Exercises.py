# Ejercicio 1 de la clase

# x = 5
# if x > 5:
#     print("X es mayor que 5")
# elif x == 5:
#     print("X es igual a 5")
# else:
#     print("X es menor que 5")
# print("afuera")


# - Ejercicio 2 de la clase

# x = 15
# y = 20

# if x > 10 and y > 25:
#     print("x es mayor que 10 y Y es Mayor que 15")

# if x > 10 or y > 25:
#     print("x es mayor que 10 Ó Y es Mayor que 15")

# if not x > 10:
#     print("X no es mayor que 10")

# Ejercicio 3 de la clase

# is_member = True
# age = 11

# if is_member:
#     if age >= 15:
#         print("Tienes acceso ya que eres miembro y mayor o igual a 15 años.")
#     else:
#         print("No tienes acceso ya que eres miembro pero menor de 15 años.")
# else:
#     print("No eres miembro y NO TIENES ACCESO.")


input_player_1 = (
    input("Jugardor 1 ingrese su jugada (piedra, papel, o tijera)").lower().strip()
)
input_player_2 = (
    input("Jugardor 2 ingrese su jugada (piedra, papel, o tijera)").lower().strip()
)

if input_player_1 == input_player_2:
    print("Empate")
elif input_player_1 == "piedra" and input_player_2 == "papel":
    print("Gana Jugador 2")
elif input_player_1 == "papel" and input_player_2 == "tijera":
    print("Gana Jugador 2")
elif input_player_1 == "tijera" and input_player_2 == "piedra":
    print("Gana Jugador 2")
else:
    print("Gana Jugador 1")
