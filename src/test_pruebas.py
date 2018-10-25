import pytest
from pruebas import Noticiario

def test_cuentaNoticias():
	n = Noticiario()
	assert n.cuentaNoticias() == 2

def test_crear_Noticia():
	n = Noticiario()
	assert n.crear_Noticia("El Clásico más importante","El Clásico del 28-O es de vital importancia para ambos equipos","Futbol")==True

def test_cuentaNoticias_postCreacion():
	n = Noticiario()
	assert n.cuentaNoticias() == 3
