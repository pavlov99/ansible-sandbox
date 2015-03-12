# -*- mode: ruby -*-
# vi: set ft=ruby:fdm=marker
HOST = "33.33.33.01"
HOSTNAME = "local.kirillpavlov.com"
MEMORY = "2048"
CPUS = "4"
NFS = true

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = HOSTNAME
    config.vm.network :private_network, ip: HOST
    # config.vm.network :public_network

    # Configure provider
    config.vm.provider :virtualbox do |vb|
        vb.gui = false
        vb.name = HOSTNAME
        vb.memory = MEMORY
        vb.cpus = CPUS

        # Fix slow external network connections
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
    end

    # Share folders
    config.vm.synced_folder "..", "/vagrant", :nfs => NFS
    
    # SSH config
    config.ssh.forward_agent = true
    config.ssh.forward_x11 = true

    config.vm.provision "ansible" do |ansible|
    end
end
