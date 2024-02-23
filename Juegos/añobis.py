anho=int(input("introduce un año"))

if anho % 400==0 and anho % 100!=0  or anho % 4==0 and anho % 100!=0: 
    print("es bisiesto")

else:
    print("No es bisiesto")
    