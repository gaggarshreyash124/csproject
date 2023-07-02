from tkinter import *
import tkinter.messagebox
import mysql.connector
import time

top = Tk()
top.geometry("700x500")
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="project")
mycur = db.cursor()
c = Canvas(top,height=500, width= 700)
   
# the label for user_name

line = c.create_line(0,60,1000,60,fill ='black')
profilepic = c.create_oval(630, 55, 680, 5,fill = 'black')
sidemenu = c.create_oval(12, 55, 60, 5,fill = 'black')

def register_user():
    username_info = username.get()
    password_info = password.get()
    name_info = name.get()
    email_info = email.get()
    if username_info == "":
        tkinter.messagebox.showinfo("error!",  "username not entered")
    elif password_info == "":
        tkinter.messagebox.showinfo("error!",  "password was not entered")
    elif name_info == "":
        tkinter.messagebox.showinfo("error!",  "name not entered")
    elif "@" not in email_info:
        tkinter.messagebox.showinfo("error!",  "email is not valid")
    elif email_info == "":
        tkinter.messagebox.showinfo("error!",  "email not entered")
    else:
        sql = "insert into login values(%s,%s.,%s,%s)"
        t = (username_info, password_info,email_info,name_info)
        mycur.execute(sql, t)
        db.commit()
        Label(top, text="").pack()
        time.sleep(0.50)
        tkinter.messagebox.showinfo("Sucsess",  "user regesitered")


username = StringVar()
password = StringVar()
name = StringVar()
email = StringVar()
Label(top,text="NAME :",font="bold").place(x =300,y=100)
Entry(top,textvariable=name).place(x =300,y=120)
Label(top, text="E-MAIL :",font="bold").place(x =300,y=150)
Entry(top, textvariable=email).place(x =300,y=170)
Label(top,text="USERNAME",font="bold").place(x =300,y=200)
Entry(top, textvariable=username,).place(x =300,y=220)
Label(top,text="PASSWORD",font="bold").place(x =300,y=250)
Entry(top, textvariable=password,show="*").place(x =300,y=270)
Button(top,text="register",command=register_user).pack()

c.pack()
top.mainloop()
