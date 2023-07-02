from tkinter import *
from PIL import ImageTk, Image

top = Tk()
top.geometry("700x500")
c = Canvas(top,height=500, width= 700)

image1 = Image.open("menu.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test
# the label for user_name

line = c.create_line(0,60,1000,60,fill ='black')
profilepic = c.create_oval(630, 55, 680, 5,fill = 'black')
sidemenu = c.create_oval(12, 55, 60, 5,fill = 'black')

Label(top,text = "search",font="bold 15").place(x=340,y=210) 
search = Entry(top,width=50).place(x=220,y=250)

label1.place(x=12, y=5)

c.pack()
top.mainloop()
