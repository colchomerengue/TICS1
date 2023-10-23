n=int(input("Introduzca un numero entero del 1 al 10"))
#Abrimos un fichero
f=open('prueba.txt', 'a')
f.write('Final')


for i in range(1,11):
    print(n, "x", i, "=", n*i)
f.close()