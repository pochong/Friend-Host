from tkinter import *
import threading
import socket

class Chatroom:
    def __init__(self, frame, username, ADDR):
        self.frame = frame
        self.username = username
        self.ADDR = ADDR

    #function for text entry displays in chat room
    def sendText(self):

        mes = bytes(self.text_entry.get(), 'utf-8')
        try:
            self.tcp_socket.send(mes)
            print("Message Sent")
        except:
            print("Failed to send message")
        """
        try:
            response = self.tcp_socket.recv(4096)
            if(response == b'received'): 
                print("response received")
        except:
            print("Failed to receive Response")
        """
        self.chat_room.insert(END, self.username + " : " + self.text_entry.get() + "\n")
        self.text_entry.delete(0, END)

    def update_chat_room(self):
        
        #TODO: 
        
        while True: 
            try:
                mes = self.tcp_socket.recv(4096)
                s = mes.decode("utf-8")
                self.chat_room.insert(END, self.username + " : " + s + "\n")
                self.text_entry.delete(0, END)
            except: 
                 print("Failed to update chat room")
                 exit(0)
        


    #Initialization of all the functionalities. 
    def initialize(self): 
        #Initialize a thread to wait for messages from other clients.
        threading.Thread(target=self.update_chat_room).start()

    
    
    def chatroom_UI(self):
         #the Right frame of the GUI
        self.subframe = Frame(self.frame, width = 170, height = 380, bg = 'lightgrey')
        self.subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

        #Chat room Text display
        self.chat_room = Text(self.subframe, width = 30, height = 19)
        self.chat_room.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.text_entry = Entry(self.subframe, width = 30)
        self.text_entry.grid(row = 1, column = 0, padx = 5, pady = 5)   
    
        #send button to send / show message in chat room
        self.send_btn = Button(self.subframe, text = 'Send', width = 8, command=self.sendText)
        self.send_btn.grid(row = 2, column = 0, padx = 5, pady = 5)

        #press ENTER to send message
        self.text_entry.bind('<Return>', self.sendText)


    def tcp_connection(self):
            self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.tcp_socket.connect(self.ADDR)
            threading.Thread(target=self.initialize).start()
