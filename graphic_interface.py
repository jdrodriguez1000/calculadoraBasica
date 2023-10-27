from tkinter import *

class Graphic_Interface:
    
    def __init__(self) -> None:
        
        self.root = Tk()
        
        self.myframe = Frame(self.root, padx=10, pady=10)
        self.myframe.pack()
        
        self.lblnumber1 = Label(self.myframe, text="Ingrese el primer numero: ")
        self.lblnumber1.grid(row=0, column=0, padx=4, pady=5)
        self.lblnumber1.config(font=('Verdana', 9))
        
        self.entnumber1 = Entry(self.myframe)
        self.entnumber1.grid(row=1, column=0, pady=5)
        self.entnumber1.config(justify='center', font=('Verdana', 14))
        
        
        
        
        self.root.mainloop()
        

#Interface1 = Graphic_Interface()