import tkinter
from tkinter import *


class ParentWindow(Frame): 
    def __init__ (self, master): 
        Frame.__init__(self)        

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(510, 160))
        self.master.title('Check files')
        self.master.config(bg='whitesmoke')



        self.txtBrowse1 = Entry(self.master, text='',width=40, font=('Helvetica', 12))
        self.txtBrowse1.grid(row=0, column=1, padx=(5,15), pady=(30,0), sticky=N)
        

        self.txtBrowse2 = Entry(self.master, text='',width=40, font=('Helvetica', 12)) 
        self.txtBrowse2.grid(row=1, column=1, padx=(5,15), pady=(10,0), sticky=N)
        

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(15,15), pady=(30,0), sticky=W)


        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(15,15), pady=(10,0), sticky=W)


        self.btnCkFiles = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCkFiles.grid(row=2, column=0, padx=(15,15), pady=(10,10), sticky=W)


        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btnClose.grid(row=2, column=1, padx=(15,15), pady=(10,10), sticky=E)


    def close(self):
        self.master.destroy() 
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() 


    
    
