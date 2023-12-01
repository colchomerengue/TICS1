# Creditos a mateo glez que me ayudó a hacer este
print("Holaa")
nEntero = int(input("Escribe un numero entero positivo:"))
if nEntero >= 0:
    res = bool(True)
    for i in range(nEntero):
        if not i % 2 == 0:
            if res == True:
                print(i)
                res = bool(False)
            else:
                print(f"{i}")
else:
    print("Error: datos introducidos incorrectos")
