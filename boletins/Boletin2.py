#Ej1

años=int(input("¿Cúantos años tienes"))
if años>=18:
    print("eres mayor de edad")
else:
    print("eres menor")
    
#Ej2

Pass="Pepe777".upper()

cont=1

nombre=input("Escriba la contraseña")

while Pass!=nombre.upper():

          nombre=input("incorrececta, intentelo de nuevo") 

print("acceso conseguido")

#Ej3

n1=int(input("DIME UN NUMERO ENTERO"))
n2=int(input("OTRO NÚMERO"))
z=n1/n2
print("AL dividir en primer número con el segundo da",z)
s=n1%n2
if s==0:
    print("ERROR, porque el resto es 0")
else:
     print("Su resto es ",s)
     
     #Ej4
     
print("SABER SI ES PAR O IMPAR")
c=int(input("Dime un número entero"))
if c%2==0:
    print(c,"es par")
else:
    print(c,"es impar")

#Ej5

año=int(input("¿Cúantos años tienes?"))
if año>=16 :
    print("si que tributas")
else print("no tributas")


#Ej6
nombre=input("¿Cómo te llamas?").lower()
sexo=input("¿eres mujer? s/n").lower()
if (nombre<"m" and sexo=="s") or (nombre>"n" and sexo=="n"):
    print("EStas en el grupo A")
elif ( nombre>"n" and sexo=="s") or (nombre <"m" and sexo=="n"):
    print("EStas en el grupo b")

#Ej7






