import sqlite3
from tkinter import *
from tkinter import messagebox
class DB:
    def __init__(self):
        self.con=sqlite3.connect("booksin.db")
        self.cursor=self.con.cursor()
        self.con.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,book_name TEXT,price INTEGER,aurthor TEXT,isbn INTEGER,category text,barcode TEXT)")

        self.con.commit()

    def __del_(self):
        self.con.close()

#Get All Books
    def books(self):
        self.cursor.execute("SELECT * FROM books")
        rows=self.cursor.fetchall() #get All Rows from database
        return rows
#Insert Data
    def insert(self,book_name,price,aurthor,isbn,category,barcode):
        self.cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?,?,?)",(book_name,price,aurthor,isbn,category,barcode))
        self.con.commit()
#Search Into DATABASE
    def search(self,book_name="",price="",aurthor="",isbn="",category="",barcode=""):
        self.cursor.execute("SELECT * FROM books WHERE book_name=? OR price=? OR aurthor=? OR isbn=? OR category=? OR barcode=?", (book_name,price,aurthor,isbn,category,barcode))
        found_rows=self.cursor.fetchall()
        return found_rows

#DELETE INTO DATABASE
    def delete(self,id):
        self.cursor.execute("DELETE FROM books WHERE id=?",str(id))
        self.con.commit()

#UPDATE INTO DATABASE
    def update(self,id,book_name,price,aurthor,isbn,category,barcode):
        self.cursor.execute("UPDATE books SET book_name=?,price=?,aurthor=?,isbn=?,category=?,barcode=? WHERE id=?",(book_name,price,aurthor,isbn,category,barcode,str(id)))




db=DB()        

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
   


def view_command():
    list1.delete(0,END)
    for row in db.books():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in db.search(book_name_text.get(),price_text.get(),aurthor_text.get(),isbn_text.get(),category_text.get(),barcode_text.get()):
        
        list1.insert(END,row)


def add_command():
    db.insert(book_name_text.get(),price_text.get(),aurthor_text.get(),isbn_text.get(),category_text.get(),barcode_text.get())
    list1.delete(0,END)
    list1.insert(END,(book_name_text.get(),price_text.get(),aurthor_text.get(),isbn_text.get(),category_text.get(),barcode_text.get()))

def update_command():
    db.update(selected_tuple[0],book_name_text.get(),price_text.get(),aurthor_text.get(),isbn_text.get(),category_text.get(),barcode_text.get())


    

def delete_command():
    db.delete(selected_tuple[0])



    


    
window=Tk()
window.title("Book  Form")

def on_closing():
    dd=db
    
    if messagebox.askokcancel("Exit","Are you sure?"):
        window.destroy()
        del dd

window.protocol("WM_DELETE_WINDOW",on_closing)


l1=Label(window,text="book_name")
l1.grid(row=0,column=0)

l2=Label(window,text="price")
l2.grid(row=0,column=2)

l3=Label(window,text="aurthor")
l3.grid(row=1,column=0)

l4=Label(window,text="isbn")
l4.grid(row=1,column=2)

l5=Label(window,text="category")
l5.grid(row=2,column=0)

l6=Label(window,text="barcode")
l6.grid(row=2,column=2)


book_name_text=StringVar()
e1=Entry(window,textvariable=book_name_text)
e1.grid(row=0,column=1)

price_text=StringVar()
e2=Entry(window,textvariable=price_text)
e2.grid(row=0,column=3)

aurthor_text=StringVar()
e3=Entry(window,textvariable=aurthor_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

category_text=StringVar()
e5=Entry(window,textvariable=category_text)
e5.grid(row=2,column=1)

barcode_text=StringVar()
e6=Entry(window,textvariable=barcode_text)
e6.grid(row=2,column=3)

list1=Listbox(window,height=5,width=55)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=4,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=5,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=6,column=3)

b4=Button(window,text="update Selected",width=12,command=update_command)
b4.grid(row=7,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=8,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=9,column=3)

window.mainloop()













        
