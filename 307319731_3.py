# input any number_1
# input any number_2
# input any  1 < base < 17  (exapmle base 12)
#from ftplib import print_line

# make the "addition"
# addition:
# editing the numbers before combination:
# first number-> list 1 of integers-> reverse list example: A89 becomes 98A
# second number-> list 2 of integers-> reverse list example: 78B123 becomes 321B87

# for value in reverse (list 1) -> dictionary key:A return value:10 - temp_value_1
# for value in reverse (list 2) -> dictionary key:7 return value: 7 - temp_value_2
# temp_add = (temp_value_1) + (temp_value_2) : return: 17
# base example(12) : char_result = temp_add - base (example=5)
# if temp_add > base : true

valid_chars = "0123456789ABCDEF"
number = input("Enter the number: ").strip()  # Input the number as a string
upper_number = number.upper()


valid = list(upper_number)
#print(valid)
for value in valid:
    if value not in valid_chars:
        print("Invalid character")
        exit()

number_2 = input("Enter the second number: ").strip()
upper_number2 = number_2.upper()


valid_2 = list(upper_number2)
#print(valid_2)
for value in valid_2:
    if value not in valid_chars:
        print("Invalid character")
        exit()

base = int(input("Enter the base (2-16): ").strip())  # Input the base as an integer

# Validate the base
if not (2 <= base <= 16):
    print("Error: Base must be between 2 and 16.")
    exit()

#print(upper_number)
#print(type(upper_number))
#print(upper_number2)
#print(type(upper_number2))

# now the addition:
reverse = valid.copy()
reverse.reverse()
#print(reverse)

reverse2 = valid_2.copy()
reverse2.reverse()
#print(reverse2)

# converter
base_convertor = base_converter = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}
converted_values1 = []
for value in reverse:
    converted_values1.append(base_convertor[value])

converted_values2 = []
for value in reverse2:
    converted_values2.append(base_convertor[value])

temp_result = [a + b for a, b in zip(converted_values1, converted_values2)]
if len(converted_values1) > len(converted_values2):
    temp_result += converted_values1[len(converted_values2):]
else:
    temp_result += converted_values2[len(converted_values1):]

print()
#print(converted_values1)
#print(converted_values2)
#print(f"temp: {temp_result}")
print()


final_result = []
for value in temp_result:
    new = value % base
    final_result.append(new)

#for i in temp_result:
#if value in temp_result > base:
#add +1 to the next item in final_result



print(f"result is: {final_result}")
print("now i need to figure out how to carry +1 to the next step of digit sum")
print("from there - to reverse and filter out the result, i did in the previous targil")
#print(type(final_result))
# now i need to






# for value in reverse (list 1) -> dictionary key:A return value:10 - temp_value_1
# for value in reverse (list 2) -> dictionary key:7 return value: 7 - temp_value_2
# temp_add = (temp_value_1) + (temp_value_2) : return: 17
# base example(12) : char_result = temp_add - base (example=5)
# if temp_add > base : true