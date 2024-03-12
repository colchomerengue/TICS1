#kilos=int(input("¿Cúantos es la cantidad de kilos de emision que quieres evitar "))
#botellas=int(input("¿Cuántas botellas?"))
#if botellas/8 >= kilos  :
 #   print("GANASTE")

goal=int(input("Introduce los kg de CO2 que deseas reciclar:"))
print("Voy a reciclar",goal,"kgs")
botella=1
contador=1
totak=0
while (botella!=0):
    botella=int(input("Introduce el numero de botellas que has traído"))
    
    totak=totak+botella*0.125

    if totak >= goal:
        ganador=contador
    else:
        contador=contador+1


if totak >= goal:
    print("GANASTE")
else:
    print("SIGUE RECICLANDO")