armario=input("Dime el contenido de tu armario.")

#print(armario)

armario_lista=armario.split()

#print("lista ->", armario_lista)
V=0
A=0
I=0
for ropa in armario_lista:
    print(ropa)

    if ropa=="V":
        V+=1
    elif ropa=="I":
        I+=1
    elif ropa=="A":
        A+=1

print(V, I, A)
if V>I and V>A:
    print("Verano")
elif I>A and I>V:
    print("Invierno")
elif A>I and A>V:
    print("Ambas")
else:
    print("Empate")
