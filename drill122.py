from tkinter import *
import tkinter.filedialog as fd


def selectDir():
    dirName = fd.askdirectory()
    if dirName:
        selection.set(dirName)
        txtPath.delete("1.0", END)
        txtPath.insert("1.0", dirName)

def userInput(status,name):
    masterFrame = Frame(root)
    masterFrame.pack()
    root.title("Directory Search")
    root.geometry('{}x{}'.format(500, 50))
    root.resizable(width=False, height=False)
    
    masterLabel = Label(masterFrame)
    masterLabel["text"] = name
    masterLabel.pack(side = LEFT, pady= 10)
        
    text = status
    selection = StringVar(root)
    selection.set(text)
        
    txtPath = Text(masterFrame, height=1, width=40)
    txtPath.pack(side = LEFT, padx = 5, pady= 10)

    btnBrowse = Button(masterFrame, text = "Browse...", command = selectDir)
    btnBrowse.pack(side = RIGHT, pady= 10)
        
    return txtPath, selection


if __name__ == '__main__':
    root = Tk()
    txtPath, selection = userInput("", "Directory Path:")
    root.mainloop()
