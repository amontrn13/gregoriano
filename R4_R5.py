def esBisiesto(anio):
	res = False
	if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
		res = True
	else:
		res = False
	return res

def esEnteroPositivo(fecha):
	res = False
	for n in fecha:
		if n > 0 and type(n) == int:
			res = True
		else:
			res = False
			break
	return res

'''
Ingresa una tubla de tamaño 3, 
correspondiente a una fecha en formato (año,mes,día).
La salida es True o False.
'''
def fecha_es_valida(fecha):
	#listas de número de mes correspondiente a la cantidad de días que tienen.
	meses31Dias = (1, 3, 5, 7, 8, 10, 12)
	meses30Dias = (4, 6, 9, 11)
	#Validaciones de tipo y formato de la fecha.
	if type(fecha) != tuple :
		print ("Error: La fecha no corresponde a una tupla. -> ().")
		return False
	elif len(fecha) != 3:
		print ("Error: La tupla de la fecha debe ser de 3 campos. -> (,,,).")
		return False
	try:
		if esEnteroPositivo(fecha) != True:
			print ("Error: La fecha debe de estar compuesta por números enteros positivos. -> 1,2,...,Inf.")
			return False
	except:
		print ("Error: La fecha debe de estar compuesta por números enteros positivos. -> 1,2,...,Inf.")
		return False

	#Validaciones de mes y día.
	if fecha[1] > 12: 
		print ("Error: El mes debe ser un número en un rango de 1 a 12 y el día en un rango de 1 a 31.")
		return False
	elif fecha[2] > 31:
		print ("Error: El día en un rango de 1 a 31.")
		return False
	else:
		#Se valida el día con respecto al mes.
		#Se valida la fecha primero para Febrero.
		if fecha[1] == 2:
			if esBisiesto(fecha[0]) == True:
				if fecha[2] > 29:
					print ("Error: Febrero no tiene más de 29 días en año bisiesto.")
					return False
				else:
					return True
			else:
				if fecha[2] > 28:
					print ("Error: Febrero no tiene más de 28 días en un año no bisiesto.")
					return False
				else:
					return True
		#Validaciones de fecha en meses con 31 días.
		elif fecha[1] in meses31Dias:
			if fecha[2] > 31:
				print ("Error: Excede la cantidad de días del mes. Este Mes no tiene más de 31 días.")
				return False
			else:
				return True
		#Validaciones de fecha en meses con 31 días.		
		elif fecha[1] in meses30Dias:
			if fecha[2] > 30:
				print ("Error: Excede la cantidad de días del mes. Este Mes no tiene más de 30 días.")
				return False
			else:
				return True


'''
R4: (días_desde_primero_enero): Dada una fecha válida, determinar el número de días
transcurridos desde el primero de enero de su año (el número de días transcurridos
entre el primero de enero y el primero de enero, dentro de un mismo año, es 0). El
resultado debe ser un número entero.

Ingresa el año, mes y día para saber la cantidad de días
correspondientes a partir del primero de enero de ese mismo año.

La salida es la cantidad de días a partir del primero de enero.

'''

def días_desde_primero_enero(anio,mes,dia):
    if(fecha_es_valida((anio,mes,dia))):
        #listas de número de mes correspondiente a la cantidad de días que tienen.
        meses31Dias = (1, 3, 5, 7, 8, 10, 12)
        meses30Dias = (4, 6, 9, 11)
        #Valida si es bisiesto.
        bisiesto = esBisiesto(anio)
        #Variables para resultado final.
        cantidadDeDias = -1
        mesActual = 1
        mesesAnteriores = mes-1
        
        while(mesActual <= mesesAnteriores):
            #Validar meses de 31 días.
            if(mesActual in meses31Dias):
                cantidadDeDias += 31
            #Validar meses de 30 días.
            elif(mesActual in meses30Dias):
                cantidadDeDias += 30
            #Validar si es bisiesto.
            elif(mesActual == 2 and bisiesto):
                cantidadDeDias += 29
            else:
                cantidadDeDias += 28
            #Pasa al siguiente mes.
            mesActual += 1
            
        #Suma la cantidad de días restantes.
        cantidadDeDias += dia
        return cantidadDeDias

'''
R5; (dia_primero_enero): Dado un año perteneciente al rango permitido, determinar el
día de la semana que le corresponde, con la siguiente codificación: 0 = domingo, 1 =
lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe
ser un número entero, conforme a la codificación indicada.

Ingresa el año a saber el día correpondiente,
el valor debe ser entre 1700 y 2299.

La salida es un número entero, conforme a la siguiente codificación:

0 = Domingo
1 = Lunes
2 = Martes
3 = Miércoles
4 = Jueves
5 = Viernes
6 = Sábado
'''

def dia_primero_enero(anio):
    if( 1700 > anio or anio > 2299):
        print("El año debe ser entre 1700 y 2299")
    else:
        #Variable según el siglo que corresponda la fecha.
        siglo = 0
        
        #Asigna un valor según al siglo que pertenezca.
        if(1700 <= anio <= 1799):
            siglo = 5
        elif(1800 <= anio <= 1899):
            siglo = 3
        elif(1900 <= anio <= 1999):
            siglo = 1
        elif(2100 <= anio <= 2199):
            siglo = -2
        elif(2200 <= anio <= 2299):
            siglo = -4

        #Valor obtenido al sumar los últimos dos dígitos del año y sumarle la cuarta parte.
        valor = anio%100 + (anio%100)//4
        #Variables si es bisiesto y el mes y día del día correspondiente a averiguar. 
        bisiesto = 0
        mes = 6
        dia = 1

        #Valida si es bisiesto.
        if(esBisiesto(anio)):
            bisiesto = -1
        #Retorna el número del día
        return (siglo + valor + bisiesto + mes + dia)%7



#Pruebas

#días_desde_primero_enero(2017,1,1)
#días_desde_primero_enero(2018,5,30)
#días_desde_primero_enero(2018,12,31)
#días_desde_primero_enero(2016,12,31)

#dia_primero_enero(1876)
#dia_primero_enero(2012)
#dia_primero_enero(1993)
#dia_primero_enero(2138)
