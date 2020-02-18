class ManejoArchivo(object):

	@staticmethod
	def Leer(NombreArchivo):
		archivivo = open(NombreArchivo,'r')
		Resultados = []
		for linea in archivo.readLines():
			if(linea != ""):
				Resultados.append(eval(linea))
		archivo.close()
		return Resultados

	@staticmethod
	def Escribir(NombreArchivo,*args):
		archivo = open(NombreArchivo,'a')
		linea="["
		i = 0
		for texto in args:
			if(i!=len(args)-1):
				linea+= "'"+texto+"',"
			else:
				linea+= "'"+texto+"']\n"
			i+=1
		archivo.write(linea)
		archivo.close()

	@staticmethod
	def Borrar(NombreArchivo,dato):
		f = open(NombreArchivo,'r')
		lineas = f.readLines()
		f.close()
		f = open(NombreArchivo, 'w')
		for linea in lineas:
			if(dato not in linea):
				f.write(linea)
		f.close()
		