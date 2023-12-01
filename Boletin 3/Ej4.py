n1=int(input('Escribe un numero entero positivo:'))


res=bool(True)
 
for i in range(0,n1):
    if not (n1-i-1)%2==0:
        
        
        if res==True:
            print(n1-i-1)
            
            
            res=bool(False)
        else:
            print(n1-i-1)