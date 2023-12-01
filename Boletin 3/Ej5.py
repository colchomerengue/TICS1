cant = float(input("Escribe la cantidad a invertir:"))
interes = float(input("Escribe el interés anual:"))
años = int(input("Escribe el número de años:"))

if cant > 0 and interes > 0 and años >= 1:
    dinero = float(cant)
    for i in range(años):
        dinero_anterior=dinero
        dinero = float(cant * (1 + interes / 100))
        print(f'Año{ i } el dinero actual es {dinero} euros, has obtenido {dinero-dinero_anterior}euros')
    print(f'Acabaste con {dinero} euros, con {dinero-cant} euros de ganancias')
else:
    print("Error: datos introducidos incorrectos")