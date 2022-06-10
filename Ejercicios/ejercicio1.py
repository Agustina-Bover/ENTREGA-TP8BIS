########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
'''
Determinar e imprimir la cantidad de elementos positivos, la de negativos y
la de ceros, de un vector V de N elementos enteros, con un diagrama de
flujo de datos.
'''
lista=[]
contador=int(input("Cuantos numeros quiere ingresar? --> "))
positivos=0
negativos=0
ceros=0
while contador>0:
    entrada=int(input("Ingresar un numero--> "))
    lista.append(entrada)
    contador-=1
for i in range (len(lista)):
    if lista[i]==0:
        ceros+=1
    elif lista[i]>0:
        positivos+=1
    else:
        negativos+=1

print(f"La cantidad de numeros positivos es: {positivos}\nLa cantidad de numeros negativos es: {negativos}\nLa cantidad de ceros es: {ceros}")
