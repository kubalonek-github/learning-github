text = str(input("Wpisz: "))
number = int(input("Ilość"))
counted = 0
n_word_pass = str(input("n-word [Y/N]: "))  

perm = True

if n_word_pass=="Y":
     y = text[0:(len(text)) - 2]
     x = y.lower()
     while (perm==True or counted<number):
         print(x)
         counted = counted + 1
         perm = False
else:
    while (perm==True or counted<number):
          x = text
          print(x)
          counted = counted + 1
          perm = False
     
        


