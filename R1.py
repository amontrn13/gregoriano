#Analiza si un año es bisiesto o no.

"""
Controler
"""
def controler(anio):
    #Entradas:recibe el anio
    #Salidas:
    #Descripcion:funcion controler
    if(anioValido(anio)):
        if(esBisiesto(anio)):
            mostrarMensaje("El anio es bisiesto")
        else:
            mostrarMensaje("El anio no es bisiesto")
    else:
        mostrarMensaje("El anio ingresado es invalido")
    

def anioValido(anio):
    #Entradas:recibe el anio
    #Salidas:valor booleano
    #Descripcion:indica si el anio es valido o no para someterse al analisis
    if(isinstance(anio,int) and anio >= 0):
        return True
    else:
        return False
    
"""
Model
"""
def esBisiesto(anio):
    #Entradas:recibe el anio
    #Salidas:valor booleano
    #Descripcion: indica si el anio es bisiesto o no
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

"""
View
"""
def mostrarMensaje(mensaje):
    #Entradas:un string
    #Salidas:imprime en consola
    #Descripcion:imprime el mensaje
    print(mensaje)

def bisiesto(anio):
    #Entradas:recibe un anio
    #Salidas:
    #Descripcion:interfaz que recibe el anio del usuario
    controler(anio)
