import tkinter as tk
from tkinter import *
import init_lists as init
import random as r

def create_ui():
    main_file = "uscities.csv"

    subroot = tk.Tk()
    
    init.get_lists()

    subroot.title("MAJOR ZONES!")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=4,rowspan=4)

    class Question:
        def __init__(self):
            pass
        def create_question(self):
            question = str(init.questions_list[0])
        
    print(init.questions_list)
    subroot.mainloop()