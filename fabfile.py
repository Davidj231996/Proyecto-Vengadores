#!/usr/bin/env python

# Fabfile to:
#    - Borrar el microservicio
#    - Actualizar el microservicio
#    - Iniciar el microservicio

# Import Fabric's API module
# from fabric.api import *
from fabric import task
from fabric.connection import Connection

@task
def Borrar(ctx):

    # Borramos antiguo codigo
    with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
       c.run('sudo rm -rf Proyecto-Vengadores')

@task
def Actualizar(ctx):

    # Borramos antiguo codigo
    Borrar(ctx)

    # Descargamos nuevo repositorio
    with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
       c.run('git clone https://github.com/Davidj231996/Proyecto-Vengadores.git')  

       # Instalamos requirements
       c.run('sudo pip3 install -r Proyecto-Vengadores/requirements.txt')

@task
def Iniciar(ctx):

     # Iniciamos el servicio web
     with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
          with c.cd('Proyecto-Vengadores'):
               c.run('ls')
               c.run('sudo gunicorn api_web:app -b 0.0.0.0:80')


@task
def Parar(ctx):
   with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
      c.run("sudo kill $(ps -ef | grep gunicorn | awk '{print $2}')")


@task
def Prueba(ctx):
   with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
      with c.cd('Proyecto-Vengadores'):
         c.run('pytest')

@task
def Instalar(ctx):
   with Connection('noticiario.westus.cloudapp.azure.com',user='vagrant') as c:
      c.run('git clone https://github.com/Davidj231996/Proyecto-Vengadores.git')
      c.run('sudo pip3 install -r Proyecto-Vengadores/requirements.txt')
