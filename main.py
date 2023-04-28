import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
import major_zones
import threading
from threading import *
import major_zones
from major_zones import create_ui, tick_time, thread_ended, picked_process, counter

root = tk.Tk()

def start_thread():
    global active_counter
    active_counter = Thread(target=tick_time,args=(0,2))
    active_counter.start()

start_thread()

def open_main():
    height = 600
    width = 800
    logo = Image.open("logo.png")
    logo = ImageTk.PhotoImage(logo)
    root.iconphoto(False,logo)
    root.title("Where Are You!")

    screen = tk.Canvas(root,width=width,height=height,bg="white")
    screen.grid(columnspan=6, rowspan=6)

    title_text = tk.Label(root,text="Test your US Geography Skills Here!",font=("Verdana",30),bg="White")
    title_text.grid(columnspan=10,column=0,row=0)

    prompt = tk.Label(root,text="Select a difficulty and click Start to begin",font=("Verdana",20),bg="White")
    prompt.grid(columnspan=10,column=0,row=1)


    def open_new():
        if drop_text.get() != "Select a difficulty:":
            #screen.after(1,trans())
            diff = drop_text.get()
            create_ui(diff)

    drop_text = StringVar()
    drop_text.set("Select a difficulty:")
    options = ["easy","medium","hard"]
    time_drop = tk.OptionMenu(root,drop_text,*options)
    time_drop.grid(column=2,row=2)

    major_zones_text = tk.StringVar()
    major_zones_text.set("Start Game")
    major_zones_btn = tk.Button(root)
    if drop_text.get() == "Select a difficulty:":
        major_zones_btn = tk.Button(root, textvariable = major_zones_text, font="Verdana", command=lambda:open_new(), state=DISABLED)
    major_zones_btn = tk.Button(root, textvariable = major_zones_text, font="Verdana", command=lambda:open_new(), state=NORMAL)
    major_zones_btn.grid(column=2,row=3)

    # global active_counter
    # active_counter = Thread(target=tick,args=(0,"increment",))
    # active_counter.start()

    if thread_ended:
        picked_process.join()
        #active_counter.join()
        #print("Game has been running for {second} seconds.".format(seconds=counter))

    global end_game
    def end_game():
        #active_counter.join()
        print("Game has been running for {second} seconds.".format(second=counter))
        quit()

open_main()

# if root.destroy():
root.protocol("WM_DELETE_WINDOW",end_game)

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
# https://stackoverflow.com/questions/24050068/tkinter-making-classes-for-buttons-and-labels
# (^^^ above link for inheriting tkinter button class)
#