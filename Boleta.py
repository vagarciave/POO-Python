class Boleta:

	def __init__(self, cantidad, precio, Evento, localidad = 'Unica'):
		self._localidad = localidad
		self._cantidad = cantidad
		self._precio = precio
		self._Evento = Evento

	def getCantidad(self):
		return self._cantidad

	def setCantidad(cantidad):
		self._cantidad = cantidad

	def getPrecio(self):
		return self._precio

	def setPrecio(precio):
		self._precio = precio

	def getLocalidad(self):
		return self._localidad

	def setLocalidad(localidad):
		self._localidad = localidad

	def toString(self):
		return( ":{ localidad: " + self.getLocalidad() + ", Precio: " + self.getPrecio() 
		+ " ,Cantidad: " + str(self.getCantidad()) + "}")

