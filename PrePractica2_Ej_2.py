#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
from socket import NI_NUMERICHOST


print("Ingrese 5 numeros")
lista1=[]
lista_impares=[]
i=0
while i<=4:
    numeros=int(input("ingrese un numero\n"))
    lista1.append(numeros)
    i+=1
print("\n")

for f in lista1:
    if f%2 !=0:
        lista_impares.append(f)

for n in lista_impares:
    print(n)



#FIN1