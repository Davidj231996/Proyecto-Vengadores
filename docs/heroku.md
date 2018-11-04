# Guía instalación Heroku [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/apps/proyecto-vengadores/deploy/github)

## Instalación

En mi caso, al estar usando windows sólo he tenido que descargarme un .exe con el cliente e instalarlo.

## Iniciar Sesión

Debemos de tener cuenta creado en la web de heroku.

$ heroku login

Nos pedirán nuestro email y contraseña.

## Despliegue

El despliegue lo vamos a hacer desde la página web. Los pasos a seguir son:

1. Tenemos que crear una aplicación en la región de europa.

2. Conectamos la aplicación creada con nuetsro repositorio de GitHub.

3. Activamos la sincronización automática, para que cuando subamos nuevos archivos a nuestro repositorio, la aplicación se actualice automáticamente.

El resultado final sería el siguiente:

![img](https://github.com/Davidj231996/Proyecto-Vengadores/tree/master/docs/Imagenes/heroku.png)

Le damos a "Desplegar Rama", y si todo sale correcto nuestra aplicación estará lista y podremos acceder a ella.

## Elementos necesarios

Debemos de tener en nuestro repositorio, en el raíz, dos archivos que son necesarios:

- Procfile: "web: gunicorn API_WEB:app --log-file -"".

- Un archivo en el idioma elegido para desarrollar nuestra aplicación, en mi caso API_WEB.py.

Además, tendremos que añadir una línea más en el requeriments.txt:

- "gunicorn".

## Ordenes importantes de Heroku

- $ heroku ps:scale web=1 -a proyecto-vengadores. (Para comprobar si está corriendo)

- $ heroku open. (Para ir a la página web de nuestra aplicación)

- $ heroku logs --tail. (Nos permite ver los últimos registros, por lo que también podremos ver los errores)