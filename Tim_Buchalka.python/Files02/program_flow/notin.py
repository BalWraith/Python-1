import os;os.system('cls')
# activity = input("What would you like todo today? ")

# if "cinema" not in activity.casefold():
#     print("But I want to go to the cinema")


## Challenge
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person is the right age to go on an 18-30 holiday (they must be over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print a (polite message refusing them entry.)

name = input("What is your name: ")
age = int(input("How old are you? "))

if age >= 18 and age <= 30:
    print("Hey {0}, welcome to the holiday".format(name))
else:
    print("Sorry {0}, you can't come on this holiday ".format(name))












print('\n'*8)