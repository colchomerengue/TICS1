#Ej6
nombre=input("¿Cómo te llamas?").lower()
sexo=input("¿eres mujer? s/n").lower()
if (nombre<"m" and sexo=="s") or (nombre>"n" and sexo=="n"):
    print("EStas en el grupo A")
elif ( nombre>"n" and sexo=="s") or (nombre <"m" and sexo=="n"):
    print("EStas en el grupo b")