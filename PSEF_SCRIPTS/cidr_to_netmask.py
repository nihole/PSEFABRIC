import socket
import struct

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    b1,b2,b3,b4 = network.split('.')
    gate = str(b1) + '.' + str(b2) + '.' + str(b3) + '.' + str(int(b4) + 1)
    return network, netmask, gate
