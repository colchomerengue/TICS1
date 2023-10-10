print("Comprueba si una palabra es un palíndromo")
palabra=input("Dime una palabra")
reves=""

#print(len(palabra))
for i in range(len(palabra),0,-1):
    print(palabra[i-1])
    reves=reves+palabra[i-1]
print(reves)
if palabra==reves:
    print("es palindromo")
else:
    print("No es palíndromo")


