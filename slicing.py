#slicing - tworzenie innego sub-tekstu z tekstu za pomocą indexing[] albo slice()
#[start, stop, step]

name = "Jakub Klimkiewicz"
http = "http://"
com = ".com"
#moje imię :)

perm=True

while perm==True:
 print("Podaj klucz")
 print("")
 print("1. Index Key")
 print("2. App name from http")
 print("3. Web http from app name")
 print("4. End interaction")
 print("")
 key = int(input(""))
 print("")


#1 INDEX METHOD
#[start, stop, step]
#start - zawsze pierwszą liczbą jest 0
#stop - zatrzymuje sie w danym momencie i zaczyna sie od liczby 1
#step - o ile (min:2)
#tip - ":" jest rowny 0 bez podanej wartości
 if key==1:
  first_name = name[:5]
  last_name = name[::-1]
  print("INDEX_METOD")
  print(last_name)
 elif key==2:
  print("Podaj url strony: ")
  url = str(input(""))
  slice = slice(6,-3)
  sliced = url[slice] #google
  web_name= sliced
  web_in_console = web_name.  capitalize()
  print("")
  print("To jest",web_in_console+"!")
  print("")
 elif key==3:
  print("Podaj nazwe aplikacji")
  app_name = str(input("")) 
  final_app_name = app_name. lower()
  print("")
  print(http+final_app_name+com)
  print("")
 elif key==4:
     perm=False
     print("Thanks for using bot!")
 else:
  print("Wrong Key!")
#2 
