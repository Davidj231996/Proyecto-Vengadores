class Noticiario():
	"""Clase para el microservicio Noticiario"""

	def crear_Noticia(titulo,descripcion):
		if(len(titulo) < 10):
			return False
		elif(len(titulo) > 50):
			return False
		elif(len(descripcion) < 0):
			return False
		else:
			return True

	def crear_Usuario(nombre,alias):
		if(len(nombre) < 3):
			return False
		elif(len(alias) < 5):
			return False
		elif(len(alias) > 15):
			return False
		else:
			return True
