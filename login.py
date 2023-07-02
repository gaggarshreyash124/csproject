from tkinter import *
import mysql.connector
import tkinter.messagebox


top = Tk()  
top.geometry("700x500")
c = Canvas(top,height=500, width=700)
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="project")
mycur = db.cursor()
# the label for user_name

line = c.create_line(0,60,1000,60,fill ='black')
profilepic = c.create_oval(630, 55, 680, 5,fill = 'black')
sidemenu = c.create_oval(12, 55, 60, 5,fill = 'black')

def raise_fram(fram):
    fram.tkraise()

def login_varify():
    user_varify = username.get()
    pas_varify = password.get()
    sql = "select * from users where username = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            tkinter.messagebox.showinfo("Sucsess!",  "log in sucsessful")
            raise_fram()
            break
username = StringVar()
password = StringVar()

name_heading = Label(top,text = "AUCTION",font=("comic sans ms",20),justify = "center").place(x =270,y=5)
Label(top, text="Username :", font="bold").place(x =300,y=100)
Entry(top,textvariable=username).place(x =300,y=120)
Label(top, text="Password :",font = "bold").place(x =300,y=150)
Entry(top,textvariable=password, show="*").place(x =300,y=170)
Button(top, text="Log-In", bg="red").place(x =300,y=210)



c.pack()
top.mainloop()
