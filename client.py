import socket
import sys


port = 6000

#server ip address
ip = '167.99.160.18'

ADDR = (ip,port)

#TCP socket for making connection
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    tcp_socket.connect(ADDR)
    


#UDP socket for data transmitting
#udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


    