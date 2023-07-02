from tkinter import *
import tkinter.messagebox
import mysql.connector
import time
from functions import topmenu,raise_fram
from PIL import ImageTk, Image

def open_sidem(): 
    top2 = Toplevel()
    top2.title("sidemenu")
    top2.geometry("200x300")
    
    button = Button(top2, text = "log out",command = lambda:raise_fram(main))
    button.place(x=100,y = 280 )
     
    top2.mainloop()

def login_varify():
    user_varify = username.get()
    pas_varify = password.get()
    sql = "select * from login where username = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            tkinter.messagebox.showinfo("Sucsess!",  "log in sucsessful")
            raise_fram(home)
            break
    else:
        tkinter.messagebox.showinfo("error!",  "username or password is invalid")
        time.sleep(1)
        top.destroy()
    
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
        sql = "insert into login values(%s,%s,%s,%s)"
        t = (username_info, password_info, email_info, name_info)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.50)
        tkinter.messagebox.showinfo("Sucsess",  "user regesitered")

top = Tk()
top.rowconfigure(0,weight = 1)
top.columnconfigure(0,weight = 1)
top.geometry("1374x1018")
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="project")
mycur = db.cursor()

sidemenu = PhotoImage(file = r"C:\Users\frame\OneDrive\Desktop\python\project backup\main project\menu.png")
logo = ImageTk.PhotoImage(Image.open("C:\Users\frame\OneDrive\Desktop\python\project backup\main project\logo.png"))

main = Frame(top)
log = Frame(top)
register = Frame(top)
home = Frame(top)
f2 = Frame(top)
f3 = Frame(top)
f4 = Frame(top)

c1 = Canvas(main,bg= "black",height=1018, width=1374)
c2 = Canvas(log,height=1018, width=1374)
c3 = Canvas(register,height=1018, width=1374)
c4 = Canvas(home,height=1018, width=1374)
c5 = Canvas(f2,height=1018, width=1374)
c6 = Canvas(f3,height=1018, width=1374)
c7 = Canvas(f4,height=1018, width=1374)

username = StringVar()
password = StringVar()
name = StringVar()
email = StringVar()

for frame in (log,register,main):
    frame.grid(row=700, column=500, sticky='news')
    Label(frame,bg="black",foreground="#FFD700",text = "AUCTION",font=("comic sans ms",20),justify = "center").place(x =600,y=5)
    l = Label(frame,image=logo,bd=0)
    l.image = logo
    l.place(x = 400,y = 100)

for frame in (home, f2, f3, f4):
    frame.grid(row=700, column=500, sticky='news')
    Label(frame,text = "AUCTION",font=("comic sans ms",20),justify = "center").place(x =600,y=5)
    Button(frame, image = sidemenu,bd = 1,command=open_sidem).place(x = 12,y=6)

for can in (c1,c2,c3,c4,c5,c6,c7):
    topmenu(can)


Button(main,bg="#323234",foreground="#FFD700",bd=0,text="register",width=10 , height=3,font="bold 25",command=lambda:raise_fram(register)).place(x = 400,y = 500)
Button(main,bg="#323234",foreground="#FFD700",bd=0,text="Log-in",width=10 , height=3,font="bold 25",command=lambda:raise_fram(log)).place(x = 800,y = 500)

Label(log, text="Username :", font="bold 20").place(x =550,y=350)
Entry(log,font="bold 20",textvariable=username).place(x =550,y=380)
Label(log, text="Password :",font="bold 20").place(x =550,y=450)
Entry(log,font="bold 20",textvariable=password, show="*").place(x =550,y=480)
Button(log, text="Log-In",font="bold 20", bg="red",command=login_varify).place(x = 650,y = 550)
Button(log,text="back to maile=en page",activeforeground="#0000FF",bd= 0,command = lambda:raise_fram(main)).place(x = 650,y = 620)

Label(register,text="NAME :",font="bold 20").place(x =650,y=350)
Entry(register,textvariable=name).place(x =650,y=390)
Label(register, text="E-MAIL :",font="bold 20").place(x =650,y=430)
Entry(register, textvariable=email).place(x =650,y=470)
Label(register,text="USERNAME",font="bold 20").place(x =650,y=510)
Entry(register, textvariable=username,).place(x =650,y=550)
Label(register,text="PASSWORD",font="bold 20").place(x =650,y=590)
Entry(register, textvariable=password,show="*").place(x =650,y=630)
Button(register,text="register",font="bold 20", bg="red",command=register_user).place(x =700,y=670)
Button(register,text="back to main page",activeforeground="#0000FF",bd= 0,command = lambda:raise_fram(main)).place(x = 700,y = 750)

cat1 = Button(home, text="category 1", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=350,y= 600)
cat2 = Button(home, text="category 2", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=650,y= 600)
cat3 = Button(home, text="category 3", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=950,y= 600)
cat4 = Button(home, text="category 4", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=350 ,y= 800)
cat5 = Button(home, text="category 5", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=650,y= 800)
cat6 = Button(home, text="category 6", font = ("comic sans ms",11) , bg ="#ff8c42" ,fg ="white" , height = 3 , width =18 ).place(x=950,y= 800)
tb = Entry(home, height=1, width=30, bg='white', font=("Bookman Old Style", 30))
tb.place(x=350, y=400)

raise_fram(main)
c1.pack()
c2.pack()
c3.pack()
c4.pack()
top.mainloop()
