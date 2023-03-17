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
            global index
            index = 2
            string = str(init.questions_list[index-1])
            return string
        def find_content(self):
            if index == 2:
                picked_index = r.randint(0,len(init.city))
                self.random_city = init.city[picked_index]
                self.state = init.state[picked_index]
                return self.random_city

    q1 = Question()
    final_str = q1.create_question()[:13] + ' ' + q1.find_content() + q1.create_question()[13:]
    label = tk.Label(subroot,text=final_str,font=("Verdana",20),bg="White")
    label.grid(column=0,row=0)
    subroot.mainloop()