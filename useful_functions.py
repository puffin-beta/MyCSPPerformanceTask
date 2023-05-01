import random as r
import tkinter as tk
from tkinter import *
import csv
import time
import sys


def get_lists():
    global questions_list, city, state
    questions_list = []
    raw_data = open("uscities.csv","r")

    questions_data = open("question-starters.txt","r")

    state = []
    city = []
    for i in range(3):
        temp = questions_data.readline()
        temp = temp[:-1]
        questions_list.append(temp)
    
    del temp
    
    reader = csv.DictReader(raw_data)
    for col in reader:
        city.append(col["city"])
        state.append(col["state_name"])

def tick_time(method,max_time=None,page=None,eventHandle=None):
    answered = eventHandle
    subroot = page
    global thread_ended
    thread_ended = False
    max = max_time
    if method == 1:
        if not thread_ended:
            while max > 0:
                if answered.is_set():
                    max = max_time
                    continue 
                time.sleep(1)
                max -= 1
                global time_label
                time_label = tk.Label(subroot,text=str(max).zfill(2),font=("Verdana",30),bg="White")
                time_label.grid(column=4,row=0)     
            print("Timer loop exitted. Game is Over")
            thread_ended = True
            time_label.destroy()
            subroot.destroy()
            sys.exit(1)
    elif method == 2:
        global counter
        counter = 0
        while True:
            time.sleep(1)
            counter += 1

class Question:
        def __init__(self):
            pass
        def create_question(self):
            self.index = 2
            self.string = str(questions_list[self.index-1])
            self.picked_index = r.randint(0,len(city))
            self.random_city = city[self.picked_index]
            self.state = state[self.picked_index]
            self.create_wrong_answers(self.state)
        def create_wrong_answers(self,correct_answer):
            self.list_of_wrong_answers = []
            for i in range(3):
                j = r.randint(0,len(state))
                if state[j] in self.list_of_wrong_answers:
                    continue
                else:
                    wrong_answer = state[j]
                    self.list_of_wrong_answers.append(wrong_answer)

class Button2(Button):
    def __init__(self,*args,**kwargs):
        Button.__init__(self,*args,**kwargs)
    def addCorrect(self,correct):
        self.correct = correct
