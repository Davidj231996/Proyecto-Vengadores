# Despliegue en Heroku de nuestro contenedor de Docker Hub.

Vamos a dar los pasos a seguir para crear nuestro contenedor en Docker Hub, y su posterior despliegue en Heroku.

## Creación del contenedor en Docker Hub.

Pasos a seguir:

1. Crear una cuenta en Docker Hub.
2. Crear un dockerfile como el siguiente:
![Dockerfile](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/dockerfile.PNG)

3. Crear un repositorio público con integración continua desde su menú de navegación.
![Docker](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/docker.png)

Primero, la orden para descargar la imagén última de python. Segundo, establecemos el directorio de trabajop en */*. Tercero, copiamos todo el repositorio en la imagén y instalamos lo que hay en *requirements.txt*. Cuarto, abrimos el puerto 80. Por último, ejecutamos gunicorn en el puerto 80 sobre *API_WEB.py, su app*.

El resultado sería el siguiente:

![Contenedor](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/contenedor.PNG)

## Despliegue del contenedor en Heroku.

Pasos a seguir:

1. *heroku auth:token*
2. *docker login --username=_ --password={token_anterior} registry.heroku.com*
3. Ahora vamos a nuestra cuenta de Heroku, y creamos una nueva aplicación.
4. *docker build -t registry.heroku.com/nombre-app/web .*
5. *docker push registry.heroku.com/nombre-app/web*

Resultado final:

![Despliegue](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/heroku_contenedor.PNG)

![Aplicación](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/contenedor_app.PNG)

Contenedor: https://proyecto-vengadores-iv.herokuapp.com

## Orden para que el entorno se pueda descargar de DockerHub.

*docker pull davidj231996/proyecto-vengadores*
