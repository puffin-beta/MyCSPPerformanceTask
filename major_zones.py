
# Import modules
import tkinter as tk
from tkinter import *
import useful_functions as lib
from useful_functions import *
import random as r
import time
from threading import Thread, Event
from multiprocessing import *
import sys

txt = ""

# Main loop for the game window
def create_ui(timer):

    # Game window object. It's global for deleting
    # objects within the root from
    # nested functions
    global subroot
    subroot = tk.Tk()
    
    # Gets all the necessary cities, states, and questions
    # in the form of lists.
    lib.get_lists()

    # Canvas for game window
    subroot.title("GAME WINDOW")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=10,rowspan=10)

    # This function creates questions, handles timers, and evaluates
    # answers.
    def make_question():

        global evaluation
        evaluation = ""

        # Question object
        q1 = Question()

        # Creates a right answers and a list of three wrong 
        # answers
        q1.create_question()

        # Takes question string from the "create_question" function
        # and inserts the state name in it.
        global final_str
        final_str = q1.string[:13] + ' ' + q1.random_city + q1.string[13:]
        label = tk.Label(subroot,text=final_str,font=("Verdana",20),bg="White")
        label.grid(column=0,row=0)

        # Creates the list of answers by creating a static, 4
        # element list as there are always 4 answers to each
        # question
        answers = list(range(4))

        # Picks one of the four to be correct
        right_answer_index = r.randint(0,3)

        # The rest of the answers will be wrong
        temp_count = 0
        for i in range(len(answers)):
            if i != right_answer_index:
                answers[i] = q1.list_of_wrong_answers[temp_count]
                temp_count += 1
            else:
                continue

        # Add the right answer
        answers[right_answer_index] = q1.state

        # Checks if each answer is right or wrong and then
        # gives a new question
        def evaluate_answer(IsCorrect,correct_option):
            # Checks the answer based on the button object's
            # "correct" attribute
            global txt
            if IsCorrect == "True":
                txt = "Correct"
            elif IsCorrect == "False":
                txt = "Wrong. the correct answer is {correct}".format(correct=correct_option)
            
            # Sets event handler for timer to reset
            answered.set()

            # Puts the evaluation in the form of a label
            evaluation = tk.Label(subroot,text=txt,font=("Verdana",20),bg="White")
            evaluation.grid(column=0,row=9)

            # Clears the screen
            my_button.destroy()
            my_button2.destroy()
            my_button3.destroy()
            my_button4.destroy()
            label.destroy()
            lib.time_label.destroy()

            # Call to create a new question
            make_question()
            
        # Creates the four answers buttons based on their position on the answers list.
        # For example, my_button will get the attributes
        # of answers[0], my_button2 will get the attributes of answers[2], and
        # so on.
        my_button_correct = ("True" if answers[0] == q1.state else "False") # Boolean value of if value at answers[0] is the right answer
        my_button = Button2(subroot,text=(answers[0]),font=("Verdana",15))
        my_button.addCorrect(my_button_correct) # Add this boolean value to the button object
        my_button['command'] = lambda:evaluate_answer(my_button_correct,q1.state) # Evaluate the answer when button clicked
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

        # Event handler for button clicks
        global answered
        answered = Event()

        global tick_time
    
        # Selects the maximum time limit for each question
        # according to the difficulty
        time_left = 0
        if timer == "easy":
            time_left = 45
        elif timer == "medium":
            time_left = 30
        elif timer == "hard":
            time_left = 20
        
        # Creates the timer thread that resets each time an answer is cliked
        global time_thread
        time_thread = Thread(target=lib.tick_time,args=(1,time_left,subroot,answered,))
        time_thread.start()

        # Game will end if "X" button is pressed or
        # if the time runs out
        def end_game():
            subroot.destroy()
        subroot.protocol("WM_DELETE_WINDOW",end_game)
        if lib.thread_ended:
            end_game()
        
    # Call to create first question
    make_question()

    # Runs the game
    subroot.mainloop()