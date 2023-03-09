import tkinter as tk

root = tk.Tk()

height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.title("Where Are You!")

screen = tk.Canvas(root,width=width,height=height,bg="white")
screen.grid(columnspan=10,rowspan=10)

title_text = tk.Label(root,text="Test your Geography Skills Here!",font="Verdana")
title_text.grid(columnspan=10,row=0)

root.mainloop()