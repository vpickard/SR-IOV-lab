#!/usr/bin/python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.util import dumpNodeConnections


def createTopology(switch, hosts):
    ODL_Controller_IP='127.0.0.1'
    setLogLevel('info')
    topo = Topo()
    switch = topo.addSwitch(switch)

    for (hostname, opts) in hosts:
        host = topo.addHost(hostname, **opts)
        topo.addLink(host, switch, None)

    network = Mininet(topo, controller=None)
    #odl_ctrl = network.addController('c0', controller=RemoteController, ip=ODL_Controller_IP, port=6633)
    network.start()
    print "*** Dumping host connections"
    dumpNodeConnections(network.hosts)
    CLI(network)
    network.stop()
