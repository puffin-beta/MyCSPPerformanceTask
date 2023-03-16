import tkinter as tk
from tkinter import *
import csv

def group_elements(raw_text,desired_character,final_list):
    temp = ""
    for c in raw_text:
        if c == desired_character:
            final_list.append(temp)
            temp = ""
        else:
            temp += c
            continue
    del temp
    return final_list

def create_ui():
    main_file = "uscities.csv"

    

    subroot = tk.Tk()
    root_file = open(main_file,'r')
    Data = list(root_file)
    del(Data[0])
    del Data, root_file

    main_file = open("uscities.csv",'r')

    subroot.title("MAJOR ZONES!")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=4,rowspan=4)

    text = open("question-starters.txt",'r')
    string = text.read()
    list_of_question_starters = []
    list_of_question_starters = group_elements(string,"\n",list_of_question_starters)

    reader = csv.reader(main_file, delimiter=",")
    modded_data = open("city_and_state.txt","w+")
    for row in reader:
        modded_data.write(str(row[0])+" "+str(row[3])+"\n")

    subroot.mainloop()