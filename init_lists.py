import csv
questions_list = []
city = []
state = []
def get_lists():
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

