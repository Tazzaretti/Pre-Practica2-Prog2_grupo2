#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
a=int(input("Ingrese el valor del primer numero  "))
b=int(input("Ingrese el valor del segundo numero "))

try:
    c=a/b
    print(c)
except ZeroDivisionError as exception:
    print(f"No puede dividirse por cero | {exception}")



#FIN