import socket
import sys
from tkinter import *
import time
import cv2
import mss
import numpy as np
from PIL import ImageTk, Image


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
        
        #the Left frame of the GUI 
        mainframe = Frame(self.frame, width = 500, height = 380, bg = 'lightgrey')
        mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)

        #start to capture screen HOWEVER IT DOESNT WORK !!!!
        def startStream():
            scene = mss.mss()
            screen = {"top": 40, "left": 0,"width":1000,"height":900}
            readscreen_ms = scene.grab(screen)
            readscreen_np = np.array(readscreen_ms)
            readscreen = Image.fromarray(readscreen_np)
            readscreen_tk = ImageTk.PhotoImage(image = readscreen)
            showscreen = Label(mainframe, image = readscreen_tk)               
            showscreen.pack()
            print("HI")
        
        #the Right frame of the GUI
        subframe = Frame(self.frame, width = 170, height = 380, bg = 'lightgrey')
        subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

        #Chat room Text display
        chat_room = Text(subframe, width = 30, height = 19)
        chat_room.grid(row = 0, column = 0, padx = 5, pady = 5)

        text_entry = Entry(subframe, width = 30)
        text_entry.grid(row = 1, column = 0, padx = 5, pady =5)
        
        #function for text entry displays in chat room
        def sendText(self):
            chat_room.insert(END, "User : " + text_entry.get() + "\n")
            text_entry.delete(0, END)
        
        #press ENTER to send message
        text_entry.bind('<Return>', sendText)

        #send button to send / show message in chat room
        send_btn = Button(subframe, text = 'Send', width = 8, command=sendText)
        send_btn.grid(row = 2, column = 0, padx = 5, pady = 5)

        #buttons frame to put buttons
        buttons_frame = Frame(self.frame, width = 500, height = 50, bg = 'lightgrey')
        buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 0)

        #start button
        start_btn = Button(buttons_frame, text = 'Start', width=8, command = startStream)
        start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

        #stop button
        stop_btn = Button(buttons_frame, text = 'Stop', width=8)
        stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        #mute button
        mute_btn = Button(buttons_frame, text = 'Mute', width=8)
        mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
        
    def tcp_connection(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.connect(self.ADDR)
        
       # while True:
        m = self.tcp_socket.recv(4096)
        m = m.decode('utf-8')   
        print(m)
        self.message.configure(text = m)


    

frame = Tk()
frame.config(bg = "LightBlue1")
client(frame)
frame.mainloop()