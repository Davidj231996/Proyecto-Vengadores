import pytest
from pruebas import Noticiario

def test_crear_Noticia():
	n = Noticiario()
	assert n.crear_Noticia("Golf","El golf es un deporte")==0, "Error en la creación de la noticia"
	assert n.crear_Noticia("El golf","El golf es un deporte en crecimiento")==0, "Error en la creación de la noticia"

def test_crear_Usuario():
	n = Noticiario()
	assert n.crear_Usuario("A","B")==0, "Error en la creación de un usuario"
	assert n.crear_Usuario("David","Rubiales")==0, "Error en la creacion de un usuario"
