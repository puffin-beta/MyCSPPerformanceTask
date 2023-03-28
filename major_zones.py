import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r
import time
import threading
import signal

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
        IsCorrect = ""
        if str(answers[i]) == str(q1.state):
            IsCorrect = True
        else:
            IsCorrect = False
        answer_btn = Button2(subroot)
        answer_btn.addCorrect(IsCorrect)
        answer_btn = Button2(subroot,text=answers[i],font="Verdana",bg="white",command=lambda:evaluate_answer(IsCorrect,q1.state))
        answer_btn.grid(column=0,row=i+1)
    
    #my_button = Button2(subroot,text="Hello")
    #my_button.grid(column=2,row=2)

    answered = threading.Event()

    def tick(max_time):
        while max_time > 0:
            time.sleep(1)
            max_time -= 1
            #print(max_time)
            time_label = tk.Label(subroot,text=str(max_time).zfill(2),font=("Verdana",30),bg="White")
            time_label.grid(column=4,row=0)
            if answered.is_set():
                break
        print("Timer loop exitted")
        #print("Time\'s Up! The correct answer is {0}.".format(q1.state))

    time_left = 0
    if timer == "easy":
        time_left = 45
    elif timer == "medium":
        time_left = 30
    elif timer == "hard":
        time_left = 20
    
    timer_thread = threading.Thread(target=tick,args=(time_left,))
    timer_thread.daemon = True
    timer_thread.start()

    def evaluate_answer(IsCorrect,correct_option):
        print(IsCorrect)


    subroot.mainloop()