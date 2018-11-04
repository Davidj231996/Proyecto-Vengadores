import pytest
from noticiario import Noticiario

#Comprobar que la inicializacion es correcta
def test_inicializar():
	n=Noticiario()
	assert isinstance(n,Noticiario), "Error al inicializar"

#Comprobar que existen 2 noticias al empezar
def test_cuentaNoticias():
	n=Noticiario()
	assert n.cuentaNoticias()==2, "Error al contar"

#Comprobar que la noticia se ha creado correctamente
def test_crear_Noticia():
	n = Noticiario()
	assert n.crear_Noticia("El Clásico más importante","El Clásico del 28-O es de vital importancia para ambos equipos","Futbol")==True, "Error en la creacion"

#Comprobar que después de la creación haya 3 noticias
def test_postCreacion():
	n=Noticiario()
	assert n.cuentaNoticias()==3, "Error al contar"

#Comprobar que se ha editado correctamente
def test_editar():
	n=Noticiario()
	assert n.editarNoticia("El golf 2018","El golf es un deporte en disminución","Golf",1)==True, "Error en la edición"

#Comprobar que al editar no se han eliminado ni creado nuevas noticias
def test_postEdicion():
	n=Noticiario()
	assert n.cuentaNoticias()==3, "Error al contar"

#Comprobar que se ha eliminado una noticia
def test_eliminar():
	n=Noticiario()
	assert n.eliminarNoticia(2)==2, "Error al eliminar"

#Comprobar que muestra solo una noticia de la categoria NBA
def test_mostrarNoticiasCategoria():
	n=Noticiario()
	assert n.mostrarNoticiasCategoria("NBA")==1, "Error en el muestreo"
