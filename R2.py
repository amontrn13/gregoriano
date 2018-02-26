
'''
Ingresa una tupla válida con la fecha,
se reviza que sus número sean enteros positivos.

La salida es True o False.
'''
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
Requerimiento R2:
Ingresa una tubla de tamaño 3, 
correspondiente a una fecha en formato (año,mes,día).
'''
def fecha_es_valida(fecha):
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
Los años bisiestos son aquellos multiplos de 4,
excepto aquellos múltiplos de 100, pero no de 400.

La entrada es el año en formato YYYY válido.
La salida es True o False.
'''
def esBisiesto(anio):
	res = False
	if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
		res = True
	else:
		res = False
	return res


#esEnteroPositivo((12,12,12))
fecha_es_valida((2018,2,29)) 
#PROBAR CON MÁS NÚMEROS EN LA TUPLA.
#esBisiesto(2016)
