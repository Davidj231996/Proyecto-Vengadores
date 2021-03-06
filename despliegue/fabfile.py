#!/usr/bin/env python

# Import modules
from fabric import task
from fabric.connection import Connection

@task
def Borrar(ctx):

    # Paramos la ejecución
    Parar(ctx)

    # Borramos antiguo codigo
    with Connection('noticiarioiv1819.westus.cloudapp.azure.com',user='vagrant') as c:
       c.run('sudo rm -rf Proyecto-Vengadores')

@task
def Actualizar(ctx):

    # Borramos antiguo codigo
    Borrar(ctx)

    # Descargamos nuevo repositorio
    with Connection('noticiarioiv1819.westus.cloudapp.azure.com',user='vagrant') as c:
       c.run('git clone https://github.com/Davidj231996/Proyecto-Vengadores.git')  

       # Instalamos requirements
       c.run('sudo pip3 install -r Proyecto-Vengadores/requirements.txt')

@task
def Iniciar(ctx):

     # Iniciamos el servicio web
     with Connection('noticiarioiv1819.westus.cloudapp.azure.com',user='vagrant') as c:
          with c.cd('Proyecto-Vengadores'):
               c.run('sudo gunicorn api_web:app -b 0.0.0.0:80')


@task
def Parar(ctx):

   #Paramos el servicio web
   with Connection('noticiarioiv1819.westus.cloudapp.azure.com',user='vagrant') as c:
      c.run("sudo kill $(ps -ef | grep gunicorn | awk '{print $2}')")


@task
def Prueba(ctx):

   #Realizamos el test
   with Connection('noticiarioiv1819.westus.cloudapp.azure.com',user='vagrant') as c:
      with c.cd('Proyecto-Vengadores'):
         c.run('pytest')
