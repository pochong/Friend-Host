from tkinter import *


window = Tk()
window.title("Read Screen")
window.config(bg = "LightBlue1")

mainframe = Frame(window, width = 500, height = 420, bg = 'lightgrey')
mainframe.grid(row = 0, column = 0, padx = 10, pady = 5)

subframe = Frame(window, width = 170, height = 420, bg = 'lightgrey')
subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

#buttons_frame = Frame(window, width = 500, height = 50, bg = 'lightgrey')
#buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 5)



window.mainloop()

