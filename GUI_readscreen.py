from tkinter import *


window = Tk()
window.title("Read Screen")
window.config(bg = "LightBlue1")
#window.resizable()

mainframe = Frame(window, width = 500, height = 380, bg = 'lightgrey')
mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)

subframe = Frame(window, width = 170, height = 380, bg = 'lightgrey')
subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

#chat_room = Text(subframe, width = 160, height = 200)
#chat_room.grid(row = 0, column = 0, padx = 5, pady = 5)

#text_entry = Entry(subframe)
#text_entry.grid(row = 1, column = 0, padx = 5, pady =5)

buttons_frame = Frame(window, width = 500, height = 50, bg = 'lightgrey')
buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 0)

start_btn = Button(buttons_frame, text = 'Start', width=8)
start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

stop_btn = Button(buttons_frame, text = 'Stop', width=8)
stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

mute_btn = Button(buttons_frame, text = 'Mute', width=8)
mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)




window.mainloop()

