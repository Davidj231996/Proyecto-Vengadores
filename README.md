# Proyecto Vengadores
[![Build Status](https://travis-ci.org/Davidj231996/Proyecto-Vengadores.svg?branch=master)](https://travis-ci.org/Davidj231996/Proyecto-Vengadores)

## Descripción del proyecto.

En este proyecto se va a realizar un Noticiario de deporte, las noticias tendrán su título, descripción y su categoria.

Sobre estas noticias, se va a poder crear nuevas, editar las existentes, eliminar y mostrar las de cierta categoria.


## Herramientas

Estas son las herramientas que voy a usar para el proyecto:

- MongoDB, para almacenar la información.

- Python, como lenguaje de programación.

- Flask, como framework.

- Unittest, como biblioteca para los tests.

## Instalación de las herramientas necesarias

Para instalar las herramientas necesarias, ejecutaremos la siguiente orden:

"pip install -r requirements.txt"

## Ejecución de los test

Usaremos pytest.

## Ejecución

python3 pruebas.py

## Uso

El uso de los tests será el siguiente: a través de dos archivos JSON (noticias y categorias), se realizará la gestión (creación, modificación, eliminación) de noticias y la muestra por 
categorias.

## Por qué he elegido estas herramientas de test e integración continua:

[Visitar](https://davidj231996.github.io/Proyecto-Vengadores/docs/explicacion)

## PaaS Elegido: Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Voy a usar heroku por ser gratis y sencillo de usar.

Despliegue: [Proyecto-Vengadores](https://proyecto-vengadores.herokuapp.com/)

[Documentación heroku](https://github.com/Davidj231996/Proyecto-Vengadores/tree/master/docs/heroku.md)

## Contenedor y despliegue

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

En la [Documentación](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/docker.md) viene explicado paso a paso la creación del contenedor y su despliegue.

Contenedor: [Proyecto-Vengadores](https://docker-proyecto-vengadores.herokuapp.com/)

Repositorio en Docker Hub: https://hub.docker.com/r/davidj231996/proyecto-vengadores/builds/

## Despliegue IaaS Vagrant

Despliegue final: 168.62.219.34

Para la realización de esta parte se ha creado una máquina virtual en Azure usando Vagrant. Además, se ha usado Ansible para su aprovisionamiento y Fabric para la automatización de su puesta en marcha e instalación.

[Documentación Completa](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/azure.md)