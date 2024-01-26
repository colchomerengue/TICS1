import datetime
myhora=input("Por favor introduce una hora(hh:mm)")
myhora=datetime.datetime.strptime(myhora, "%H:%M").time()
hora_espejo=myhora

if myhora.hour!=12:
    hora_espejo=hora_espejo.replace(hour=12-myhora.hour)
if myhora.minute!=0:
    hora_espejo=hora_espejo.replace(minute=60-myhora.minute)


if myhora.minute!=0 and myhora.minute<30:
    hora_espejo=hora_espejo.replace(hour=hora_espejo.hour-1)
    print(hora_espejo)    
else:
    print(hora_espejo)

