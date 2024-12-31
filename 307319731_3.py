from operator import truediv

valid_chars = "0123456789ABCDEF"

#the basic input and basic reference for validation
#cleaning input with .strip
number = input("Enter the number: ").strip()

#quick fix for lower letters reduce bugs
upper_number = number.upper()

# validation proccess
valid = list(upper_number)
for value in valid:
    if value not in valid_chars:
        print("Invalid character")
        exit()

# same for second number
number_2 = input("Enter the second number: ").strip()
upper_number2 = number_2.upper()

# second validation proccess. in future i should use function
valid_2 = list(upper_number2)
for value in valid_2:
    if value not in valid_chars:
        print("Invalid character")
        exit()

# Input the base as an integer
base = int(input("Enter the base (2-16): ").strip())

# Validate the base
if not (2 <= base <= 16):
    print("Error: Base must be between 2 and 16.")
    exit()

#print(upper_number)
#print(type(upper_number))
#print(upper_number2)
#print(type(upper_number2))

# making a copy out of the first string
reverse = valid.copy()

# the action of inverting the list
reverse.reverse()

# making a copy out of the second string
reverse2 = valid_2.copy()


# the action of inverting the second list
reverse2.reverse()

# converter
base_convertor = base_converter = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}

# initiating new list of temporal result
converted_values1 = []

#starting the loop of convertion
for value in reverse:
    converted_values1.append(base_convertor[value])

# initiating new list of temporal result for second string in question
converted_values2 = []


#starting the second loop of convertion
for value in reverse2:
    converted_values2.append(base_convertor[value])

# after setting up the convertor, it is time to combine values
temp_result = [a + b for a, b in zip(converted_values1, converted_values2)]
if len(converted_values1) > len(converted_values2):
    temp_result += converted_values1[len(converted_values2):]
else:
    temp_result += converted_values2[len(converted_values1):]


# temp_ is a list with all converted numbers, now we need to design the carrier
not_final_result = []

# initiate carrier
carrier = 0

# if value which is combined, is bigger than the base: make mod, and change carrier
for value in temp_result:
    value += carrier
    if value >= base:
        digi = value % base
        carrier = 1

        # else the temp result is not > base, then no need of carrier, the digi == the value in qustion
    else:
      digi = value
      carrier = 0

    not_final_result.append(digi)

# for loop ends here


# at the end of loop, carrier is = 1 or 0
if carrier == 1:
  not_final_result.append(1)

# we need to convert back, converting integers back to keys = strings
inverse_dict = {value : key for key, value in base_convertor.items()}

#initialize list of strings
converted_back = []
for i in not_final_result:
        converted_item =  inverse_dict.get(i)
        converted_back.append(converted_item)

# var_type = type(converted_back)
# print(var_type)
#         # converted_back.append(i)


almost_final_result = ''.join(str(num) for num in converted_back)
final_result= almost_final_result[::-1]
# rev = list(almost_final_result)
# rev.reverse()
# print(not_final_result)
print(final_result)
# almost_final_result.reverse()





print()
#print(converted_values1)
#print(converted_values2)
print(f"temp: {temp_result}")
print()

#
# final_result = []
# for value in temp_result:
#     new = value % base
#     final_result.append(new)


print(f"result is: {final_result}")
# print("now i need to figure out how to carry +1 to the next step of digit sum")
# print("from there - to reverse and filter out the result, i did in the previous targil")

