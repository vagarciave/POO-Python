
from Mensajes import Mensajes

class Usuario:

	def __init__(self,email, clave,cuenta,documento,nombre, celular):
		self._email = email
		self._clave = clave
		self._cuenta = cuenta
		self._documento= documento
		self._nombre = nombre       
		self._celular = celular
		self._facturas = []

	def getEmail(self):
		return self._email

	def setEmail(self,email):
		self._email = email

	def getClave(self):
		return self._clave

	def getCuenta(self):
		return self._cuenta
	
	def setCuenta(self,cuenta):
		self._cuenta = cuenta

	def getDocumento(self):
		return self._documento

	def setDocumento(self,documento):
		self._documento = documento

	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre = nombre

	def getCelular(self):
		return self._celular

	def setCelular(self,celular):
		self._celular = celular

	def getFacturas(self):
		return self._facturas

	def toString(self):
		return (" : { Email: " + self.getEmail() + ", Cuenta: " + self.getCuenta() +
		", Documento: "+ self.getDocumento() + ", " + ", Nombre: "  + self.getNombre() +
		", Celular: "+ self.getCelular()+ " }")

	@staticmethod
	def ConsultarUsuario(listaUsuarios,email):
		for usuario in listaUsuarios:
			if(usuario.getEmail() == email):
				return usuario
			else:
				return None
	
	@staticmethod
	def display_menu_usuario():
		return (Mensajes.MensajesUsuario['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['ver'], "\n 2." , Mensajes.MensajesEvento['consultaNombre'],
		"\n 3." , Mensajes.MensajesEvento['consultaCodigo'],"\n 4." , Mensajes.MensajesEvento['consultaCategoria'],"\n 5.", Mensajes.MensajesUsuario['verFacturas'],
		"\n 6." , Mensajes.MensajesUsuario['verDatos'],"\n 7." , Mensajes.MensajesUsuario['editarDatos'],"\n 8." ,Mensajes.MensajesOtros['regresar'])
