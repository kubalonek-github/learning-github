from KlasyProjektu import Main
from KlasyProjektu import Words
import sqlite3
import math
import random

word = Words()

key1,key2,key3,key4,key5,key6,key7 = word.smain1,word.smain2,word.smain3,word.smain4,word.smain5,word.smain6,word.smain7

user_menu_choices = Main(key1,key2,key3,key4,key5,key6,key7)

# -----------Database------------

connection = sqlite3.connect("todo.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def watch_database(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()
    print("")
    for i in result:
        print(str(i[0]) + ". " + i[1])


def add_to_database(connection):
    print("dodajemy zadanie")
    task = str(input("Dodaj zadanie: "))
    if input==0:
        print("Powrót do menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
        print("dodano zadanie!")

def del_from_database(connection):
    index = int(input("Podaj index zadania do usuniecia: "))
    cur = connection.cursor()
    rows_deleted = cur.execute(""" DELETE FROM task WHERE rowid=?""", (index,)).rowcount
    connection.commit()
    if rows_deleted==0:
        print("")
        print("Takie zadanie nie istnieje")
    else:
        print("")
        print("Usunieto zadanie")

def random_from_database(connection):
    try:
        things_in_db = []
        cur = connection.cursor()
        cur.execute(""" SELECT task FROM task """)
        rand = cur.fetchall()
        for i in rand:
            things_in_db.append(i)
        print(str(random.choice(things_in_db))[2:-3])
    except:
        pass

def add_db_to_file(connection):
    try:
        cur = connection.cursor()
        cur.execute("""SELECT task FROM task""")
        text = cur.fetchall()
        row_num = 0
        for i in text:
            with open("work_notes.txt", "w+") as file:
                file.writelines(str(row_num) + ". " + str(i)[2:-3] + "\n")
                row_num += 1
        print("")
        print("Dodano zadanie z bazy danych do pliku tekstowego")
    except:
        print("ERR101: Brak treści w bazie danych")
        pass

create_table(connection)

while True:
    print("")
    print(user_menu_choices.key1)
    print(user_menu_choices.key2)
    print(user_menu_choices.key3)
    print(user_menu_choices.key4)
    print(user_menu_choices.key5)
    print(user_menu_choices.key6)
    user_choice = int(input(""))

    if user_choice == 1:
        watch_database(connection)

    elif user_choice == 2:
        add_to_database(connection)

    elif user_choice == 3:
        del_from_database(connection)

    elif user_choice == 4:
        random_from_database(connection)

    elif user_choice == 5:
        add_db_to_file(connection)

    elif user_choice == 6:
        break

