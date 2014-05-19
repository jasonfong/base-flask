# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Base box
  config.vm.box = "cloudimg-trusty64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Port forwarding
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Private network
  # config.vm.network "private_network", ip: "192.168.99.99"

  # Public network, which generally matched to bridged network.
  # config.vm.network "public_network"

  # SSH agent forwarding.
  config.ssh.forward_agent = true

  # Additional shared folders to the guest VM
  # config.vm.synced_folder "/projects/vboxshare/", "/media/sf_vboxshare"
  

  # VirtualBox config tweaks
  config.vm.provider "virtualbox" do |vb|
    # VirtualBox name
    vb.name = "base-project"

    # Don't boot with headless mode
    # vb.gui = true
  
    # VM settings:
    vb.customize ["modifyvm", :id, "--ostype", "Ubuntu_64"]
    vb.customize ["modifyvm", :id, "--memory", "512"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
    # vb.customize ["modifyvm", :id, "--acpi", "on"]
    # vb.customize ["modifyvm", :id, "--ioapic", "on"]
    # vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
    # vb.customize ["modifyvm", :id, "--pae", "on"]
  end


  # Ansible provisioning
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.host_key_checking = false
    #ansible.verbose = "vvvv"
  end

end
