# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

# NOTE: Netmask is assumed 255.255.255.0 for all

# devstack setup for control and compute nodes
DS_CONTROL_TUNNEL_IP   = "192.168.254.31"
DS_CONTROL_GATEWAY     = "192.168.254.254"
DS_CONTROL_MGMT_IP     = "192.168.50.31"

# devstack setup for compute node
DS_COMPUTE_TUNNEL_IP   = "192.168.254.32"
DS_COMPUTE_GATEWAY     = "192.168.254.254"
DS_COMPUTE_MGMT_IP     = "192.168.50.32"

#Emulated HWVTEP 
HWVTEP_TUNNEL_IP      = "192.168.254.20"
HWVTEP_TUNNEL_GATEWAY = "192.168.254.254"
HWVTEP_MGMT_IP        = "192.168.50.20"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "rboyer/ubuntu-trusty64-libvirt"

  # "Control/Compute"
  config.vm.define "control" do |server|
    server.vm.hostname = "control"

    # Control node tunnel transport network
    server.vm.network "private_network",
                      libvirt__network_name: "vxlan_net",
                      ip: DS_CONTROL_TUNNEL_IP,
                      netmask: "255.255.255.0"

    # Management/Control network
    server.vm.network "private_network",
                      ip: DS_CONTROL_MGMT_IP,
                      netmask: "255.255.255.0"

    server.vm.provider "libvirt" do |lv|
      lv.memory = 2048
      lv.cpus = 2
    end

    server.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.manifest_file  = "site.pp"
      puppet.options = "--verbose --debug"
    end
  end


  # Compute
  #config.vm.define "compute" do |server|
  #  server.vm.hostname = "compute"

    # Tunnel transport network
    #server.vm.network "private_network",
    #                  virtualbox__intnet: "server1_net",
    #                  ip: COMPUTE_TUNNEL_IP,
    #                  netmask: "255.255.255.0"

    # Management/Control network
    #server.vm.network "private_network",
    #                  ip: COMPUTE_MGMT_IP,
    #                  netmask: "255.255.255.0"

    #server.vm.provider "libvirt" do |lv|
    #  lv.memory = 2048
    #  lv.cpus = 2
    #end

    #server.vm.provision "puppet" do |puppet|
    #  puppet.manifests_path = "puppet/manifests"
    #  puppet.manifest_file  = "site.pp"
    #  puppet.options = "--verbose --debug"
    #end
  #end

  # HWVTEP
  config.vm.define "hwvtep" do |hwvtep|
    hwvtep.vm.hostname = "hwvtep"

    # Tunnel transport network
    hwvtep.vm.network "private_network",
                      libvirt__network_name: "vxlan_net",
                      ip: HWVTEP_TUNNEL_IP,
                      netmask: "255.255.255.0"

    # Management/Control network
    hwvtep.vm.network "private_network",
                      ip: HWVTEP_MGMT_IP,
                      netmask: "255.255.255.0"

    hwvtep.vm.provider "libvirt" do |lv|
      lv.memory = 2048
      lv.cpus = 2
    end


    # Not persistent across reboots!
    #hwvtep.vm.provision "shell", inline: "route add #{DS_CONTROL_TUNNEL_IP}/32 gw #{DS_GATEWAY} dev eth1"
    #hwvtep.vm.provision "shell", inline: "route add #{DS_COMPUTE_TUNNEL_IP}/32 gw #{DS_GATEWAY} dev eth1"

    hwvtep.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.manifest_file  = "site.pp"
      puppet.options = "--verbose --debug"
    end
  end



end
