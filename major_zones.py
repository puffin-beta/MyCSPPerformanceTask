import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r

def create_ui():
    subroot = tk.Tk()
    
    lib.get_lists()

    subroot.title("GAME WINDOW")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=10,rowspan=10)

    q1 = Question()
    q1.create_question()

    final_str = q1.string[:13] + ' ' + q1.random_city + q1.string[13:]
    label = tk.Label(subroot,text=final_str,font=("Verdana",20),bg="White")
    label.grid(column=0,row=0)

    answer_btn = Button(subroot,True)
    answer_btn.draw(q1.state,0,1)
    for j in range(3):
        btn = Button(subroot,False)
        btn.draw(q1.list_of_wrong_answers[j],0,j+2)

    subroot.mainloop()