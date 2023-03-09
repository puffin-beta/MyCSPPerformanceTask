import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

height = root.winfo_screenheight()
width = root.winfo_screenwidth()
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
root.iconphoto(False,logo)
root.title("Where Are You!")

screen = tk.Canvas(root,width=width,height=height,bg="white")
screen.grid(columnspan=10, rowspan=10)

title_text = tk.Label(root,text="Test your Geography Skills Here!",font=("Verdana",40),bg="White")
title_text.grid(columnspan=10,column=0,row=0)

prompt = tk.Label(root,text="Click one of the options to begin",font=("Verdana",20),bg="White")
prompt.grid(columnspan=10,column=0,row=1)
major_zones_text = tk.StringVar()
major_zones_text.set("America, Canada, and India")
major_zones_btn = tk.Button(root, textvariable = major_zones_text, font="Verdana")
major_zones_btn.grid(column=1,row=2)

other_zones_text = tk.StringVar()
other_zones_text.set("Other Countries")
other_zones_btn = tk.Button(root, textvariable = other_zones_text, font="Verdana")
other_zones_btn.grid(column=4,row=2)

root.mainloop()