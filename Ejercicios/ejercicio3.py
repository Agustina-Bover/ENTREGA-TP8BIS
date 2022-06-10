########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
lista=[]
contador=10
while contador>0:
    entrada=int(input('Ingrese un numero--> '))
    while entrada>-15 and entrada<50:
        lista.append(entrada)
        contador-=1
        break
    else:
        print('No valido, recuerde -15<nro<50')
suma=0
impares=0
negativos=0
for i in range (len(lista)):
    suma=suma+lista[i]
    if i%2!=0:
        impares=impares+lista[i]
    if lista[i]<0:
        negativos+=1
promedio=suma/10
porcentaje=(negativos*100)/10
print(lista)
print(f'La suma de los nros es:{suma}')
print(f'La suma de los nros impares es: {impares}')
print(f'El promedio de todos los nros es:{promedio}')
print(f'El porcentaje de nros negativos es: {porcentaje}%')
    