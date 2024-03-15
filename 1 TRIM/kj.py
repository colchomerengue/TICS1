def leer(nombre):
    try:
        f=open(nombre, 'r')
    except FileNotFoundError:
        print('no existe el fichero')
    else:
        print(f.read())
        f.close()
    return


def escribir(nombre):
   #toma de datos  
    dni= input("Introduzca su dni:")
    mes= input("Introduzca el mes :")
    dia= input("Introduzca el dia:")
    hora= input("Introduzca la hora:")
    especialidad= input("Introduzca la especialidad:")
    #escribir en fichero
    citas=open(nombre, 'a+')
    citas.write(dni + ";" + mes + ";"+ dia + ";" + hora + ";"+ especialidad + "\n")
    citas.close
    return



def menu():
    print("============================")
    print("Aplicacion Banco de Negreira")
    print("============================")
    print("1 - Consultar Citas")
    print("2 - Añadir cita nueva")
    print("3 - Buscar una Cita")
    print("4 - Eliminar Citas")
    print("0-Sair")
    op=input("Introduzca a opcion dexexada")
    return op
  
def xestion():
  
  fichero="banco.csv"
  while True:
    opcion=menu()
    if opcion == '1':
      leer(fichero)
    elif opcion == '2':
      escribir(fichero)
    else:
      break
  return


xestion()




   