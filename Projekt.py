import math
import random

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

while user_choice!=7:
    print("")
    print("1. Zobacz tablice zadan")
    print("2. Dodaj zadanie do tablicy")
    print("3. Usun zadanie z tablicy")
    print("4. Dodaj zadanie do pliku")
    print("5. Synchronizuj")
    print("6. Losowe zadanie z listy")
    print("7. Zakończ program")
    user_choice = int(input(""))
    if user_choice == 1:
        watch_tab()

    elif user_choice == 2:
        add_to_tab()

    elif user_choice == 3:
        del_from_tab()

    elif user_choice == 4:
        save_tab_to_file()

    elif user_choice == 5:
        sync_data()

    elif user_choice == 6:
        random_work()

