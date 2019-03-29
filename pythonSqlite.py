import sqlite3
import os


conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE tbl_stuff(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_names STRING)")
    
conn.commit()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for txtFile in fileList:
    if txtFile.endswith('.txt'):  
        print(txtFile)
        cur.execute("INSERT INTO tbl_stuff(col_names) VALUES (?)", (txtFile,))
   
conn.commit()

conn.close()



