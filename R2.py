'''
Ingresa una tubla de tamaño 3, 
correspondiente a una fecha en formato (año,mes,día)
'''
def fecha_es_valida(fecha):
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
	#validar_numeros(fecha)


def validar_numeros(fecha):
	return

def esEnteroPositivo(fecha):
	res = False
	for n in fecha:
		if n > 0 and type(n) == int:
			res = True
		else:
			res = False
			break
	print (res)
	return res

#esEnteroPositivo((12,12,12))
#fecha_es_valida((554,12,12))