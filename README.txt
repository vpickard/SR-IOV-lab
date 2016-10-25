SR-IOV Lab
================

This is a companion project to the Open vSwitch series of articles at
http://www.relaxdiego.com.

Network Topology
----------------
We will build a Vagrant file to build a portion of the network in the SR-IOV.pdf file. 
Specifically, we will build:

1. A VM for the Compute Node (SR-IOV enabled). Middle compute node in the diagram.
2. A VM for HWVTEP emulator. This is TOR in the diagram.
3. A VM that has Control/Compute Node (not SR-IOV enabled). Left control/compute node in the diagram.



Requirements
------------

1. Libvirt

2. Vagrant v1.6.3 or above. Install from http://www.vagrantup.com/downloads.html

3. The vagrant-vbguest plugin. Install with `vagrant plugin install vagrant-vbguest`


Installation
------------

Estimated time for the following steps including automated provisioning:
30 minutes. Time will vary depending on your connection speed.

1. Clone this repo and cd to it

2. Run `vagrant up`



Stopping and starting the VMs
-----------------------------

To suspend your VMs, run `vagrant suspend`. To shut them down, run
`vagrant halt`.


Viewing VM status
-----------------

`vagrant status`


Troubleshooting
---------------

