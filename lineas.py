


""" 
UNIVERSIDAD NACIONAL DE SAN AGUSTIN DE AREQUIPA
Curso:Computacion 1
Ing:Ramiro Banda Valdivia
Estudiantes: George Daniel Machacca Catari
             Fernando Jesús Miranda Apaza
"""
a=float(input("Ingrese el valor de (a):\n"))
b=float(input("Ingrese el valor de (b):\n"))
c=float(input("Ingrese el valor de (c):\n"))
disc=((b**2)-(4*a*c))
raiz=(disc)**(0.5)

if(disc>0):
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("X1= ",x1)
    print("X2= ",x2)
elif(disc==0):
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("X1= ",x1)
    print("X2= ",x2)
    
  
