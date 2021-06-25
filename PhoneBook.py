import mysql.connector
from tkinter import *
from mysql.connector import Error

def getConnection(usr,passw,db):
    if connection.is_connected():
        return connection
    
fr=Frame()
fr.pack()
l1=Label(fr,text="Name")
l1.pack(side='top')
e1=Entry(fr)
e1.pack(side='top')
l2=Label(fr,text="Phone Number")
l2.pack(side='top')
e2=Entry(fr)
e2.pack(side='top')
def h1():
    global e1,e2
    connection = mysql.connector.connect(host='localhost',database='phonebook',user='root',password='',auth_plugin='mysql_native_password')
    cursor= connection.cursor()
    name=e1.get()
    phone=e2.get()
    query = "INSERT INTO phbook VALUES (%s,%s)"
    val = (e1.get(),e2.get())
    cursor.execute(query,val)
    connection.commit()
    query = "select * from phbook"
    cursor.execute(query)
    lst.delete(0,'end')
    for x in cursor.fetchall():
        w = str(x[0]) +" "*4+str(x[1])
        lst.insert('0',w)
    
def h3():
    global e1,e2
    connection = mysql.connector.connect(host='localhost',database='phonebook',user='root',password='',auth_plugin='mysql_native_password')
    cursor= connection.cursor()
    name=e1.get()
    phone=e2.get()
    query = "DELETE FROM phbook WHERE Name=%s or Phone=%s"
    val = (e1.get(),e2.get())
    cursor.execute(query,val)
    connection.commit()
    query = "select * from phbook"
    cursor.execute(query)
    lst.delete(0,'end')
    for x in cursor.fetchall():
        w = str(x[0]) +" "*4+str(x[1])
        lst.insert('0',w)
def h4():
    global e1,e2
    connection = mysql.connector.connect(host='localhost',database='phonebook',user='root',password='',auth_plugin='mysql_native_password')
    cursor= connection.cursor()
    name=e1.get()
    phone=e2.get()
    query = "select * from phbook"
    cursor.execute(query)
    lst.delete(0,'end')
    for x in cursor.fetchall():
        w = str(x[0]) +" "*4+str(x[1])
        lst.insert('0',w)

b1=Button(fr,text="ADD CONTACT",command=h1)
b3=Button(fr,text="DELETE CONTACT",command=h3)
b1.pack(side='top')
b3.pack(side='top')
b4=Button(fr,text="LOAD ALL CONTACTS",command=h4)
b4.pack(side='top')
lst=Listbox(fr,height = 10,width = 40)
scrll=Scrollbar(fr)
scrll.config(command=lst.yview)
lst.config(yscrollcommand=scrll.set)
scrll.pack(side='right',fill="y")
lst.pack(side='left')
lst.bind('<Double-1>',h5)
fr.mainloop()
