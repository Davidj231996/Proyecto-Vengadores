# Despliegue IaaS Vagrant

Para el despliegue se han realizado los 3 siguientes pasos:

	1. Aprovisionamiento
	2. Creación de la máquina virtual y despliegue.
	3. Despliegue

## 1. Arovisionamiento

Para el aprovisionamiento, se ha usado Ansible. Para ello hemos creado un script con las tareas necesarias a realizar para que la máquina virtual tenga todos los requisitos funcionales.

Lo primero que tenemos que hacer es editar el archivo `/etc/ansible/hosts`. Tenemos que añadir el host de nuestra máquina virtual:

~~~
[noticiario]
noticiarioiv1819.cloudapp.azure.com
~~~

El script de ansible creado es el siguiente:

![playbook.yml](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/ansible.PNG)

Para ejecutar el script fuera del Vagrantfile se usa la orden `ansible-playbook playbook.yml`.

Las primeras tres líneas del archivo son para la conexión a la máquina virtual. `hosts` nos indica el nombre del host al que conectar, en nuestro caso, lo que hemos añadido al archivo `/etc/ansible/hosts`; `sudo: yes` es para indicar que vamos a ejecutar las ordenes como sudo; y `remote_user`es el usuario con el que nos conectamos al host.

El resto del archivo son los tasks o acciones que se hacen una vez conectados a la máquina virtual. En nuestro caso:

- Actualizar el sistema.
- Instalar Git.
- Instalar Pip.
- Clonar el repositorio Github.
- Instalar requeriments.txt.

## 2. Creación de la máquina virtual y despliegue

Lo primero que tenemos que hacer es instalar Vagrant desde su página oficial. Después tenemos que crear las claves ssh en el caso que no las tengamos con la orden `ssh-keygen`, y guardarlas en `~/.ssh/id_rsa`.

Ahora pasamos a la creación del archivo Vagrantfile para la creación de la máquina virtual usando azure como provisionador. Para ello necesitamos primero instalar el plugin de azure en Vagrant, y la obtención de las claves de Azure.

Para instalar el plugin de Azure en Vagrant, tenemos que ejecutar la siguientes órdenes:

- `vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure`
- `vagrant plugin install vagrant-azure`

Para la obtención de claves de Azure, nos vamos al portal de Azure y abrimos él bash que viene con Azure CLI ya instalado. Para ello ejecutamos las siguientes órdenes:

- `az login` o `az account list` (dependiendo si estamos ya logueados o no). Esto nos devolverá nuestras suscripciones en Azure, debemos de fijarnos en la que tenga el valor `isDefault` a True. De esa tenemos que coger las claves `id`, que es el ID de la subscripción activa por defecto
- `az ad sp create -for-rbac`. Para crear un Directorio de Aplicación Activo Azure. Nos devolverá las claves `Tenant_id passwordId y appId`.

Las claves obtenidas tenemos que añadirlas al archivo /etc/environments para exportar unas variables con esos valores y así no sean visibles.

Una vez realizado estos pasos, ya podemos crear nuestro Vagrantfile:

![Vagrantfile](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/vagrant.PNG)

En el archivo indicamos que vamos a usar azure con `config.vm.box`. Le indicamos donde va a estar las claves ssh con `config.ssh.private_key_path`. Le indicamos que con el proveedor azure vamos a realizar lo siguiente:

- Le indicamos las claves de Azure previamente obtenidas.
- Le indicamos el nombre de la máquina virtual, su tamaño y su puerto.

Por último, le indicamos que hacer cuando indicamos la orden provision:

- ejecutar `ansible-playbook playbook.yml`.


## 3. Despliegue

Para el despliegue es necesario crear un archivo fabfile.py, que nos permitirá automatizar ordenes a través de ssh.

El archivo fabfile.py es el siguiente:

![Fabfile](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/fabfile.PNG)
![Fabfile](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/docs/Imagenes/fabfile2.PNG)

En este archivo establecemos los tasks a realizar con `@task` y una función con el parámetro `ctx` como nos indica que tenemos que hacer en el tutorial de Fabric.

En las funciones, primero conectamos usando `Connection`, le indicamos el host y el usuario. Una vez ya conectados, ejecutamos las órdenes necesarias en cada función.

Para ejecutar el archivo desde fuera de la máquina virtual usamos la siguiente orden `fab -f fabfile.py -H vagrant@noticiarioiv1819.westus.cloudapp.azure.com <nombrefuncio>`.