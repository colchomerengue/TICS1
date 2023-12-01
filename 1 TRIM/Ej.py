print("Hola buenos días, estas en el oculista")

f=open('banco csv', 'a')

dni=input("DIME TU DNI:")
mes=input("EL MES DE LA CITA:")
dia=input("EL DIA:")
hora=input("LA HORA")
especialidad=input("LA ESPECIALIDAD:")

f.write('DNI:' +dni+'\n'  + 'MES:' +mes +'\n' 'DIA:'+ dia+'\n'   'HORA:'+hora+'\n'  'ESPECIALIDAD:'+ especialidad+'\n')
f.read


f.close()