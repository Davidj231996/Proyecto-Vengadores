import json
import os

class Noticiario():
	"""Clase para el microservicio Noticiario"""

	def __init__(self):
		noticia_i = 0
		try:
			if os.path.exists('data/noticias.json'):
				with open('data/noticias.json', 'r') as f:
				self.noticias = json.load(f)
			else:
				raise IOError("No se encuentra 'noticias.json'")

			if os.path.exists('data/categorias.json'):
				with open('data/categorias.json', 'r'r) as f:
				self.categorias = json.load(f)
			else:
				raise IOError("No se encuentra 'data/categorias.json'")

		except IOError as fallo:
			print("Error {} leyendo hitos.json".format( fallo ) )

		def cuentaNoticias(self):
			self.noticia_i = len(self.noticias)
			return len(self.noticias)

		def crear_Noticia(self,titulo,descripcion,categoria):
			if(len(titulo) < 10):
				return False
			elif(len(titulo) > 50):
				return False
			elif(len(descripcion) < 0):
				return False
			elif(!categoria_correcta(categoria)):
				return False
			self.noticias[noticia_i]["titulo"] = titulo
			self.noticias[noticia_i]["descripcion"] = descripcion
			self.noticias[noticia_i]["categoria"] = categoria

			return True

		def categoria_correcta(self,categoria):
			for i in self.categorias:
				if(i == categoria):
					return True
			return False
