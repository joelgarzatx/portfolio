from tkinter import *
import sys

ALL = N+S+E+W
WIDE = E+W

class Application(Frame):    
    def __init__(self, master=None):
        """ Initialize the master frame for the Tkinter application """
        # main Frame
        Frame.__init__(self,master)
        self.configure
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        self.create_widgets()
        
    def create_widgets(self):
        """ Layout the widgets used in the interface, using grid() """
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
            
        self.rowconfigure(4, weight=0)
        
        # Buttons    
        but1 = Button(self,name="red",text="Red",command=self.change_text_red)
        but1.grid(row = 4, column = 0, sticky = WIDE)

        but2 = Button(self,name="blue",text="Blue",command=self.change_text_blue)
        but2.grid(row = 4, column = 1, sticky = WIDE)
        
        but3 = Button(self,name="green",text="Green",command=self.change_text_green)
        but3.grid(row = 4, column = 2, sticky = WIDE)
        
        but4 = Button(self,name="black",text="Black",command=self.change_text_black)
        but4.grid(row = 4, column = 3, sticky = WIDE)
        
        but5 = Button(self,name="open",text="Open",command=self.open_file)
        but5.grid(row = 4, column = 4, sticky = WIDE)
        
        # Frames           
        frame1 = Frame(self, name = "frame1", bg = "blue", width = 300)
        frame1.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = ALL)
        frame1.rowconfigure(0, weight = 1)
        frame1.columnconfigure(0, weight = 1)
        
        frame2 = Frame(self, name = "frame2", bg = "red", width = 300)
        frame2.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = ALL)
        frame2.rowconfigure(0, weight = 1)
        frame2.columnconfigure(0, weight = 1)
        
        frame3 = Frame(self, name = "frame3", bg = "yellow", width = 450)
        frame3.grid(row = 0, column = 2, rowspan = 4, columnspan = 3, sticky = ALL)
        frame3.rowconfigure(0, weight = 1)
        frame3.columnconfigure(0, weight = 1)
        
        frame4 = Frame(frame3, name = "frame4")
        frame4.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = ALL)
        frame4.rowconfigure(0, weight = 0)
        frame4.rowconfigure(1, weight = 1)
        frame4.columnconfigure(0, weight = 0)
        frame4.columnconfigure(1, weight = 1)        
        
        # Bind the primary mouse button to register clicks in frame 1 and frame 2
        frame1.bind("<Button-1>", self.handler)
        frame2.bind("<Button-1>", self.handler)
        
        # Entry widget and label used to enter a filename
        label1 = Label(frame4, name = "label1", text="Enter filename, click Open")
        label1.grid(row=0, column=0, sticky = WIDE)

        self.entry1 = Entry(frame4, name = "entry1")
        self.entry1.grid(row=0, column=1, sticky = WIDE)
             
        # Text widget used to present the contents of the file
        self.text1 = Text(frame4, name = "text1", wrap = WORD)
        self.text1.insert(0.0, "Click the open button to load a text file.")
        self.text1.grid(row = 1, column = 0, columnspan = 2, sticky = ALL)

        

    def handler(self,event):
        """ Prints to stdout the coordinates in the frame where clicked."""
        widgetname = event.widget.winfo_name().title()
        print("You clicked", widgetname, "at", event.x, event.y)
        
    def change_text_red(self):
        """ Changes the font color in the text widget to red. """
        self.text1.configure(fg = "red")
        
    def change_text_blue(self):
        """ Changes the font color in the text widget to blue. """
        self.text1.configure(fg = "blue")  
    
    def change_text_green(self):
        """ Changes the font color in the text widget to green. """
        self.text1.configure(fg = "green")
        
    def change_text_black(self):
        """ Changes the font color in the text widget to black. """
        self.text1.configure(fg = "black")       
        
    def open_file(self):
        """ Attempts to open a file using filename entered into 
            text entry widget. Catches errors and places an error message
            in the entry box.
        """
        filename = self.entry1.get()
        try:
            f = open(filename,'r')
        except Exception:
            self.entry1.delete(0, END)
            err_message = "".join(['"', filename, '" did not work, try again.'])
            self.entry1.insert(0, err_message)
            return
        else:
            s = f.read()
            f.close()
        self.text1.delete(0.0, END)
        self.text1.insert(0.0, s)
            

root = Tk()
app = Application(master=root)
app.mainloop()
