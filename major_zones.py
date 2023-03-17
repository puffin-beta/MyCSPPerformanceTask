import tkinter as tk
from tkinter import *
import init_lists as init
import random as r

def create_ui():
    main_file = "uscities.csv"

    subroot = tk.Tk()
    
    init.get_lists()

    subroot.title("MAJOR ZONES!")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=10,rowspan=10)

    class Question:
        def __init__(self):
            pass
        def create_question(self):
            self.index = 2
            self.string = str(init.questions_list[self.index-1])
            if self.index == 2:
                self.picked_index = r.randint(0,len(init.city))
                self.random_city = init.city[self.picked_index]
                self.state = init.state[self.picked_index]
                self.create_wrong_answers(self.state)
        def create_wrong_answers(self,correct_answer):
            self.list_of_wrong_answers = []
            if self.index == 2:
                for i in range(3):
                    j = r.randint(0,len(init.state))
                    if j == self.picked_index:
                        continue
                    k = init.state[j]
                    self.list_of_wrong_answers.append(k)


    class Button:
        def __init__(self,width=200,height=100,color=None,correct=False):
            self.color = color
            self.correct = correct
            pass
        def draw(self,t,c=0,r=0):
            button = tk.Button(subroot,text=t,font="Verdana",color=self.color,command=lambda:self.highlight())
            button.grid(column=c,row=r)
            return button
        def highlight(self):
            if self.correct == False:
                self.color = (255,0,0)
            if self.correct == True:
                self.color = (0,255,0)
            return self.color


    q1 = Question()
    q1.create_question()
    final_str = q1.string[:13] + ' ' + q1.random_city + q1.string[13:]
    label = tk.Label(subroot,text=final_str,font=("Verdana",20),bg="White")
    label.grid(column=0,row=0)
    answer_btn = Button(True)
    answer_btn.draw(q1.state,0,1)
    for j in range(3):
        btn = Button(False)
        btn.draw(q1.list_of_wrong_answers[j],0,j+2)
    subroot.mainloop()