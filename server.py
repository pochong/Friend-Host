import socket
import sys
import threading



class server:
    
    PORT = 6011
    ADDR = ('',PORT)
    clients = []
    Size = 0
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(self.ADDR)
        self.tcp_socket.listen(5)

        threading.Thread(target=self.tcp_connection).start()

        self.print_list()


    def print_list(self):
        
        while self.Size <2:
            i = 1

        for c in self.clients:
            print(c)

    #TCP socket for making connection
    def tcp_connection(self):
        while True:
            c  = self.tcp_socket.accept()
            addr = c[1]
            self.clients.append(addr)
            self.Size += 1
            print("Get connection from: ", addr)
            m = ("welcome to chat room").encode('utf-8')
            c[0].send(m)


server()
    
    
    
    





    
