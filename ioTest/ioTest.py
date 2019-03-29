# Python drill for the Tech Academy

import os

filePath = "C:\\PythonProjects\\ioTest\\"

for txtFile in os.listdir(path = filePath):
    abPath = os.path.join(filePath, txtFile)
    if txtFile.endswith('.txt'):
        print(txtFile,os.path.getmtime(filePath))




