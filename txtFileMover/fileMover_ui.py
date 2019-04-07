from tkinter import *
import tkinter as tk

import fileMover_main
import fileMover_func

def loadUI(self):  
    ## The label, text box, and button for the source directory
    self.lbl_sourceDir = Label(self.master, text="Source Folder:")
    self.lbl_sourceDir.grid(row=0, column=0, padx=5, pady=10, sticky=W)
    txt_sourceDir = Text(self.master, height=1, width=35)
    txt_sourceDir.grid(row=0, column=1, padx=5, pady=10, sticky=W)
    btn_sourceDir = Button(self.master, text="Browse...", command= lambda: fileMover_func.sourceDir(txt_sourceDir))
    btn_sourceDir.grid(row=0, column=2, padx=5, pady=10, sticky=W)

    ## The label, text box, and button for the destination directory
    lbl_destinationDir = Label(self.master, text="Destination Folder:")
    lbl_destinationDir.grid(row=1, column=0, padx=5, pady=10, sticky=W)
    txt_destinationDir = Text(self.master, height=1, width=35)
    txt_destinationDir.grid(row=1, column=1, padx=5, pady=10, sticky=W)
    btn_destinationDir = Button(self.master, text="Browse...", command= lambda: fileMover_func.destinationDir(txt_destinationDir)) 
    btn_destinationDir.grid(row=1, column=2, padx=5, pady=10, sticky=W)

    ## Label and button for file transfer
    lbl_transferFiles = Label(self.master, text="Click to move all .txt files from the source folder, to the destination folder.")
    lbl_transferFiles.grid(row=2, column=0, columnspan=2, padx=5, sticky=W)    
    btn_transferFiles = Button(self.master, text="Transfer Files", fg="red", command= lambda: fileMover_func.transferFiles(txt_sourceDir, txt_destinationDir))
    btn_transferFiles.grid(row=2, column=2, padx=5, pady=10, sticky=W)

if __name__ == "__main__":
    pass
