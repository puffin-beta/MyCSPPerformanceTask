import tkinter as tk
from tkinter import *
import csv

def group_elements(raw_text,desired_character,final_list):
    temp = ""
    for c in raw_text:
        if c == desired_character:
            final_list.append(temp)
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

    subroot.title("MAJOR ZONES!")
    canvas = tk.Canvas(subroot,width=800,height=600,bg="White")
    canvas.grid(columnspan=4,rowspan=4)

    text = open("question-starters.txt",'r')
    string = text.read()
    list_of_question_starters = []
    list_of_question_starters = group_elements(string,"\n",list_of_question_starters)

    city_with_state = {}
    with open(main_file,'r') as file_obj:  
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            try:
                city_with_state[str(row[0])] = str(row[3])
            except:
                continue
    
    print(list_of_question_starters)
    subroot.mainloop()