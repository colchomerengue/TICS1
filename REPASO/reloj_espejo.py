import datetime
mihora=input("Introduce la hora en formato HH:MM ")
mihora=datetime.datetime.strptime(mihora, "%H:%M").time()
hora_esp=mihora
hora_esp=hora_esp.replace(60-(minute=28))
