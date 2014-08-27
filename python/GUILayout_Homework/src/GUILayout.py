""" GUILayout module for Lesson 7 """
from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    
    def __init__(self, master=None):
        """ Builds a window layout, as shown in the assignment, with 
            three frames and five buttons
        """
        
        # Main frame
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        #Rows
        for r in range(2):
            self.rowconfigure(r, weight = 1)     
        
        # Frames
        frame1 = Frame(self)
        frame1.grid(row = 0, column = 0, columnspan = 2, sticky = ALL)
        frame1.rowconfigure(0, weight = 1)
        frame1.columnconfigure(0, weight = 1)
        label1 = Label(frame1, text = "Frame 1", bg = "blue", fg = "white")
        label1.grid(sticky = ALL)
        
        frame2 = Frame(self)
        frame2.grid(row = 1, column = 0, columnspan = 2, sticky = ALL)
        frame2.rowconfigure(0, weight = 1)
        frame2.columnconfigure(0, weight = 1)
        label2 = Label(frame2, text = "Frame 2", bg = "green", fg = "black")
        label2.grid(sticky = ALL)
                
        frame3 = Frame(self)
        frame3.grid(row = 0, column = 2, rowspan = 2, columnspan = 3, sticky = ALL)
        frame3.rowconfigure(0, weight = 1)
        frame3.columnconfigure(0, weight = 1)
        label3 = Label(frame3, text = "Frame 3", bg = "yellow", fg = "black")
        label3.grid(sticky = ALL)
                
        # Buttons
        for c in range(5):
            self.columnconfigure(c, weight = 1)
            Button(self, text = "Button {0}".format(str(c + 1))).grid(row = 2, column = c, sticky = ALL)

root = Tk()
app = Application(master=root)
app.mainloop()