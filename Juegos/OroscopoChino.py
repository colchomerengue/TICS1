#Manera larga
print("Voy a calcular tu orroscopo chino")
ano=int(input("En que año naciste?"))
zodiaco=ano%12
if zodiaco==0:
    print("Tu signo es el mono")
elif zodiaco==1:
    print("Tu signo es el gallo")
elif zodiaco==2:
    print("Tu signo es el perro")
elif zodiaco==3:
    print("Tu signo es el cerdo")
elif zodiaco==4:
    print("Tu signo es la rata")
elif zodiaco==5:
    print("Tu signo es el buey")
elif zodiaco==6:
    print("Tu signo es el tigre")
elif zodiaco==7:
    print("Tu signo es el conejo")
elif zodiaco==8:
    print("Tu signo es el dragón")
elif zodiaco==9:
    print("Tu signo es la serpiente")
elif zodiaco==10:
    print("Tu signo es el caballo ")
elif zodiaco==11:
    print("Tu signo es la cabra")
else:
    print("Error")   

    #MAnera facil
ano=int(input("En que año naciste"))
signo=["Mono", "gallo", "perro", "cerdo", "rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "cabra"]
zodiaco=ano%12
print("Eres", signo[zodiaco])

