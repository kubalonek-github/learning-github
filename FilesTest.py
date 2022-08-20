file = open("countries_and_capitals.txt", "w+")

countries_and_captials = {"Poland": "Warsaw","Germany": "Berlin","US": "London"}

for country, capital in countries_and_captials.items():
    file.write(country + "-" + capital + "\n")
file.close()

###

file = open("countries_and_capitals.txt")
for line in file.readlines(): #line = lineNumber
    print(line.strip())
file.close()