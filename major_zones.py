import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r
import time
from threading import Thread, Event
import sys

def create_ui(timer):
    subroot = tk.Tk()
    
    lib.get_lists()

    subroot.title("GAME WINDOW")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=10,rowspan=10)

    global isTerminated
    isTerminated = False

    def make_question():

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

        def evaluate_answer(IsCorrect,correct_option):
            my_button.destroy()
            my_button2.destroy()
            my_button3.destroy()
            my_button4.destroy()
            label.destroy()
            time_label.destroy()
            answered.set()
            make_question()
            
            if IsCorrect == "True":
                print("Correct")
            elif IsCorrect == "False":
                print("Wrong")
            elif IsCorrect == "NULL":
                print("Not Answered")

    
        my_button_correct = ("True" if answers[0] == q1.state else "False")
        my_button = Button2(subroot,text=(answers[0]),font=("Verdana",15))
        my_button.addCorrect(my_button_correct)
        my_button['command'] = lambda:evaluate_answer(my_button_correct,q1.state)
        my_button.grid(column=0,row=2)

        my_button2_correct = ("True" if answers[1] == q1.state else "False")
        my_button2 = Button2(subroot,text=(answers[1]),font=("Verdana",15))
        my_button2.addCorrect(my_button_correct)
        my_button2['command'] = lambda:evaluate_answer(my_button2_correct,q1.state)
        my_button2.grid(column=0,row=3)

        my_button3_correct = ("True" if answers[2] == q1.state else "False")
        my_button3 = Button2(subroot,text=(answers[2]),font=("Verdana",15))
        my_button3.addCorrect(my_button_correct)
        my_button3['command'] = lambda:evaluate_answer(my_button3_correct,q1.state)
        my_button3.grid(column=0,row=4)

        my_button4_correct = ("True" if answers[3] == q1.state else "False")
        my_button4 = Button2(subroot,text=(answers[3]),font=("Verdana",15))
        my_button4.addCorrect(my_button_correct)
        my_button4['command'] = lambda:evaluate_answer(my_button4_correct,q1.state)
        my_button4.grid(column=0,row=5)

        answered = Event()

        def tick(max_time):
            global thread_ended
            thread_ended = False
            max = max_time
            while max > 0:
                if answered.is_set():
                    max = max_time
                    continue 
                time.sleep(1)
                max -= 1
                global time_label
                time_label = tk.Label(subroot,text=str(max).zfill(2),font=("Verdana",30),bg="White")
                time_label.grid(column=4,row=0)     
            print("Timer loop exitted")
            #time_label.after(1,time_label.destroy())
            thread_ended = True
            sys.exit()
            #del subroot
            #evaluate_answer("NULL",q1.state)
            
        time_left = ''
        if timer == "easy":
            time_left = 45
        elif timer == "medium":
            time_left = 30
        elif timer == "hard":
            time_left = 5
        
        picked_process = Thread(target=tick,args=(time_left,))
        picked_process.start()
        if thread_ended == True:
            picked_process.join()
            subroot.destroy()
        
    make_question()

    subroot.mainloop()