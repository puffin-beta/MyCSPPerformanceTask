import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r
import time
from threading import Thread, Event
import sys

picked_process = None

def create_ui(timer):
    global subroot
    subroot = tk.Tk()
    
    lib.get_lists()

    subroot.title("GAME WINDOW")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=10,rowspan=10)

    def make_question():

        q1 = Question()
        q1.create_question()

        final_str = q1.string[:13] + ' ' + q1.random_city + q1.string[13:]
        label = tk.Label(subroot,text=final_str,font=("Verdana",20),bg="White")
        label.grid(column=0,row=0)

        answers = list(range(4))
        right_answer_index = r.randint(0,3)
        temp_count = 0
        for i in range(len(answers)):
            if i != right_answer_index:
                answers[i] = q1.list_of_wrong_answers[temp_count]
                temp_count += 1
            else:
                continue
        answers[right_answer_index] = q1.state

        def evaluate_answer(IsCorrect,correct_option):
            if IsCorrect == "True":
                print("Correct")
            elif IsCorrect == "False":
                print("Wrong. the correct answer is {correct}".format(correct=correct_option))
            
            answered.set()
            my_button.destroy()
            my_button2.destroy()
            my_button3.destroy()
            my_button4.destroy()
            label.destroy()
            lib.time_label.destroy()
            make_question()
            
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

        global answered
        answered = Event()

        global tick_time
    
        time_left = ''
        if timer == "easy":
            time_left = 45
        elif timer == "medium":
            time_left = 30
        elif timer == "hard":
            time_left = 20
        
        global time_thread
        time_thread = Thread(target=lib.tick_time,args=(1,time_left,subroot,answered,))
        time_thread.start()

        def end_game():
            subroot.destroy()
        subroot.protocol("WM_DELETE_WINDOW",end_game)
        if lib.thread_ended:
            end_game()
        
    make_question()

    subroot.mainloop()