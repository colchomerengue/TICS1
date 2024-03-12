codigo=input("Introduce un código a TRADUCIR")
codigo="1ES270030085802"
codigo1=codigo[0]
codigo2=codigo[1:3]
codigo3=codigo[3:5]
codigo4=codigo[5:7]
codigo5=codigo[8:]
print(codigo1,codigo2,codigo3,codigo4,codigo5)

n1={'0':'Produccion ecológica','1':'Gallinas camperas', '2':'Gallinas creadas en el suelo','3': 'Gallinas ciradas en granja'}
n2={'ES':'España','DE':'Alemania','BE':'Bélgica', 'HR': 'Croacia', 'DK': 'Dinamarca', 'FR': 'Francia ', 'EL': 'Grecia', 'IE': 'Irlanda', 'IT': 'Italia'}
n3={'15':' A coruña','27':'Lugo','32':'Ourense','36':'Pontevedra'}
n4={'057':'Negreira'}
#print(n1[codigo.title()])

print(n1.get(codigo1))
print(n2.get(codigo2))

if codigo3.title() in n3:
    print(n3.get(codigo3))
else:
    print
elif codigo4.title() in n4:
    print(n4.get(codigo4))
else:
    print("NO ES DE LA NEGRE")
    