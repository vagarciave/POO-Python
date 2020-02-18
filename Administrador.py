from Usuario import Usuario

class Administrador(Usuario):
	def __init__(self, email,clave,cuenta,documento,nombre,celular,llave):
		super().__init__(email, clave,cuenta,documento,nombre, celular)
		self._llave = llave

	def getLlave():
		return self._llave

	@staticmethod
	def display_menu_admin():
		return (Mensajes.MensajesUsuario['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['ver'], 
		"\n 2." , Mensajes.MensajesEvento['consultaNombre'] ,"\n 3." , Mensajes.MensajesEvento['consultaCodigo'],
		"\n 4." , Mensajes.MensajesUsuario['verFacturas'],"\n 5." , Mensajes.MensajesUsuario['verDatos'],
		"\n 6." , Mensajes.MensajesUsuario['editarDatos'],"\n 7." ,Mensajes.MensajesOtros['regresar'])


