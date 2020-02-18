from  Boleta  import Boleta
class Item:

	def __init__(self, Boleta, cantidadItems):
		self._Boleta = Boleta
		self._cantidadItems = cantidadItems
		
	def subTotal(self):
		subTotal = self._Boleta.getPrecio() * self._cantidadItems
		return subTotal

	def getCantidadItems(self):
		return self._cantidadItems

	def setCantidadItems(cantidadItems):
		self._cantidadItems = cantidadItems

	def toString(self):
		return (" : { Localidad: " + self._Boleta.getLocalidad() + ", cantidadItems: " + self.getCantidadItems() + ", subTotal: " + self.subTotal() + " }")