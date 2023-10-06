#Ej7

renta=float(input("Renta anual: "))
if renta<10000:
    print("Su impositivo es de un 5%.")
elif renta>=10000 and renta<20000:
    print("su impostivo es de un 15%")
elif renta>=20000 and renta<35000:
    print("Su impositivo es del 20%")
elif renta>=35000 and renta<=60000:
    print("Su impositivo es del 30%")
else:
    print("su impositivo es del 45%")