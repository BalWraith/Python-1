import os;os.system('cls')
# number = "9,223;372:036 854,775;807"

## slices the variable number starting at 1 and slices every 4th character 
## separators = , ; : space , ;
# separators = number[1::4]
# print(separators)

## string.join(character if the character is not in the separators variable)
## if the variable is in the separators the else block will execute 
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])




# number = input("Please enter a series of numbers, using any separators you like: ")

# Empty string
# separators = "" 

## this for loop will check every character in the number string
# for char in number:
    ## if the character is not a number then it will be added to the separators variable
    # if not char.isnumeric():
        # adds all none number characters to the separators variable
        # separators = separators + char

# print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])







number = input("Please enter a series of numbers, using any separators you like: ")
separators = "" 

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))





















print('\n'*8)


