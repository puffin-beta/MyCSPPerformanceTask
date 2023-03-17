import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
import major_zones

root = tk.Tk()

def open_main():
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

    def open_new():
        root.destroy()
        major_zones.create_ui()

    major_zones_text = tk.StringVar()
    major_zones_text.set("America, Canada, and India")
    major_zones_btn = tk.Button(root, textvariable = major_zones_text, font="Verdana", command=lambda:open_new())
    major_zones_btn.grid(column=1,row=2)

    other_zones_text = tk.StringVar()
    other_zones_text.set("Other Countries")
    other_zones_btn = tk.Button(root, textvariable = other_zones_text, font="Verdana", command=lambda:open_new())
    other_zones_btn.grid(column=4,row=2)

open_main()

root.mainloop()

# Sources used log (for future benefit):
#
# https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv
#
# https://www.youtube.com/watch?v=itRLRfuL_PQ (basic tkinter functionality)
#
# https://www.youtube.com/watch?v=q2LI3w-RGL0 (add CSV to tkinter)
#
# https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
#
# https://www.tutorialspoint.com/python/tk_listbox.htm
# https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/
#
#
# https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
# (^^ above link for one code segment in major_zones.py)
#
# https://simplemaps.com/data/us-cities. (new database)
#
# https://java2blog.com/add-character-to-string-in-python/ (character substitution in string)
#