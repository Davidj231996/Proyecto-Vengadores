import pytest
from pruebas import Noticiario

def test_crear_Noticia():
	n = Noticiario()
	assert n.crear_Noticia("Golf","El golf es un deporte")==False, "Error en la creación de la noticia"
	assert n.crear_Noticia("El golf y su crecimiento","El golf es un deporte en crecimiento") ==True

def test_crear_Usuario():
	n = Noticiario()
	assert n.crear_Usuario("A","B") ==False, "Error en la creación de un usuario"
	assert n.crear_Usuario("David","Rubiales") ==True
