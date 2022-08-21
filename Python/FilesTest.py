#BELONG TO config.txt

with open("config.txt") as file:
    argument1 = file.readline().strip()
    argument2 = file.readline().strip()
    arg1 = argument1[-5:22].strip()
    arg2 = argument2[-5:19].strip()
if arg1=="True":
    print("Ptak lata!")
else:
    print("Ptak nie lata")

if arg2=="True":
    print("Pies chodzi")
else:
    print("Pies nie chodzi")
