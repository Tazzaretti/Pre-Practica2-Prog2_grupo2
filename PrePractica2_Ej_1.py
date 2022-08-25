#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
from re import A


a=int(input("Elija el primer valor  "))
b=int(input("Elija el segundo valor "))

print(max(a,b))

if a>b:
    print("El primero numero es mayor")
elif b==a:
    print("Los numeros son iguales")
else:
    print("El segundo numero es mayor")

#FIN