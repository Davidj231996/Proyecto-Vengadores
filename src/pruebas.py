class Noticiario():
	"""Clase para el microservicio Noticiario"""

	def __init__(self):
		self.__noticias = 0;

	def crear_Noticia(titulo, descripcion):
		if(len(titulo) < 10):
			return -1
		elif(len(titulo) > 50):
			return -2
		elif(len(descripcion) < 0):
			return -3
		else:
			return 0

	def crear_Usuario(nombre, alias):
		if(len(nombre) < 3):
			return -1
		elif(len(alias) < 5):
			return -2
		elif(len(alias) > 15):
			return -3
		else:
			return 0
