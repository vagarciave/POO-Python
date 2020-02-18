from Boleta import Boleta

class Evento():

	COD = 0

	def __init__(self,categoria,nombre,descripcion,lugar,fecha):
		self._categoria = categoria
		self._nombre = nombre
		self._descripcion = descripcion
		self._codigoEvento = Evento.COD
		self._lugar = lugar
		self._fecha = fecha
		self._ListaBoletas = []
		Evento.COD = Evento.COD+1


	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre = nombre

	def getDescripcion(self):
		return self._descripcion

	def setDescripcion(self,descripcion):
		self._descripcion = descripcion

	def getCodigoEvento(self):
		return self._codigoEvento

	def setCodigoEvento(self,codigoEvento):
		self._codigoEvento = codigoEvento

	def getCategoria(self):
		return self._categoria

	def setCategoria(self,categoria):
		self._categoria = categoria

	def getFecha(self):
		return self._fecha
		
	def setFecha(self,fecha):
		self._fecha = fecha

	def getLugar(self):
		return self._lugar

	def setLugar(self,nombre):
		self._lugar = lugar

	def boletasDisponibles(self):
		CantidadTotal = 0;
		for boleta in self._ListaBoletas:
			CantidadTotal += boleta.getCantidad()
		return CantidadTotal

	def InfoBoletas(self):
		Info = []
		for boleta in self._ListaBoletas:
			Info.append(boleta.toString() + "\n")
		return Info

	def toString(self):
		InfoEvento = " : { Categoria: " + self.getCategoria() + ", Nombre: " + self.getNombre() + ", Descripcion: " 
		+ self.getDescripcion() + ", " + ", Codigo: "  + self.getCodigoEvento() + ", Lugar: " + self.getLugar()
		+ ", Fecha: " + self.getFecha() + ", Boletas disponibles: }"
		InfoBoletas = self.InfoBoletas()
		return InfoEvento + InfoBoletas 

	def agregarBoletas(self,*args):
		for boleta in args:
			self._ListaBoletas.append(boleta)

	
	def consultarEventoCodigo(listaEventos, codigoEvento):
		for Evento in listaEventos:
			if Evento.getCodigoEvento() == codigoEvento:
				return Evento
		return None

	def consultarEventoNombre(listaEventos, nombre):
		for Evento in listaEventos:
			if Evento.getNombre() == nombre:
				return Evento
		return None

