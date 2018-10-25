import json
import os

class Noticiario():
	"""Clase para el microservicio Noticiario"""

	def __init__(self):
		noticiai=0
		try:
			if os.path.exists('data/noticias.json'):
				with open('data/noticias.json', 'r') as f:
					self.noticias=json.load(f)
			else:
				raise IOError("No se encuentra 'noticias.json'")

			if os.path.exists('data/categorias.json'):
				with open('data/categorias.json', 'r') as f:
					self.categorias = json.load(f)
			else:
				raise IOError("No se encuentra 'data/categorias.json'")

		except IOError as fallo:
			print("Error {} leyendo hitos.json".format( fallo ) )

	def categoria_correcta(self,categoria):
		for i in self.categorias:
			if(i == categoria):
				return True
		return False

	def cuentaNoticias(self):
		self.noticiai = len(self.noticias)
		return len(self.noticias)

	def crear_Noticia(self,titulo,descripcion,categoria):
		if(len(titulo) < 10):
			return False
		elif(len(titulo) > 50):
			return False
		elif(len(descripcion) < 0):
			return False
		elif(Noticiario.categoria_correcta(self,categoria)==False):
			return False
		self.noticias[noticiai]["titulo"] = titulo
		self.noticias[noticiai]["descripcion"] = descripcion
		self.noticias[noticiai]["categoria"] = categoria

		return True