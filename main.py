###############################
#
# APCSP
# Period 3
#
# This is a game built using Tkinter
# that quizzes knowledge on US Cities
#
# Dependencies (for all three files): tkinter, Image, ImageTK,
# threading, major_zones, useful_functions,
# time, sys, random, csv
#
###############################

# Import the modules
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from threading import *
import major_zones
import useful_functions as lib

# Create the object that houses the entire game
root = tk.Tk()

# Starts the active counter thread that counts
# how long the application is running for
def start_thread():
    global active_counter
    active_counter = Thread(target=lib.tick_time,args=(2,))
    active_counter.start()

start_thread()

# The main function
def open_main():

    # Specifies the main screen properties
    height = 600
    width = 800
    logo = Image.open("logo.png")
    logo = ImageTk.PhotoImage(logo)
    root.iconphoto(False,logo)
    root.title("Where Are You!")

    # Creates the main screen with those properties.
    screen = tk.Canvas(root,width=width,height=height,bg="white")
    screen.grid(columnspan=6, rowspan=6)

    # Title screen
    title_text = tk.Label(root,text="Test your US Geography Skills Here!",font=("Verdana",30),bg="White")
    title_text.grid(columnspan=10,column=0,row=0)

    # Tells the user how to start the game
    prompt = tk.Label(root,text="Select a difficulty and click Start to begin",font=("Verdana",20),bg="White")
    prompt.grid(columnspan=10,column=0,row=1)

    # Opens a new game window passing the 
    # selected difficulty for the timer
    def open_new():
        if drop_text.get() != "Select a difficulty:":
            diff = drop_text.get()
            major_zones.create_ui(diff)

    # Creates the dropdown that allows the user to
    # select the three difficulty levels available:
    # easy, medium, and hard
    drop_text = StringVar()
    drop_text.set("Select a difficulty:")
    options = ["easy","medium","hard"]
    time_drop = tk.OptionMenu(root,drop_text,*options)
    time_drop.grid(column=2,row=2)

    # Creates the button that starts the game.
    # The button is disabled when no difficulty
    # level is selected, reminding the user to
    # select a difficulty before starting
    start_text = tk.StringVar()
    start_text.set("Start Game")
    start_btn = tk.Button(root)
    if drop_text.get() == "Select a difficulty:":
        start_btn = tk.Button(root, textvariable = start_text, font="Verdana", command=lambda:open_new(), state=DISABLED)
    start_btn = tk.Button(root, textvariable = start_text, font="Verdana", command=lambda:open_new(), state=NORMAL)
    start_btn.grid(column=2,row=3)

    # If timer thread has run out, it
    # will merge with the main thread
    if lib.thread_ended:
        major_zones.time_thread.join()

    # Function for when the "X" button at top right is pressed
    global end_game
    def end_game():
        # Prints the number of seconds and quits the application
        print("You\'ve been playing for {second} seconds. Keep up the good work!".format(second=lib.counter))
        quit()

open_main()

# Event handler for the "X" button
root.protocol("WM_DELETE_WINDOW",end_game)

# Starts the game
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