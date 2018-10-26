import pytest
from pruebas import Noticiario

def test_inicializar():
	n=Noticiario()
	assert isinstance(n,Noticiario), "Error al inicializar"

def test_cuentaNoticias():
	n=Noticiario()
	assert n.cuentaNoticias()==2, "Error al contar"

def test_crear_Noticia():
	n = Noticiario()
	assert n.crear_Noticia("El Clásico más importante","El Clásico del 28-O es de vital importancia para ambos equipos","Futbol")==3, "Error en la creacion"

def test_postCreacion():
	n=Noticiario()
	assert n.cuentaNoticias()==3, "Error al contar"

def test_editar():
	n=Noticiario()
	assert n.editarNoticia("El golf 2","El golf es un deporte en disminución","Golf",1)==True, "Error en la edición"
