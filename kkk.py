import sys
from Usuario import Usuario
from Administrador import Administrador
from Evento import Evento
from Boleta import Boleta
from Item import Item
from Factura import Factura
from Mensajes import Mensajes
from ManejoArchivos import ManejoArchivos
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
		'2': self.ConsultarEventoNombre,
		'3': self.ConsultarEventoCodigo,
		'4': self.ConsultarEventoCategoria,
		'5': self.VerMisFacturas,
		'6': self.VerMisDatos,
		'7': self.EditarMisDatos,
		'8': self.RealizarPedido
		}
	#la opcion de regresar sería en el run,mostrar nuevamente el menu
		self.opcionesAdministrador = {
		'1': self.RegistrarEvento,
		'2': self.EditarEvento,
		'3': self.VerEventos,
		'4': self.ConsultarEventoNombre,
		'5': self.ConsultarEventoCodigo,
		'6': self.ConsultarEventoCategoria,
		'7': self.VerUsuarios,
		}

		self.opcionesInvitado = {
		'1': self.VerEventos,
		'2': self.ConsultarEventoNombre,
		'3': self.ConsultarEventoCodigo,
		'4': self.ConsultarEventoCategoria,
		'5': self.RegistrarUsuario,
		}

#-----------------------------------------------------Menús---------------------------------------------------------------
	def display_menu(self):
		print("Menu:", "\n 1.", Mensajes.MensajesUsuario['ingresar'] , "\n 2." , Mensajes.MensajesAdministrador['ingresar'] ,
		"\n 3." , Mensajes.MensajesOtros['ingresar'],"\n 4." , Mensajes.MensajesOtros['datosFicticios'],"\n 5." , Mensajes.MensajesOtros['salir'])

	def display_menu_invitado(self):
		print("\n 1.", Mensajes.MensajesEvento['ver'], "\n 2." , Mensajes.MensajesEvento['consultaNombre'],
		"\n 3." , Mensajes.MensajesEvento['consultaCodigo'], "\n 4.", Mensajes.MensajesEvento['consultaCategoria'], 
		"\n 5.",Mensajes.MensajesUsuario['registro'],"\n 6." ,Mensajes.MensajesOtros['regresar'])

	def display_menu_usuario(self):
		print(Mensajes.MensajesUsuario['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['ver'], "\n 2." , Mensajes.MensajesEvento['consultaNombre'],
		"\n 3." , Mensajes.MensajesEvento['consultaCodigo'],"\n 4." , Mensajes.MensajesEvento['consultaCategoria'],"\n 5.", Mensajes.MensajesUsuario['verFacturas'],
		"\n 6." , Mensajes.MensajesUsuario['verDatos'],"\n 7." , Mensajes.MensajesUsuario['editarDatos'],"\n 8." ,Mensajes.MensajesCompra['pedido'],"\n 9." ,Mensajes.MensajesOtros['regresar'])

	def display_menu_admin(self):
		print(Mensajes.MensajesAdministrador['menu'] + " :", "\n 1.", Mensajes.MensajesEvento['Crear'], 
		"\n 2." , Mensajes.MensajesEvento['editar'] ,"\n 3." , Mensajes.MensajesEvento['ver'],
		"\n 4." , Mensajes.MensajesEvento['consultaNombre'],"\n 5." , Mensajes.MensajesEvento['consultaCodigo'],
		"\n 6." , Mensajes.MensajesEvento['consultaCategoria'],"\n 7." ,Mensajes.MensajesAdministrador['verUsuarios'],"\n 8." ,Mensajes.MensajesOtros['regresar'])

	def display_menu_otros(self):
		print(Mensajes.MensajesOtros['menu'] + " :", "\n 1.", Mensajes.MensajesOtros['datosFicticios'], 
		"\n 2." , Mensajes.MensajesOtros['salir'])

#-----------------------------------------------------Funciones Usuario------------------------------------------------------------ 
	@staticmethod
	def LoginUsuario(email,clave):
		for usuario in Main.ListaUsuarios:
			if(usuario.getEmail()== email and str(usuario.getClave()) == str(clave)):     
				return usuario
			else:
				return None

	def RegistrarUsuario(self):
		email = input(Mensajes.MensajesUsuario['ingreseEmail'])
		clave = input(Mensajes.MensajesUsuario['ingreseClave'])
		cuenta = input(Mensajes.MensajesUsuario['ingreseCuenta'])
		documento = input(Mensajes.MensajesUsuario['ingreseDocumento'])
		nombre = input(Mensajes.MensajesUsuario['ingreseNombre'])   
		celular = input(Mensajes.MensajesUsuario['ingreseCelular'])      
		UsuarioConsultado = Usuario.consultarUsuario(Main.ListaUsuarios, email)
		if(not Main.existenciaDato(UsuarioConsultado)):
			NuevoUsuario = Usuario(email,clave,cuenta,documento,nombre,celular)
			ManejoArchivos.Escribir("Usuarios.txt",email,clave,cuenta,documento,nombre,celular)
			Main.ListaUsuarios.append(NuevoUsuario)
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
			print("\n" + Main.UsuarioEnLinea.toString())
		else:
			print(Mensajes.MensajesOtros['noLogin'])

	def EditarMisDatos(self):
		pass

	def VerMisFacturas(self):
		pass

	@staticmethod
	def ObtenerLocalidad(opcion):
		if(opcion == 1):
			resultado = 'Unica'
		elif(opcion == 2):
			resultado= 'Platino'
		elif(opcion == 3):
			resultado = 'VIP'
		elif(opcion == 4):
			resultado = 'Preferencia'
		return resultado



	def RealizarPedido(self):
		Pedido = Factura(Main.UsuarioEnLinea)
		print(Mensajes.MensajesUsuario['online'] + Main.UsuarioEnLinea.getNombre())
		Main.UsuarioEnLinea.agregarFactura(Pedido)
		Salida = 1
		Respuesta = 2
		Comprar = True		
		verificar = 0
		while(Comprar == True):              
			while(Salida != 3):
				Busqueda = int(input(Mensajes.MensajesEvento['ingreseCodigo']))
				EventoCompra = Evento.consultarEventoCodigo(Main.ListaEventos,Busqueda)
				print(EventoCompra.toString())
				Respuesta = input((Mensajes.MensajesCompra['confirmarEvento']))
				if(Respuesta == '2'):
					Respuesta = 2
				elif(Respuesta == '3'):
					Salida = 3
					if(verificar == 0):
						Comprar = False
				elif(Respuesta == '1'):				
					while(True):
						verificar += 1
						OpcionCompra = Main.ObtenerLocalidad(int(input(Mensajes.MensajesCompra['localidadCompra'])))
						BoletaCompra = EventoCompra.obtenerBoletaLocalidad(OpcionCompra)
						if BoletaCompra != None:
							Cantidad = int(input(Mensajes.MensajesEvento['ingreseCantidad']))
							item = Item(BoletaCompra,Cantidad)
							Pedido.agregarItem(item)
							SeguirComprando = (input(Mensajes.MensajesCompra['continuarCompra']))
							if(SeguirComprando == '1'):
								break
							elif(SeguirComprando ==  '2'):
								Salida = 3
								break              
						else:
							print(Mensajes.MensajesOtros['opcionNoValida'])
			if (Comprar == False):
				break
			MetodoPago = int(input((Mensajes.MensajesCompra['metodoPago'])))
			if(MetodoPago == 1):
				Pedido.setMetodo('Efectivo')
			elif(MetodoPago == 2):
				Pedido.setMetodo('Tarjeta')             
			Pedido.pagarFactura()
			Main.UsuarioEnLinea.agregarFactura(Pedido)
			print(Mensajes.MensajesCompra['gracias'])
			Comprar = False
		print("******************************************")

#-----------------------------------------------------Funciones Administrador----------------------------------------------------
	@staticmethod
	def LoginAdmin(email,llave):
		for admin in Main.ListaAdministradores:
			if(admin.getEmail()== email and admin.getLlave() == llave):     
				return admin
			else:
				return None

	def EditarEvento():
		pass

	def RegistrarEvento(self):
		categoria = Main.ObtenerCategoria(int(input(Mensajes.MensajesEvento['ingreseCategoria'])))
		nombre = input(Mensajes.MensajesEvento['ingreseNombre'])
		descripcion = input(Mensajes.MensajesEvento['ingreseDescripcion'])
		lugar = input(Mensajes.MensajesEvento['ingreseLugar'])
		fecha = str(input(Mensajes.MensajesEvento['ingreseFecha']))
		EventoConsultado = Evento.consultarEventoCodigo(Main.ListaEventos, nombre)
		if(not Main.existenciaDato(EventoConsultado)):
			NuevoEvento = Evento(categoria,nombre,descripcion,lugar,fecha)
			VerificarLocalidad = Main.VerificarLocalidad(input(Mensajes.MensajesEvento['Localidad']))
			if(VerificarLocalidad):
				PrecioBoletaPlatino = int(input(Mensajes.MensajesEvento['PrecioPlatino']))
				CantidadBoletaPlatino = int(input(Mensajes.MensajesEvento['ingreseCantidad']))
				BoletaPlatino = Boleta(CantidadBoletaPlatino,PrecioBoletaPlatino,NuevoEvento,'Platino')
				PrecioBoletaVIP = int(input(Mensajes.MensajesEvento['PrecioVIP']))
				CantidadBoletaVIP = int(input(Mensajes.MensajesEvento['ingreseCantidad']))
				BoletaVIP = Boleta(CantidadBoletaVIP,PrecioBoletaVIP,NuevoEvento,'VIP')
				PrecioBoletaPreferencia = int(input(Mensajes.MensajesEvento['PrecioPreferencia']))
				CantidadBoletaPreferencia = int(input(Mensajes.MensajesEvento['ingreseCantidad']))
				BoletaPreferencia = Boleta(CantidadBoletaPreferencia,PrecioBoletaPreferencia,NuevoEvento,'Preferencia')
				NuevoEvento.agregarBoletas(BoletaPlatino,BoletaVIP,BoletaPreferencia)               
			else:
				precio = int(input(Mensajes.MensajesEvento['ingresePrecio']))
				cantidad = int(input(Mensajes.MensajesEvento['ingreseCantidad']))
				boleta = Boleta(cantidad,precio, NuevoEvento)
				NuevoEvento.agregarBoletas(boleta)              
		Main.ListaEventos.append(NuevoEvento)
		Main.clasificarCategoria(NuevoEvento)
		print(Mensajes.MensajesOtros['operacionExitosa'])
		if(Main.existenciaDato(EventoConsultado)):
			print(Mensajes.MensajesEvento['EventoExistente'])

	def VerUsuarios(self):
		for usuario in Main.ListaUsuarios:
			print("\n" + usuario.toString())
 
#-----------------------------------------------------Funciones Evento-----------------------------------------------------------
	@staticmethod
	def ObtenerCategoria(categoria):
		if(categoria == 1):
			resultado = 'Concierto'
		elif(categoria == 2):
			resultado = 'Deporte'
		elif(categoria == 3):
			resultado = 'Teatro'
		elif(categoria == 4):
			resultado = 'Festival'
		return resultado

	@staticmethod
	def VerificarLocalidad(localidad):
		if(localidad == '1'):
			return True
		else:
			return False

	@staticmethod
	def clasificarCategoria(Evento):
		if(Evento.getCategoria() == 'Concierto'):
			Main.EventoConcierto.append(Evento)
		elif(Evento.getCategoria() == 'Deporte'):
			Main.EventoDeporte.append(Evento)
		elif(Evento.getCategoria() == 'Teatro'):
			Main.EventoTeatro.append(Evento)
		elif(Evento.getCategoria() == 'Festival'):
			Main.EventoFestival.append(Evento)

	@staticmethod
	def VerLista(lista):
		for elemento in lista:
			print("\n" + elemento.toString())

	def VerEventos(self):
		for Evento in Main.ListaEventos:
			print("\n" + Evento.toString())

	def ConsultarEventoNombre(self):
		nombreConsulta = input(Mensajes.MensajesEvento['ingreseNombre'])
		EventoConsulta = Evento.consultarEventoNombre(Main.ListaEventos,nombreConsulta)
		if(Main.existenciaDato(EventoConsulta)):
			print(EventoConsulta.toString())
		else:
			print(Mensajes.MensajesOtros['noExiste'])

	def ConsultarEventoCodigo(self):
		codigoConsulta = int(input(Mensajes.MensajesEvento['ingreseCodigo']))
		EventoConsulta = Evento.consultarEventoCodigo(Main.ListaEventos,codigoConsulta)
		if(Main.existenciaDato(EventoConsulta)):
			print(EventoConsulta.toString())                
		else:
			print(Mensajes.MensajesOtros['noExiste'])
			

	def ConsultarEventoCategoria(self):
		Categoria = int((input(Mensajes.MensajesEvento['ingreseCategoria'])))
		if(Categoria == 1):
			Main.VerLista(Main.EventoConcierto)
		elif(Categoria == 2):
			Main.VerLista(Main.EventoDeporte)
		elif(Categoria == 3):
			Main.VerLista(Main.EventoTeatro)
		elif(Categoria == 4):
			Main.VerLista(Main.EventoFestival)

	def EditarEvento(self):
		pass


#-----------------------------------------------------Datos ficticios------------------------------------------------------------
	def CrearDatosFicticios(self):
		#Cargar Base de datos usuarios
		ListaInstanciasUsuario = ManejoArchivos.Leer("Usuarios.txt")
		for usuario in ListaInstanciasUsuario:
			Main.ListaUsuarios.append(Usuario(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5]))
		#Crear datos ficticios para administradores
		Admin1 = Administrador("admin1@evento.com","2468","1234456789","1143678903","Pepe","3008889977","master1")
		Admin2 = Administrador("admin2@evento.com","2469","1234456780","1143678904","Francisco","3008889978","master1")
		Main.ListaAdministradores.append(Admin1)
		Main.ListaAdministradores.append(Admin2)
		#Crear eventos ficticios
		#1
		ConciertoGuns = Evento("Concierto","Guns & roses","Concierto de despedida Guns & roses","Medellin","2017-12-24")
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
		Main.ListaEventos.append(PartidoBR)
		Main.EventoDeporte.append(PartidoBR)
		#3
		TeatroRJ = Evento("Teatro","Romeo y Julieta","Clasico de Shakespeare","Teatro Patria","2017-12-01")
		TRJBoletaPlatino = Boleta(2000,45000,TeatroRJ,'Platino')
		TRJBoletaVIP = Boleta(5000,35000,TeatroRJ,'VIP')
		TRJBoletaPreferencia = Boleta(5000,30000,TeatroRJ,'Preferencia')
		TeatroRJ.agregarBoletas(TRJBoletaPlatino,TRJBoletaVIP,TRJBoletaPreferencia)
		Main.ListaEventos.append(TeatroRJ)
		Main.EventoTeatro.append(TeatroRJ)
		#4
		FestivalVerano = Evento("Festival","Festival de verano","Festival de verano 2018-Música","Parque Metropolitano","2018-12-01")
		BoletaFest = Boleta(52000,70000,FestivalVerano)
		FestivalVerano.agregarBoletas(BoletaFest)
		Main.ListaEventos.append(FestivalVerano)
		Main.EventoFestival.append(FestivalVerano)
		print(Mensajes.MensajesOtros['operacionExitosa'])

#------------------------------------------Funciones del sistema---------------------------------------
	@staticmethod
	def existenciaDato(objeto):
		if(objeto != None):
			return True
		else:
			return False

	def salir(self):
		print("Gracias por visitarnos,feliz día")
		sys.exit(0)

	def run(self):
		while (self.break_while==1):
			self.display_menu()
			print("******************************************")
			opcion=""
			action=""
			print(Mensajes.MensajesOtros['elejirMenu'])
			opcionMenu = int(input())
			if(opcionMenu == 1):
				email = input(Mensajes.MensajesUsuario['Email'])
				clave = input(Mensajes.MensajesUsuario['Clave'])
				UsuarioLogin = Main.LoginUsuario(email,clave)
				if(UsuarioLogin != None):
					Main.UsuarioEnLinea = UsuarioLogin
					print('Bienvenido '+ Main.UsuarioEnLinea.getNombre())
					while(Main.existenciaDato(Main.UsuarioEnLinea)):
						self.display_menu_usuario()
						print(Mensajes.MensajesOtros['opcion'])
						opcion = input()
						action = self.opcionesUsuario.get(opcion)
						if(opcion == '9'):
							print("******************************************")
							Main.UsuarioEnLinea = None
							break
						if action:
							action()

				else:
					print(Mensajes.MensajesOtros['loginFail'])
			elif(opcionMenu == 2):
				email = input(Mensajes.MensajesUsuario['Email'])
				llave = input(Mensajes.MensajesUsuario['Clave'])
				AdminLogin = Main.LoginAdmin(email,llave)
				if(AdminLogin != None):
					Main.UsuarioEnLinea = AdminLogin
					print('Bienvenido Administrador: '+ Main.UsuarioEnLinea.getNombre())
					while(Main.existenciaDato(Main.UsuarioEnLinea)):
						self.display_menu_admin()
						print(Mensajes.MensajesOtros['opcion'])
						opcion = input()
						action = self.opcionesAdministrador.get(opcion)
						if(opcion == '7'):
							print("******************************************")
							Main.UsuarioEnLinea = None
							break
						if action:
							action()
				else:
					print(Mensajes.MensajesOtros['loginFail'])

			elif(opcionMenu == 3):
				while(True):
					self.display_menu_invitado()
					print(Mensajes.MensajesOtros['opcion'])
					opcion = input()
					action = self.opcionesInvitado.get(opcion)
					if(opcion == '6'):
						print("******************************************")
						break
					if action:
						action()

			elif(opcionMenu == 4):
				action = self.CrearDatosFicticios()

			elif(opcionMenu == 5):
				action = self.salir()
			if action:
				action()


if __name__ == "__main__":
	Main().run()