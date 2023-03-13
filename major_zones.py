import tkinter as tk
from tkinter import *
import csv

def create_ui():
    subroot = tk.Tk()

    subroot.title("MAJOR ZONES!")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=4,rowspan=4)

    filepath = "us_cities_states_counties.csv"
    text = open("question-starters.txt",'r')
    list_of_questions = text.read()
    Answers = open(filepath)
    Reader = csv.reader(Answers)
    Data = list(Reader)

    print(list_of_questions)

    subroot.mainloop()