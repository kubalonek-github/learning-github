# CALCULATOR APP
# ONLY THE SAME LENGTH NUMBERS OPERATIONS!!
print("KALKULATOR: ")
print("*" * 30)
print("")
string_number = input("Wykonaj działanie: ")

if len(string_number) == 3:
    number1 = int(string_number[0])
    math_char = string_number[1]
    number2 = int(string_number[-1])
elif len(string_number) == 5:
    number1 = int(string_number[0:2])
    math_char = string_number[2]
    number2 = int(string_number[3:5])
elif len(string_number) == 7:
    number1 = int(string_number[0:3])
    math_char = string_number[3]
    number2 = int(string_number[4:7])
elif len(string_number) == 9:
    number1 = int(string_number[0:4])
    math_char = string_number[4]
    number2 = int(string_number[5:9])


def add_numbers(add1, add2):
    add_result = add1 + add2
    print(("***** " + str(add1) + " + " + str(add2) + " = " + str(add_result) + " *****"))


def subtract_numbers(sub1, sub2):
    sub_result = sub1 - sub2
    print(("***** " + str(sub1) + " - " + str(sub2) + " = " + str(sub_result) + " *****"))


def multiply_numbers(multi1, multi2):
    multi_result = multi1 * multi2
    print(("***** " + str(multi1) + " × " + str(multi2) + " = " + str(multi_result) + " *****"))


def dividing_numbers(div1, div2):
    div_result = div1 / div2
    print(("***** " + str(div1) + " : " + str(div2) + " = " + str(div_result) + " *****"))


def moduling_numbers(mod1, mod2):
    mod_result = mod1 % mod2
    print(("***** " + str(mod1) + " % " + str(mod2) + " = " + str(mod_result) + " *****"))


def power_numbers(pow1, pow2):
    pow_result = pow1 ** pow2
    print(("***** " + str(pow1) + " ^ " + str(pow2) + " = " + str(pow_result) + " *****"))


if math_char == "+":
    add_numbers(number1, number2)
elif math_char == "-":
    subtract_numbers(number1, number2)
elif math_char == "*":
    multiply_numbers(number1, number2)
elif math_char == ":":
    dividing_numbers(number1, number2)
elif math_char == "%":
    moduling_numbers(number1, number2)
elif math_char == "^":
    power_numbers(number1, number2)
