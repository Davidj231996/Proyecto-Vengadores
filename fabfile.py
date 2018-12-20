#!/usr/bin/env python

# Fabfile to:
#    - Borrar el microservicio
#    - Actualizar el microservicio
#    - Iniciar el microservicio

# Import Fabric's API module
from fabric.api import *

def Borrar():

    # Borramos antiguo codigo
    run('rm -rf Proyecto-Vengadores')


def Actualizar():

    # Borramos antiguo codigo
    Borrar

    # Descargamos nuevo repositorio
    run('git clone https://github.com/Davidj231996/Proyecto-Vengadores.git')  

    # Instalamos requirements
    run('pip3 install -r Proyecto-Vengadores/requirements.txt')


def Iniciar():

     # Iniciamos el servicio web
     run('cd Proyecto-Vengadores && sudo gunicorn api_web:app -b 0.0.0.0:80')
