from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    setLogLevel('info')
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    print("*** Adding Remote SDN Controller")
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)

    print("*** Adding Switch")
    s1 = net.addSwitch('s1')

    print("*** Adding Hosts (Server & Client)")
    server = net.addHost('server', ip='10.0.0.1')
    client = net.addHost('client', ip='10.0.0.2')

    print("*** Creating Links")
    net.addLink(server, s1)
    net.addLink(client, s1)

    print("*** Starting Network")
    net.build()
    c0.start()
    s1.start([c0])

    print("*** Network Started. Entering CLI...")
    CLI(net)

    print("*** Stopping Network")
    net.stop()

if __name__ == '__main__':
    create_network()
