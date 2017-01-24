# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

# NOTE: Netmask is assumed 255.255.255.0 for all

# devstack setup for control and compute nodes
DS_CONTROL_TUNNEL_IP   = "192.168.254.31"
DS_CONTROL_GATEWAY     = "192.168.254.254"
DS_CONTROL_MGMT_IP     = "10.8.125.240"

# devstack setup for compute node
DS_COMPUTE_TUNNEL_IP   = "192.168.254.32"
DS_COMPUTE_GATEWAY     = "192.168.254.254"
DS_COMPUTE_MGMT_IP     = "192.168.50.32"

#Emulated HWVTEP 
HWVTEP_TUNNEL_IP      = "192.168.254.20"
HWVTEP_TUNNEL_GATEWAY = "192.168.254.254"
HWVTEP_MGMT_IP        = "10.8.125.241"
HWVTEP_VLAN_IP        = "192.168.220.20"
HWVTEP_VLAN_IP2       = "192.168.230.20"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "rboyer/ubuntu-trusty64-libvirt"

  # "Control/Compute"
  config.vm.define "control" do |server|
    server.vm.hostname = "control"

    # Control node tunnel transport network
    server.vm.network "private_network",
                      :libvirt__network_name => 'vxlan_net',
                      :libvirt__forward_mode => 'none',
                      ip: DS_CONTROL_TUNNEL_IP,
                      netmask: "255.255.255.0"

    # Management/Control network
    server.vm.network :public_network,
                      :mode => 'bridge',
                      :dev => 'em1',
                      :type => 'direct',
                      :trust_guest_rx_filters => 'true',
                      ip: DS_CONTROL_MGMT_IP,
                      netmask: "255.255.255.0"

    server.vm.provider "libvirt" do |lv|
      lv.memory = 8192
      lv.cpus = 4
    end

    server.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.manifest_file  = "site.pp"
      puppet.options = "--verbose --debug"
    end
  end

  # HWVTEP
  config.vm.define "hwvtep" do |hwvtep|
    hwvtep.vm.hostname = "hwvtep"

    # Tunnel transport network
    hwvtep.vm.network "private_network",
                      :libvirt__network_name => 'vxlan_net',
                      :libvirt__forward_mode => 'none',
                      ip: HWVTEP_TUNNEL_IP,
                      netmask: "255.255.255.0"

    #L2 network, vlan tag 2900
    #hwvtep.vm.network "private_network",
    #                  :libvirt__dhcp_enabled => false,
    #                  :libvirt__network_name => 'v_2900',
    #                  :libvirt__forward_mode => 'none',
    #                  ip: HWVTEP_VLAN_IP,
    #                  netmask: "255.255.255.0"

    # tap for eth2, that will be connected to ovs bridge hwvtepbr
    hwvtep.vm.network :public_network,
                      :mode => 'bridge',
                      :dev => 'hwvtepbr',
                      :type => 'bridge',
                      :ovs => true,
                      :trust_guest_rx_filters => 'true',
                      ip: HWVTEP_VLAN_IP,
                      netmask: "255.255.255.0"

    # tap for eth3, that will be connected to ovs bridge hwvtep-eth3
    hwvtep.vm.network :public_network,
                      :mode => 'bridge',
                      :dev => 'hwvtep-eth3',
                      :type => 'bridge',
                      :ovs => true,
                      :trust_guest_rx_filters => 'true',
                      ip: HWVTEP_VLAN_IP2,
                      netmask: "255.255.255.0"



    # Management/Control network
    hwvtep.vm.network :public_network,
                      :mode => 'bridge',
                      :dev => 'em3',
                      :type => 'direct',
                      :trust_guest_rx_filters => 'true',
                      ip: HWVTEP_MGMT_IP,
                      netmask: "255.255.255.0"

    #Doesn't work, used ip utility to create tagged i/f
    #hwvtep.vlan.add vlan: 2900, parent: "eth2", type: "static",
    #                ip: HWVTEP_VLAN_IP,
    #                netmask: "255.255.255.0"

    hwvtep.vm.provider "libvirt" do |lv|
      lv.memory = 2048
      lv.cpus = 2
    end

    hwvtep.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.manifest_file  = "site.pp"
      puppet.options = "--verbose --debug"
    end
  end

end
