#Ej1
print("Hola mundo!")

#Ej2
variable=print("hola mundo")

#Ej3
nombre = input(print("Cual es tu nombre"))
print("hola", nombre)

#Ej4
print((3+2)/(2*5)**2)

#Ej5
n1 = float(input("Dime las horas que trabajas"))
n2 = float(input("tambien el coste por hora"))
result = n1*n2
print("Ganas", result)

#Ej6
n=int(input("dime u8n número entero positivo"))
print("voy a sumar todos los números desde 1 hasta tu número")
n2=n*(n+1)/2
print("Sería", n2)

#Ej7
peso=float(input("¿Cúanto pesas (kg)?"))
altura=float(input("¿Cúanto mides (m)?"))
print("voy a calcular tu IMC")
imc=float(peso/(altura**2))
print("TU índice de masa corporal es de", imc)

#Ej8
n1=int(input("Dame un número entero"))
n2=int(input("Dame otro"))
print("te voy a dar el cociente y el resto del primer número entre el segundo")
c=n1//n2
r=n1%n2
print("el resto es", r)
print("el cociente es", c)

#Ej9
d=float(input("¿Cuanto dinero quieres invertir?"))
i=float(input("Y el interés anual?"))
a=float(input("Y en cúantos años?"))
c=float(d*(i/100)*a)
print("El capital obtenido en la inversión es de", c)

#Ej10
muñeca=int(input("Número de muñecas enviados."))
payaso=int(input("Número de payasos enviados"))
result=112*payaso+75*muñeca
t=result/1000
print("El peso total en kg es de",t )


#Ej11
cc=float(input("Cuánto dinero quieres depositar?"))
f=cc+(4/100*cc)
z=f+(4/100*f)
x=z+(4/100*z)
print("El primer año tienes",f)
print("El segundo año tienes", z)
print("El tercer año tienes", x)

#Ej12
bar=int(input("¿Cúantas barras no del día has vendido?"))
ba=int(input("Cúantas barras del día has vendido?"))
print("Una barra del día cuesta 3,49 y sino es del día se aplica un 60% menos.")
ju=float(ba*3.49+(bar*3.49*(60/100)))
print("ganaste un total de",ju)
