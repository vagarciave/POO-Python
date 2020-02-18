import sys
from Usuario import Usuario
from Administrador import Administrador
from Evento import Evento
from Boleta import Boleta
from Item import Item
from Factura import Factura
from Mensajes import Mensajes

class Main:
#Listas de objetos de las clases
	ListaUsuarios = []
	ListaAdministradores =[]
	ListaFacturas = []
	ListaEventos = []
	EventoConcierto = []
	EventoDeporte = []
	EventoTeatro = []
	EventoFestival = []
	UsuarioEnLinea = None

#Inicializador de opciones
def __init__(self):
	self.break_while = 1
	self.opcionesUsuario = {
	'1': self.VerEventos,
	'2': self.ConsultaEventoNombre,
	'3': self.ConsultaEventoCodigo,
	'4': self.ConsultaEventoCategoria,
	'5': self.VerMisFacturas,
	'6': self.VerMisDatos,
	'7': self.EditarMisDatos,
	#la opcion de regresar sería en el run,mostrar nuevamente el menu
	}

	self.opcionesAdministrador = {
	'1': self.RegistrarEvento,
	'2': self.EditarEvento,
	'3': self.VerEventos,
	'4': self.ConsultaEventoNombre,
	'5': self.ConsultarEventoCodigo,
	'6': self.ConsultaEventoCategoria,
	'7': self.VerUsuarios,

	}

	self.opcionesInvitado = {
	'1': self.VerEventos,
	'2': self.ConsultaEventoNombre,
	'3': self.ConsultaEventoCodigo,
	'4': self.ConsultaEventoCategoria,
	}

#-----------------------------------------------------Menú principal---------------------------------------------------------------
	def display_menu(self):
		print("Menu:", "\n 1.", Mensajes.MensajesUsuario['ingresar'] , "\n 2." , Mensajes.mensajesAdministrador['ingresar'] ,
		"\n 3." , Mensajes.MensajesOtros['ingresar'],"\n 4." , Mensajes.mensajesOtros['menu'])

	def display_menu_invitado(self):
		print("\n 1.", Mensajes.MensajesEvento['ver'], "\n 2." , Mensajes.MensajesEvento['consultaNombre'],
		"\n 3." , Mensajes.MensajesEvento['consultaCodigo'])

#-----------------------------------------------------Funciones Usuario------------------------------------------------------------ 
	
	def LoginUsuario(self,email,clave):
		for usuario in Main.listaUsuarios:
			if(usuario.getEmail()== email and usuario.getClave() == clave):     
				return usuario
			else:
				return None

	def RegistrarUsuario(self):
		email = input(Mensajes.MensajesUsuario['ingreseEmail'])
		clave = input(Mensajes.MensajesUsuario['ingreseClave'])
		cuenta = input(Mensajes.MensajesUsuario['ingreseCuenta'])
		documento = input(Mensajes.mensajesUsuario['ingreseDocumento'])
		nombre = input(Mensajes.mensajesUsuario['ingreseNombre'])   
		celular = input(Mensajes.mensajesEstudiante['ingreseCelular'])      
		UsuarioConsultado = Usuario.ConsultarUsuario(Main.ListaUsuarios, email)
		if(not Main.existenciaDato(UsuarioConsultado)):
			NuevoUsuario = Usuario(email,clave,cuenta,documento,nombre,celular)
			ManejoArchivos.escribir("Usuarios.txt",email,clave,cuenta,documento,nombre,celular)
			Main.listaUsuarios.append(NuevoUsuario)
			print(Mensajes.MensajesOtros['operacionExitosa'])
		else:
			print(Mensajes.MensajesOtros['UsuarioExistente'])

	def VerFacturas(self):
		if(Main.UsuarioEnLinea != None):
			Facturas = Main.UsuarioEnLinea.getFacturas()
			for Factura in Facturas:
				print("\n" + Factura.toString())
		else:
			print(Mensajes.MensajesOtros['noLogin'])

	def VerMisDatos(self):
		if(Main.UsuarioEnLinea != None):
			print("\n" + Main.UsuarioEnlinea.toString())
		else:
			print(Mensajes.MensajesOtros['noLogin'])

	def EditarMisDatos(self):
		pass


#-----------------------------------------------------Funciones Administrador----------------------------------------------------
	def RegistrarEvento():
		categoria = Main.ObtenerCategoria(input(Mensajes.MensajesEvento['ingreseCategoria']))
		nombre = input(Mensajes.MensajesEvento['ingreseNombre'])
		descripcion = input(Mensajes.MensajesEvento['ingreseDescripcion'])
		lugar = input(Mensajes.MensajesEvento['ingreseLugar'])
		fecha = input(Mensajes.MensajesEvento['ingreseFecha'])
		EventoConsultado = Evento.ConsultarEventoCodigo(Main.listaEventos, nombre)
		if(not Main.existenciaDato(EventoConsultado)):
			NuevoEvento = Evento(categoria,nombre,descripcion,lugar,fecha)
			VerificarLocalidad = input(Mensajes.MensajesEvento['localidad'])
			if(not eval(VerificarLocalidad)):
				precio = input(Mensajes.MensajesEvento['ingresePrecio'])
				cantidad = input(Mensajes.MensajesEvento['ingreseCantidad'])
				boleta = Boleta(cantidad,precio, NuevoEvento)
				NuevoEvento.agregarBoletas(boleta)
			else:
				PrecioBoletaPlatino = input(Mensajes.MensajesEvento['ingresePrecio'])
				CantidadBoletaPlatino = input(Mensajes.MensajesEvento['PrecioPlatino'])
				BoletaPlatino = Boleta(CantidadBoletaPlatino,PrecioBoletaPlatino,NuevoEvento,'Platino')
				PrecioBoletaVIP = input(Mensajes.MensajesEvento['ingresePrecio'])
				CantidadBoletaVIP = input(Mensajes.MensajesEvento['PrecioVIP'])
				BoletaVIP = Boleta(CantidadBoletaVIP,PrecioBoletaVIP,NuevoEvento,'VIP')
				PrecioBoletaPreferencia = input(Mensajes.MensajesEvento['ingresePrecio'])
				CantidadBoletaPreferencia = input(Mensajes.MensajesEvento['PrecioPreferencia'])
				BoletaPreferencia = Boleta(CantidadBoletaPreferencia,PrecioBoletaPreferencia,NuevoEvento,'Preferencia')
				NuevoEvento.agregarBoletas(BoletaPlatino,BoletaVIP,BoletaPreferencia)
		Main.listaEventos.append(NuevoEvento)
		Main.clasificarCategoria(NuevoEvento)
		if(Main.existenciaDato(EventoConsultado)):
			print(Mensajes.MensajesEvento['EventoExistente'])

	def VerUsuarios(self):
		for usuario in Main.listaUsuarios:
			print("\n" + Usuario.toString())
 
#-----------------------------------------------------Funciones Evento-----------------------------------------------------------
	@staticmethod
	def ObtenerCategoria(categoria):
		if(categoria == 1):
			return Concierto
		elif(categoria == 2):
			return Deporte
		elif(categoria == 3):
			return Teatro
		elif(catgoria == 4):
			return Festival

	@staticmethod
	def VerificarLocalidad(localidad):
		if(localidad == 1):
			return True
		else:
			return False

	@staticmethod
	def clasificarCategoria(Evento):
		if(Evento.getCategoria == Concierto):
			Main.EventoConcierto.append(Evento)
		elif(Evento.getCategoria == Deporte):
			Main.EventoDeporte.append(Evento)
		elif(Evento.getCategoria == Teatro):
			Main.EventoTeatro.append(Evento)
		elif(Evento.getCategoria == Festival):
			Main.EventoFestival.append(Evento)

	@staticmethod
	def VerEventos(listaEventos = Main.listaEventos):
		for Evento in listaEventos:
			print("\n" + Evento.toString())

	def ConsultaEventoNombre(self):
		nombreConsulta = input(Mensajes.MensajesEvento['ingreseNombre'])
		EventoConsulta = Evento.ConsultarEventoNombre(Main.listaEventos,nombreConsulta)
		if(Main.existenciaDato(EventoConsulta)):
			print(EventoConsulta.toString())
		else:
			print(Mensajes.MensajesOtros['noExiste'])

	def ConsultaEventoCodigo(self):
		codigoConsulta = input(Mensajes.MensajesEvento['ingreseCodigo'])
		EventoConsulta = Evento.ConsultarEventoCodigo(Main.listaEventos,codigoConsulta)
		if(Main.existenciaDato(EventoConsulta)):
			print(EventoConsulta.toString())
		else:
			print(Mensajes.MensajesOtros['noExiste'])

	def ConsultaEventoCategoria(self):
		Categoria = Main.ObtenerCategoria(input(Mensajes.MensajesEvento['ingreseCategoria']))
		if(Categoria == Concierto):
			Main.VerEventos(Main.EventoConcierto)
		elif(Categoria == Teatro):
			Main.VerEventos(Main.EventoTeatro)
		elif(Categoria == Deporte):
			Main.VerEventos(Main.EventoDeporte)
		elif(Categoria == Festival):
			Main.VerEventos(Main.EventoConcierto)

#-----------------------------------------------------Datos ficticios------------------------------------------------------------
	@staticmethod
	def CargarUsuarios(NombreArchivo):
		archivo = open(NombreArchivo)
		for linea in archivo.readlines():
			if(linea != ""):
				datos = eval(linea)
				email = datos[0]
				clave = datos[1]
				cuenta = datos[2]
				documento = datos[3]
				nombre = datos[4]
				celular = datos[5]
				CargaUsuario = Usuario(email,clave,cuenta,documento,
										nombre,celular)
				Main.ListaUsuarios.append(CargaUsuario)
			else:
				break
		archivo.close()

	def CrearDatosFicticios(self):
		#Cargar Base de datos usuarios
		Main.CargarUsuarios("Usuarios.txt")
		#Crear datos ficticios para administradores
		Admin1 = Administrador("admin1@evento.com","2468","1234456789","1143678903","Pepe","3008889977","master1")
		Admin1 = Administrador("admin2@evento.com","2469","1234456780","1143678904","Francisco","3008889978","master1")
		Main.ListaAdministradores.append(Admin1)
		Main.ListaAdministradores.append(Admin2)
		#Crear eventos ficticios
		#1
		ConciertoGuns = Evento("Concierto","Guns n' roses","Concierto de despedida Guns n' roses","Medellin","2017-12-24")
		BoletaGuns = Boleta(50000,520000, ConciertoGuns)
		ConciertoGuns.agregarBoletas(BoletaGuns)
		Main.ListaEventos.append(ConciertoGuns)
		Main.EventoConcierto.append(ConciertoGuns)
		#2
		PartidoBR = Evento("Deporte","Barcelona vs Real Madrid","Superclásico de España","Estadio Maracaná","2018-01-25")
		PBRBoletaPlatino = Boleta(10000,540000,PartidoBR,'Platino')
		PBRBoletaVIP = Boleta(35000,234000,PartidoBR,'VIP')
		PBRBoletaPreferencia = Boleta(40000,134000,PartidoBR,'Preferencia')
		PartidoBR.agregarBoletas(PBRBoletaPlatino,PBRBoletaVIP,PBRBoletaPreferencia)
		Main.listaEventos.append(PartidoBR)
		Main.EventoDeporte.append(PartidoBR)

#------------------------------------------Funciones del sistema---------------------------------------
	@staticmethod    
	def existenciaDato(objeto):
		if(objeto != None):
			return True
		else:
			return False
	def salir(self):
		print("Gracias por visitarnos,feliz día")
		sys.exist(0)

	def run(self):
		while self.break_while==1:
			self.display_menu()
			print("******************************************")
			opcion=""
			action=""
			print(Mensajes.mensajesOtros['elejirMenu'])
			opcionMenu = int(input())
			if(opcionMenu == 1):
				email = input(Mensajes.MensajesUsuario['Email'])
				clave = input(Mensajes.MensajesUsuario['Clave'])
				UsuarioLogin = Main.LoginUsuario(email,clave)
				if(Login != None):
					Main.UsuarioEnlinea.append(UsuarioLogin)
					Usuario.display_menu_usuario()
					print(Mensajes.mensajesOtros['opcion'])
					opcion = input()
					action = self.opcionesEstudiante.get(opcion)
				else:
					print(Mensajes.MensajesOtros['loginFail'])
			elif(opcionMenu == 2):
				Administrador.display_menu_admin()
				print(Mensajes.mensajesOtros['opcion'])
				opcion = input()
				action = self.opcionesAdministrador.get(opcion)
			elif(opcionMenu == 3):
				Main.display_menu_invitado()
				print(Mensajes.mensajesOtros['opcion'])
				opcion = input()
				action = self.opcionesInvitado.get(opcion)
			if action:
				action()
			else:
				print(Mensajes.mensajesOtros['opcionNoValida'].format(opcion))      
















