import socket
import sys
from tkinter import *
import time


class client:

    PORT = 6011
    ip = '192.168.1.9'
    ADDR = (ip,PORT)


    def __init__(self,frame):
        self.frame = frame
        self.GUI()
        self.tcp_connection()
       
    #simple GUI for testing
    def GUI(self):
        self.message = Message(self.frame,text = "this is a message", width = 200)
        self.message.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5)

    def tcp_connection(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.connect(self.ADDR)
        
       # while True:
        m = self.tcp_socket.recv(4096)
        m = m.decode('utf-8')   
        print(m)
        self.message.configure(text = m)





frame = Tk()

client(frame)
frame.mainloop()