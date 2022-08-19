import math
import random

times_len = 0
password = ""

print("PASSWAORD GENERATOR")
print("")
print("How many characters would you like in your password?")
print("")
pass_len = int(input(""))

#Global Variables:

characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

numbers="1234567890"

specials="@#$&/*!?"

#MAIN CODE:

while times_len<pass_len:
 char_pos = random.randint(0,len(characters) - 1)
 num_pos = random.randint(0,  len(numbers) - 1)
 spec_pos = random.randint(0, len(specials) - 1)
 
 rand_char = characters[char_pos]
 rand_num = numbers[num_pos]
 rand_spec = specials[spec_pos]
 comp_choice = [rand_char,    rand_num, rand_spec]
  
 ran = random.choice(comp_choice)
 password = str(password)+ran
 times_len = times_len + 1


print(password)
  
  
  


 

 
 






