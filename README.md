# Proyecto Vengadores
[![Build Status](https://travis-ci.org/Davidj231996/Proyecto-Vengadores.svg?branch=master)](https://travis-ci.org/Davidj231996/Proyecto-Vengadores)

## Descripción del proyecto.

El proyecto se basa en la creación de un servicio web de noticias 
deportivas. Las noticas se mostraran por deporte, y además, el usuario 
podrá ordenarlas por diferentes categorias.


## Herramientas

Estas son las herramientas que voy a usar para el proyecto:

- Azure

Voy a usar Azure debido a su facilidad para conectarlo con Vagrant y 
Docker. Además, de la posibilidad de usarlo gracias a los creditos 
proporcionados por Microsoft para la asignatura.

- Docker

Voy a usar Docker, ya que se puede conectar a github de manera sencilla 
y rápida. También, su integración con Azure.

- Vagrant

Vagrant se va a usar para la integración del servicio web creado en 
Azure en una máquina virtual.

- MongoDB

Voy a usar esta herramienta de Base de Datos, porque su funcionalidad 
con python es bastante sencilla y fácil de conectar desde el lenguaje.

- Python

Python va a ser el lenguaje de programación a usar, debido a que se 
trata de un lenguaje nuevo para mi y a su fácilidad de uso con MongoDB.

- Flask

Flask va a ser mi framework de servicio web, debido a que es un 
framework de Python y a su facilidad de instalación y uso.

## Infraestructura

La infraestructura del servicio será la siguiente:

- Una base de datos donde almacenar las noticias.

- Un servidor desplegado en Microsoft Azure donde se mostraran las 
noticias almacenadas en la base de datos.

## Pasos a llevar a cabo.

Los pasos a seguir durante el proyecto son:

1. Creación de cuenta en todas las herramientas necesarias.

2. Conectar herramientas como vagrant con azure, azure con docker, 
docker con github.

3. Creación de noticias de prueba en la base de datos.

4. Códifación junto a las pruebas necesarias para conocer el correcto 
funcionamiento.

5. Creación de noticias para el despliegue del servicio.

6. Despliegue del servicio.

## Tests

Los test que voy a realizar, se van a usar para el control en la creación de noticias y de usuarios.

## Instalación de las herramientas necesarias

Para instalar las herramientas necesarias, ejecutaremos la siguiente orden:

pip install -r requirements.txt

## Ejecución de los test

Usaremos pytest.

## Ejecución

python3 pruebas.py
