########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
########
#def decomponer():
def descomponer(numero):
    if len(numero)==5:
        unidad=numero[4]
        p_unidad='Unidades:'+unidad
        decena=numero[3]
        p_decena='Decenas:'+decena
        centena=numero[2]
        p_centena='Centenas:'+centena
        unidad_de_mil=numero[1]
        p_unidad_de_mil='Unidades de mil:'+unidad_de_mil
        decena_de_mil=numero[0]
        p_decena_de_mil='Decenas de mil:'+decena_de_mil
        return p_unidad,p_decena,p_centena,p_unidad_de_mil,p_decena_de_mil
    else:
        unidad=numero[3]
        p_unidad='Unidades:'+unidad
        decena=numero[2]
        p_decena='Decenas:'+decena
        centena=numero[1]
        p_centena='Centenas:'+centena
        unidad_de_mil=numero[0]
        p_unidad_de_mil='Unidades de mil:'+unidad_de_mil
        return p_unidad,p_decena,p_centena,p_unidad_de_mil
def es_capicua(numero):
    if numero==numero[::-1]:
        return True
    return False
        
def principal():
    numero=int(input('Ingresar un nro--> '))
    try:
        assert numero>999 and numero<99999
        numero=str(numero)
        print (numero)
        resultado=descomponer(numero)
        resultado2=(es_capicua(numero))
        print(resultado)
        print(f'Es capicua? {resultado2}')
    except:
        print('No valido, recuerde: 999<nro<99999')
        principal()

if __name__ =='__main__':
    principal()