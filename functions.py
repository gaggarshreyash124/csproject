from tkinter import *
import tkinter.messagebox
import mysql.connector
import time
from PIL import ImageTk, Image


def topmenu(canva):
    
    line = canva.create_line(0,65,1374,65,fill ='#FFD700')
    profilepic = canva.create_oval(1300, 60, 1354, 5,fill = '#FFD700')


def raise_fram(fram):
    fram.tkraise()
