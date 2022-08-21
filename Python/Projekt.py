from KlasyProjektu import Main
from KlasyProjektu import Words
import math
import random

word = Words()

key1,key2,key3,key4,key5,key6,key7 = word.smain1,word.smain2,word.smain3,word.smain4,word.smain5,word.smain6,word.smain7

menu_number1 = int(word.smain1[0])
menu_number2 = int(word.smain2[0])
menu_number3 = int(word.smain3[0])
menu_number4 = int(word.smain4[0])
menu_number5 = int(word.smain5[0])
menu_number6 = int(word.smain6[0])
menu_number7 = int(word.smain7[0])

user_menu_choices = Main(key1,key2,key3,key4,key5,key6,key7)

work_tab = []
user_choice = -1

def watch_tab():
    print("Elementy na liscie: ")
    print("*"*30)
    index = 0
    elem_num=1
    for tab in work_tab:
        print(str(elem_num)+". " + work_tab[index])
        print("*"*30)
        index = index + 1
        elem_num = elem_num + 1

def add_to_tab():
    print("Wpisz zadanie ktore ma sie pojawic w tablicy: ")
    work_input = str(input(""))
    work_tab.append(work_input)
    file = open("work_notes.txt", "a+")
    file.write(work_input + "\n")

def del_from_tab():
    print("Wybierz index zadania do usuniecia: ")
    print("")
    print(work_tab, "[", "1 -", str(len(work_tab)).strip(), "]")
    del_index = int(input(""))
    if del_index<0 or del_index>len(work_tab):
        print("Niepoprawny Index!")
    else:
        work_tab.pop(del_index - 1)
def save_tab_to_file():
    try:
        file = open("work_notes.txt", "w")
        ind = 0
        for work in work_tab:
            file.write(work+"\n")
    except:
        print("Coś poszło nie tak")
def sync_data():
    print("Dodano: ")
    print("*"*30)
    index = 0
    elem_num = 1
    file = open("work_notes.txt")
    for line in file.readlines():
        work_tab.append(line.strip())
        print(str(elem_num) + ". " + line.strip())
        elem_num = elem_num + 1
        print("*"*30)
def random_work():
    rand = str(random.choice(work_tab))
    print("")
    print("*"*30)
    print("Losowa rzecz z listy: "+rand)
    print("*"*30)

while user_choice!=menu_number7:
    print("")
    print(user_menu_choices.key1)
    print(user_menu_choices.key2)
    print(user_menu_choices.key3)
    print(user_menu_choices.key4)
    print(user_menu_choices.key5)
    print(user_menu_choices.key6)
    print(user_menu_choices.key7)
    user_choice = int(input(""))

    if user_choice == menu_number1:
        watch_tab()

    elif user_choice == menu_number2:
        add_to_tab()

    elif user_choice == menu_number3:
        del_from_tab()

    elif user_choice == menu_number4:
        save_tab_to_file()

    elif user_choice == menu_number5:
        sync_data()

    elif user_choice == menu_number6:
        random_work()

