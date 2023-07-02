import tkinter as tk
from tkinter import font as tkFont
root = tk.Tk()


text = tk.Entry()
text.pack()

def underline():
    f = tkFont.Font(text, text.cget("font"))
    f.configure(underline = True)
    text.configure(font=f)


underline =tk.Button(root,text="underline",command=underline)
underline.pack()



root.mainloop()