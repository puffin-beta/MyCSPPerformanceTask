
# Import the modules
import random as r
import tkinter as tk
from tkinter import *
import csv
import time
import sys

# This function is responsible for loading all the necessary
# city names, their corresponding states, and the question to 
# quiz the user.
def get_lists():
    global questions_list, city, state
    
    # opens the raw CSV data
    raw_data = open("uscities.csv","r")

    # reads the question frames from the 
    # txt file
    questions_list = []
    questions_data = open("question-starters.txt","r")
    for i in range(3):
        temp = questions_data.readline()
        temp = temp[:-1]
        questions_list.append(temp)
    
    # Deletes unnecessary data
    del temp

    # Where citis and states are copied from the CSV
    # into their respective lists
    state = []
    city = []
    reader = csv.DictReader(raw_data)
    for col in reader:
        city.append(col["city"])
        state.append(col["state_name"])

# This function is responsible for the timer and for the 
# active counter
def tick_time(method,max_time=None,page=None,eventHandle=None):

    # loads all the necessary variables for each functionality
    answered = eventHandle
    subroot = page
    global thread_ended
    thread_ended = False
    max = max_time

    # The timer functionality
    if method == 1:

        # Thread is active
        if not thread_ended:

            # the timer loop
            while max > 0:

                # If answer is selected
                if answered.is_set():
                    max = max_time
                    continue 
                
                # decrements max and displays it on a label
                time.sleep(1)
                max -= 1
                global time_label
                time_label = tk.Label(subroot,text=str(max).zfill(2),font=("Verdana",30),bg="White")
                time_label.grid(column=4,row=0)

            # When the timer runs out     
            print("Timer loop exitted. Game is Over")
            thread_ended = True
            time_label.destroy()
            subroot.destroy()
            sys.exit(1) # System exits out of this specific program and not out of the main program

    # The active counter functionality
    elif method == 2:
        # Increments counter until program is manually
        # stopped by user
        global counter
        counter = 0
        while True:
            time.sleep(1)
            counter += 1

# The question class that holds the question objects
class Question:
        def __init__(self):
            pass # Each question is by default empty

        # Creates the right answer by selecting a random city and corresponding state
        def create_question(self):
            # Creating the right answer
            self.index = 2
            self.string = str(questions_list[self.index-1])
            self.picked_index = r.randint(0,len(city))
            self.random_city = city[self.picked_index]
            self.state = state[self.picked_index]
            self.create_wrong_answers(self.state)

        # Generates the wrong answers necessary to create the challenge
        def create_wrong_answers(self,correct_answer):
            self.list_of_wrong_answers = []
            for i in range(3):
                # Picks random states that are not the correct ones
                j = r.randint(0,len(state))

                # Check for duplicate elements
                if state[j] in self.list_of_wrong_answers:
                    continue
                else:
                    # Add wrong answers
                    wrong_answer = state[j]
                    self.list_of_wrong_answers.append(wrong_answer)

# Improvised button specifically for this project.
# This button class is inherited from the tkinter
# Button class.
class Button2(Button):
    def __init__(self,*args,**kwargs):
        Button.__init__(self,*args,**kwargs)
    def addCorrect(self,correct): # The added functionality required for this project
        self.correct = correct
