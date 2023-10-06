#Ej8

punt=float(input("cual es tu puntuacion,0.0, 0.2, 0.4, 0.6 o mas?"))
pasta=punt*2400
if punt==0.0:
    print("tu nivel es inaceptable cobras",pasta, "€")
elif punt==0.4:
    print("Tu nivel es aceptable cobras",pasta, "€")
elif punt>=0.6:
    print("Tu nivel es Meritorio cobras",pasta, "€")