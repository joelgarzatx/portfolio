from tkinter import *

def float_sum(a,b):
    try:
        op1 = float(a)
        op2 = float(b)
    except ValueError:
        result = "***ERROR***"
    else:
        result = op1 + op2
    return result
        
class Application(Frame):
    """ Application main window class """
    def __init__(self, master=None):
        """Main frame initialization"""
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        top_frame = Frame(self)
        self.operand_A = Entry(top_frame)
        self.operand_B = Entry(top_frame)
        self.operand_A.pack(side=LEFT)
        self.operand_B.pack(side=LEFT)
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        self.result = Label(bottom_frame, text="Result")
        self.add_nums = Button(bottom_frame, text="Calculate Sum", command=self.calculate)
        self.result.pack(side=TOP)
        self.add_nums.pack(side=TOP)
        bottom_frame.pack(side=TOP)
        
    def calculate(self):
        """ Convert operands to float and calculate the sum """
        self.result.config(text=float_sum(self.operand_A.get(),self.operand_B.get()))
        
root = Tk()
app = Application(master=root)
app.mainloop()
        