import datetime 

#ejemplo de fecha completa
fecha=datetime.date.today()
print(fecha)
#ejemplo    
hora=datetime.time(10,30)
print(hora.hour)
print(hora.minute)


#print(type(hora)
hora=hora.replace(minute=28)
#print

date_time_str= "08:20"
date_time_object=datetime.datetime.strptime(date_time_str, "%H:%M")
print(date_time_str)
print(date_time_object)