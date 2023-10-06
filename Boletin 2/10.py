#Ej10

print("hola")
veg=str(input("Pizza vegetariana, responde S/N"))
print("Solo puedes elegir un ingrediente")
if veg=="S":
    ingve=str(input("Elige Menu: pimiento o tofu"))
if veg=="S" and ingve=="tofu":
    print("Tu pizza lleva tofu tomate y mozzarella")
elif veg=="S" and ingve=="pimiento":
    print("Tu pizza lleva tomate mozzarella y pimiento")
if veg=="N":
    ingcar=str(input("Menu: peperoni, jamon y salmon"))
if veg=="N" and ingcar=="jamon":
    print("Tu pizza lleva tomate mozzarella y jamon")
elif veg=="N" and ingcar=="salmon":
    print("tu pizza lleva tomate mozzarella y salmon")
elif veg=="N" and ingcar=="Peperoni":
    print("Tu pizza lleva tomate mozzarella y peperoni")
