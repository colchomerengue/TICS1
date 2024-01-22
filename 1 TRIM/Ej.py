print("Hola buenos días, estas en el oculista")
op=str(input('por favo escoge : introduzca cita, leer libro de citas, borrar citas')).lower()
if(op=='introduzca una cita'):
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
    print('No existe el fichero')

elif(op=='leer libro de citas'):
  try:
      with  open("banco.csv", 'r') as f:
        print("aki")

  except FileNotFoundError:
    print('No existe el fichero')