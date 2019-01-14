Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # Usamos una red privada para evitar el acceso desde internet. a nuestra MV
  config.vm.network "private_network", guest: 80, host: 80

  # Ponemos el link del box usado para azure
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'

  # Deshabilitamos la copia del directorio actual en la MV en /vagrant
  config.vm.synced_folder '.', '/vagrant', :disabled => true


  config.vm.provider :azure do |azure, override|

    # Las credenciales de azure
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Datos sobre la MV
    azure.vm_name = 'noticiarioiv1819' # Nombre
    azure.vm_size = 'Standard_B1s' # Tipo de tamaño
    azure.tcp_endpoints = '80' # Puerto para TCP
    azure.location = 'westus' # Localizacion de la MV
    azure.vm_image_urn = 'Canonical:UbuntuServer:18.04-LTS:latest' # Nombre de la MV de Azure a usar
    azure.resource_group_name = 'rough-snowflake-37' # Nombre del grupo de recursos

  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
