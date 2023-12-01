import random

# Calcular número a adivinar
aleatorio = random.randint(1, 10)
# print(aleatorio)

print("Hola buenas!")
nombre = input("¿Cómo te llamas")
print("hola", nombre)

pregunta = input("Quieres jugar a un juego S/N")

if pregunta == "N":
    print("Ah valeee chaoo")
if pregunta == "S":
    print("Estoy pensando un número ........ entre el 1 y el 10")
    numUsuario = int(input("Intenta  adivinarlo:"))
if numUsuario > aleatorio:
    print("mas pequeño")
if numUsuario < aleatorio:
    print("Más grande")
while numUsuario != aleatorio:
    if numUsuario > aleatorio:
        print("mas pequeño")
if numUsuario < aleatorio:
    print("Más grande")
while numUsuario != aleatorio:
    numUsuario = int(input("Intentalo de nuevo:"))
if numUsuario == aleatorio:
    print("Ganaste")
