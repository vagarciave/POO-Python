from Usuario import Usuario
from Item import Item
from datetime import date 

class Factura:
	COD = 1
	def __init__(self, Usuario, fecha = date.today(), listaItems = None, estado = "No aprobado"):
		self._codigo = Factura.COD
		self._fecha = fecha
		self._Usuario = Usuario
		self._listaItems = []
		self._estado = estado
		Factura.COD += 1 

	def getCodigo(self):
		return str(self._codigo)

	def getFecha(self):
		return self._fecha

	def setFecha(self, fecha):
		self._fecha = fecha

	def getUsuario(self):
		return self._Usuario

	def getItems(self):
		return self._listaItems

	def agregarItem(Item):
		self._listaItems.append(Item)

	def borrarItem(Item):
		self._listaItems.remove(Item)

	def pagarFactura(self):
		self._estado = "Aprobado"


	def toString(self):
		return ("Factura : { Nombre: " + self._Usuario.getNombre() + ", Documento: " +self._Usuario.getDocumento()
		+ ", Fecha: " + self.getFecha()+", Cuenta: " + self._Usuario.getCuenta() + " }" + "\n Items:" + "\n" + self.getItems())
	
		

