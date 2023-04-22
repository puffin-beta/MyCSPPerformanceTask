import random as r
import tkinter as tk
from tkinter import *
import csv
import time


def get_lists():
    global questions_list, city, state
    questions_list = []
    city = []
    state = []
    raw_data = open("uscities.csv","r")

    questions_data = open("question-starters.txt","r")

    for i in range(3):
        temp = questions_data.readline()
        temp = temp[:-1]
        questions_list.append(temp)
    
    del temp
    
    reader = csv.DictReader(raw_data)
    for col in reader:
        city.append(col["city"])
        state.append(col["state_name"])


def tick(max_time):
    while max_time > 0:
        time.sleep(1)
        max_time -= 1
        return max_time
    return 0

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
                    if state[j] in self.list_of_wrong_answers:
                        continue
                    else:
                        k = state[j]
                        self.list_of_wrong_answers.append(k)

class Button2(Button):
    def __init__(self,*args,**kwargs):
        Button.__init__(self,*args,**kwargs)
    def addCorrect(self,correct):
        self.correct = correct

# class Timer:
#     def __init__(self,root,difficulty):
#         self.difficulty = difficulty
#         self.max_time = 0
#         self.root = root
#         if self.difficulty == "easy":
#             self.max_time = 45
#         elif self.difficulty == "medium":
#             self.max_time = 30
#         elif self.difficulty == "hard":
#             self.max_time = 20
#     def tick(self):
#         startTime = time.time()
#         currentTime = startTime
#         while (currentTime - startTime < self.max_time):
#             temp = ""
#             currentTime = time.time()
#             deltaTime = int(self.max_time - (currentTime - startTime))
#             #print(deltaTime)
#             last_time = int(time.gmtime().tm_sec)
#             if (last_time - deltaTime >= 1) :
#                 last_time -= 1
#                 print(last_time)
#             #print(" ")
#             self.root.update()
#         print("Time is up")
#         #last_time = float(time.gmtime().tm_sec)

    
        