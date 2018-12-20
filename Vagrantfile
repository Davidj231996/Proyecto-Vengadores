Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    # each of the below values will default to use the env vars named as below if not specified explicitly
    azure.tenant_id = "6970c313-2466-4a80-a636-1f2fd6f07405"
    azure.client_id = "c0405557-b470-443c-9b90-477c7faba57a"
    azure.client_secret = "cafe051e-b997-406d-8384-736efa21c60c"
    azure.subscription_id = "60538fec-4301-4eee-b463-534ddc71e8a4"

    azure.vm_name = 'noticiario'
    azure.vm_size = 'Standard_B1s'
    azure.tcp_endpoints = '80'

  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook.yml"
  end

end
