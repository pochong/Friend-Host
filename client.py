import socket
import sys
from tkinter import *
import time
import cv2
import mss
import numpy as np
from PIL import ImageTk, Image
import cv2
import pickle
import struct
import threading


class client:

    PORT = 8004
    ip = '167.99.160.18'
    ADDR = (ip,PORT)
    username = "User0"

    def __init__(self,frame):
        self.frame = frame
        self.GUI()
        self.tcp_connection()


    #start to capture screen HOWEVER IT DOESNT WORK !!!!
    def startStream(self):
        self.scene = mss.mss()
        self.screen = {"top": 40, "left": 0,"width":1000,"height":900}
        self.readscreen_ms = scene.grab(self.screen)
        self.readscreen_np = np.array(self.readscreen_ms)
        self.readscreen = Image.fromarray(self.readscreen_np)
        self.readscreen_tk = ImageTk.PhotoImage(image = readscreen)
        self.showscreen = Label(mainframe, image = self.readscreen_tk)               
        self.showscreen.pack()
        print("HI")
       
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
        


    #Initialization of all the functionalities. 
    def initialize(self): 
        #Initialize a thread to wait for messages from other clients.
        threading.Thread(target=self.update_chat_room).start()


    #simple GUI for testing
    def GUI(self):
        
        self.Display = Label(self.frame, height=50,width = 200)
        self.Display.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5)
        
        #the Right frame of the GUI
        self.subframe = Frame(self.frame, width = 170, height = 380, bg = 'lightgrey')
        self.subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

        #Chat room Text display
        self.chat_room = Text(self.subframe, width = 30, height = 19)
        self.chat_room.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.text_entry = Entry(self.subframe, width = 30)
        self.text_entry.grid(row = 1, column = 0, padx = 5, pady =5)   
        
        #press ENTER to send message
        self.text_entry.bind('<Return>', self.sendText)

        #send button to send / show message in chat room
        self.send_btn = Button(self.subframe, text = 'Send', width = 8, command=self.sendText)
        self.send_btn.grid(row = 2, column = 0, padx = 5, pady = 5)

        #buttons frame to put buttons
        self.buttons_frame = Frame(self.frame, width = 500, height = 50, bg = 'lightgrey')
        self.buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 0)

        #start button
        self.start_btn = Button(self.buttons_frame, text = 'Start', width=8, command = self.startStream)
        self.start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

        #stop button
        self.stop_btn = Button(self.buttons_frame, text = 'Stop', width=8)
        self.stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        #mute button
        self.mute_btn = Button(self.buttons_frame, text = 'Mute', width=8)
        self.mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    
        
    
    def read_screen(self):
        ms = mss.mss()
        screen = {"top": 40, "left": 0,"width":1000,"height":900}
        while True:
            #capture screen pixel
            frame = ms.grab(screen)
            #cap = cv2.VideoCapture(0)
            #ret,frame = cap.read()
            #convert pixel to matrix and show it on cv2 
            #cv2.imshow('screen', np.array(frame))
            #print(readscreen_pil)
            #press q to quit

            data = pickle.dumps(frame) ### new code
            self.tcp_socket.sendall(struct.pack("L", len(data))+data) ### new code

            
            if cv2.waitKey(25) & 0XFF == ord('q'):
                cv2.destroyAllWindows()
                break
            

    def recv_screen(self):
        data = b''
        payload_size = struct.calcsize("L") 
        while True:
            while len(data) < payload_size:
                data += self.tcp_socket.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.tcp_socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            
            ###
            
            frame=pickle.loads(frame_data)
            f2 = open('frame1.jpg','wb')
            f2.write(frame)
            #print frame
            #cv2.imshow('frame',np.array(frame))
    

    def tcp_connection(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.connect(self.ADDR)
        
       # while True:
        m = self.tcp_socket.recv(4096)
        if m == b'host':
            #start a thread to send camera frame
            print("Go to read screen")
            #self.read_screen()
        else:
            print("Go to recv screen")
            #self.recv_screen()
        threading.Thread(target=self.initialize).start()



    

frame = Tk()
frame.config(bg = "LightBlue1")
client(frame)
frame.mainloop()