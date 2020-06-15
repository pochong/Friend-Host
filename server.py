import socket
import sys
import threading
import pickle
import struct


class server:
    
    PORT = 8004
    ADDR = ('',PORT)
    clients_address = []
    clients_socket = []
    Size = 0

    #d = b''
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(self.ADDR)
        self.tcp_socket.listen(5)

        threading.Thread(target=self.tcp_connection).start()

        self.print_list()


    def print_list(self):
        
        while self.Size <2:
            i = 1

        for c in self.clients_address:
            print(c)

    """
    def recv_screen(self):
        print("in recv_screen")
        data = b''
        payload_size = struct.calcsize("L") 
        while True:
            while len(data) < payload_size:
                data += self.clients_socket[0].recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.clients_socket[0].recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            if self.Size > 1:

                d = pickle.dumps(frame_data) ### new code
                self.clients_socket[1].sendall(struct.pack("L", len(d))+d) ### new code
            
            ###
            
            frame=pickle.loads(frame_data)
            print frame
            cv2.imshow('framd = pickle.dumps(frame_data) ### new code
            self.tcp_socket.sendall(struct.pack("H", len(d))+d) ### new codeonnection
            
        """

    def recv_message(self,num):
        try: 
            while(True):
                mes = self.clients_socket[num].recv(4096)
                """
                try: 
                    self.clients_socket[num].send(b'received')
                except:
                    print("Failed to reply ")
                """
                self.send_message(num,mes)
        except: 
            print("Failed to receive message")
        
    def send_message(self,num,mes):
        try: 
            i = 0
            while(i < self.Size) :
                if(i!=num): 
                    self.clients_socket[i].send(mes)
                i += 1
        except: 
            print("Failed to send message ")

    def tcp_connection(self):
        while True:
            c  = self.tcp_socket.accept()
            addr = c[1]
            self.clients_address.append(addr)
            self.clients_socket.append(c[0])
            
            if self.Size == 0:
                c[0].send(b'host')
               # threading.Thread(target = self.recv_message,args = (self.Size)).start()
            else:
                c[0].send(b'client')
            threading.Thread(target = self.recv_message,args = (self.Size,)).start()
            self.Size += 1

            
            """
            print("Get connection from: ", addr)
            m = ("welcome to chat room").encode('utf-8')
            c[0].send(m)
            """


server()
    
    
    
    





    
