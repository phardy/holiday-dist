#!/usr/bin/python
#
import socket
import struct

MCAST_GRP = '224.0.0.249'       # MooresCloud multicast address
MCAST_PORT = 4011               # And port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print "Listening..."

while True:
        d = sock.recv(1024)
        print d
        #ds = d.split('\n')
        #print len(ds)

