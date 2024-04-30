archivo = open("data/atp_tennis.csv","r")
lineas = archivo.readlines()
lineas= [l.split("|") for l in lineas]
#Contador para los nombres unicos
contador = 1
for x in lineas:
	cadena ="""<b>Torneo:</b> %s<br> <b>Ganador: </b>%s""" % (x[0],x[9])
	# print(cadena)
	# genera un nombre unico de archico con el contador
	nombre_archivo = "data/%s_%d.html"% (x[9],contador)
	# va aumentando el contador para el proximo archivo
	contador += 1 
	# Escribir el contenido en el archivo
	archivo_generado = open(nombre_archivo,"w")
	archivo_generado.writelines("%s\n"%(cadena))
	archivo_generado.close()
	
	#salir los 25 362 archivos con nombres unicos 