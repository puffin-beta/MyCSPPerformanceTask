import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r
import time

def create_ui(timer):
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

    answers = list(range(4))
    right_answer_index = r.randint(0,3)
    answers[right_answer_index] = q1.state
    temp_count = 0
    for i in range(4):
        if i != right_answer_index:
            answers[i] = q1.list_of_wrong_answers[temp_count]
            temp_count += 1
        else:
            continue
    #print(answers)
    
    for i in range(4):
        IsCorrect = None
        IsCorrect = True if answers[i] == q1.state else False
        answer_btn = Button(subroot,IsCorrect)
        answer_btn.draw(answers[i],0,i+1)
    
    timer = Timer(subroot,timer)
    timer.tick()
    
    subroot.mainloop()