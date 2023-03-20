import random as r
import tkinter as tk
import csv
import time


def get_lists():
    global questions_list, city, state
    questions_list = []
    city = []
    state = []
    raw_data = open("uscities.csv","r")

    questions_data = open("question-starters.txt","r")

    #start_time = time.time()
    for i in range(3):
        temp = questions_data.readline()
        temp = temp[:-1]
        questions_list.append(temp)
    
    del temp
    
    reader = csv.DictReader(raw_data)
    for col in reader:
        city.append(col["city"])
        state.append(col["state_name"])

    #end_time = time.time()
    #print(end_time-start_time)

class Question:
        def __init__(self):
            pass
        def create_question(self):
            self.index = 2
            self.string = str(questions_list[self.index-1])
            if self.index == 2:
                self.picked_index = r.randint(0,len(city))
                self.random_city = city[self.picked_index]
                self.state = state[self.picked_index]
                self.create_wrong_answers(self.state)
        def create_wrong_answers(self,correct_answer):
            self.list_of_wrong_answers = []
            if self.index == 2:
                for i in range(3):
                    j = r.randint(0,len(state))
                    if j == self.picked_index:
                        continue
                    k = state[j]
                    self.list_of_wrong_answers.append(k)

class Button:
        def __init__(self,root,correct,width=200,height=100,color=None):
            self.color = color
            self.correct = correct
            self.activecolor = None
            self.root = root
            pass
        def draw(self,t,c=0,r=0):
            if self.correct == False:
                a = "red"
            if self.correct == True:
                a = "green"
            self = tk.Button(self.root,text=t,font="Verdana",color=self.color,activebackground=a)
            self.grid(column=c,row=r)
        