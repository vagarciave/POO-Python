class Menu:

	@staticmethod
	def display_menu_principal():
		return ("Menu:", "\n 1.", Mensajes.MensajesUsuario['ingresar'] , "\n 2." , Mensajes.mensajesAdministrador['ingresar'] ,
		"\n 3." , Mensajes.MensajesOtros['ingresar'],"\n 5." , Mensajes.mensajesOtros['menu'])

	@staticmethod
	def display_menu_invitado():
		retunr ("Menu invitado" + "\n 1.", Mensajes.MensajesEvento['ver'], "\n 2." , Mensajes.MensajesEvento['consultaNombre'],
		"\n 3." , Mensajes.MensajesEvento['consultaCodigo'])

	@staticmethod
    def display_menu_usuario():
    	return (Mensajes.MensajesUsuario['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['ver'], 
    	"\n 2." , Mensajes.MensajesEvento['consultaNombre'] ,"\n 3." , Mensajes.MensajesEvento['consultaCodigo'],
    	"\n 4." , Mensajes.MensajesUsuario['verFacturas'],"\n 5." , Mensajes.MensajesUsuario['verDatos'],
    	"\n 6." , Mensajes.MensajesUsuario['editarDatos'],"\n 7." ,Mensajes.MensajesOtros['regresar'])

    @staticmethod
    def display_menu_admin():
    	return (Mensajes.MensajesUsuario['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['ver'], 
    	"\n 2." , Mensajes.MensajesEvento['consultaNombre'] ,"\n 3." , Mensajes.MensajesEvento['consultaCodigo'],
    	"\n 4." , Mensajes.MensajesUsuario['verFacturas'],"\n 5." , Mensajes.MensajesUsuario['verDatos'],
    	"\n 6." , Mensajes.MensajesUsuario['editarDatos'],"\n 7." ,Mensajes.MensajesOtros['regresar'])

