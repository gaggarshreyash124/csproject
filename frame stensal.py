from tkinter import *
import tkinter.messagebox
import mysql.connector
import time
from functions import topmenu,raise_fram
from PIL import ImageTk, Image

top = Tk()
top.geometry("700x500")
c = Canvas(top,height=500, width= 700)
   


line = c.create_line(0,60,1000,60,fill ='black')
profilepic = c.create_oval(630, 55, 680, 5,fill = 'black')
sidemenu = c.create_oval(12, 55, 60, 5,fill = 'black')





c.pack()
top.mainloop()
