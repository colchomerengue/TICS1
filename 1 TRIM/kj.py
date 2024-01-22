print("Hola buenos días, estas en el oculista")
fichero="banco.csv"
#Solicitamos datos para el fichero

dni=input("DIME TU DNI:")
mes=input("EL MES DE LA CITA:")
dia=input("EL DIA:")
hora=input("LA HORA")
especialidad=input("LA ESPECIALIDAD:")

#Manipulamos el fichero. Abrimos, escribimos y cerramos
try:
      with  open("banco.csv", 'a+') as f:
        f.write( dni+ ';'    + mes +';'+ dia+';'   +hora+';'  + especialidad+'\n')

except FileNotFoundError:
    print('No existe el fichero', n)

   