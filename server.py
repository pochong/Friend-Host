import socket
import sys
import threading



class server:
    
    PORT = 6000
    ADDR = ('',port)

    def __init__(self):
        self.clients = {}
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(ADDR)
        self.tcp_socket.listen(5)

        threading.Thread(target=self.tcp_connection).start()

    #TCP socket for making connection
    def tcp_connection(self):
        while True:
            c , addr = self.tcp_socket.accept()
            print("Get connection from: ", addr)


server().start()
    
    
    
    





    