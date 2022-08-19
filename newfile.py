first_name = input("Jak masz na imię?"+" "+"(L)")

if first_name=="Kuba":
    print("Czesc", first_name,"!")
else:
    print("To nie ty!")
    
print("Ile masz lat?")
age = input("")

if int(age) >= 18 and int(age) < 65:
    print("Jesteś dorosłą osobą!")
elif int(age)<18:
    print("Jesteś niepełnoletni!")
else:
    print("Jesteś seniorem!")