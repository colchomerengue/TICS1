n1=int(input("POr favor introduzca un número"))
n2=int(input("POr favor introduzca un número"))
n3=int(input("POr favor introduzca un número"))




if n1<0 or n2<0 or n3<0:
    print("Error")
else:
    if n1>n2 and n2>n3:
        print(n1, ">", n2, ">" , n3)
    elif n1>n3 and n3>n2:
        print(n1, ">", n3, ">" , n2)
    elif n2>n1 and n1>n3:
        print(n2, ">", n1, ">" , n3)
    elif n2>n3 and n3>n1:
        print(n2, ">", n3, ">" , n1)
    elif n3>n2 and n2>n1:
        print(n3, ">", n2, ">" , n1)
    elif n3>n1 and n1>n2:
        print(n3, ">", n1, ">" , n2)
    elif n1==n2==n3:
        print(n1, "=", n2, "=" , n3)
    
    

       
        