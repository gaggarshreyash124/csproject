from tkinter import *
from PIL import ImageTk , Image


root = Tk()
root.geometry("1374x1018")
root.title("")
root.configure(bg="#F5F5DC")


home_frame = Frame(root , height = 1370 , width = 2000 , bg ="#F5F5DC")
home_frame.grid(row = 0 , column = 0 , sticky="nsew")
home_frame.tkraise()

#BUTTONS

cat1 = Button(home_frame , text="category 1", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=350,y= 600)
cat2 = Button(home_frame , text="category 2", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=650,y= 600)
cat3 = Button(home_frame , text="category 3", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=950,y= 600)
cat4 = Button(home_frame , text="category 4", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=350 ,y= 800)
cat5 = Button(home_frame , text="category 5", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=650,y= 800)
cat6 = Button(home_frame , text="category 6", font = ("comic sans ms",11) , bg ="#ff8c42" , command = home_frame.tkraise ,fg ="white" , height = 3 , width =18 ).place(x=950,y= 800)

tb = Text(home_frame, height=1, width=30, bg='white', font=("Bookman Old Style", 30))
tb.place(x=350, y=400)


root.mainloop()
