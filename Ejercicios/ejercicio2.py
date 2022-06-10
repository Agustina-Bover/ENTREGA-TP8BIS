########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
lista=[]
negativo=0
contador=int(input('Cuantos numeros desea ingresar? -->'))
while contador<8 or contador>40:
    contador=int(input('Reingresar numero\nRecuerde que 8<nro<40\n-->'))
while contador>0:
    entrada=int(input('Ingresar un numero --> '))
    lista.append(entrada)
    contador-=1
for i in range(len(lista)):
    if lista[i]<0:
        negativo=i
    
print (f'La posicion del ultimo numero negativo es: {negativo}')
    
    
