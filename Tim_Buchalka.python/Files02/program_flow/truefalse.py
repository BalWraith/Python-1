import os; os.system('cls')
day = "Saturday"
temperature = 30
raining = False

## if the day is "Saturday" and the temperature is above 27 and it is not raining
## if one is False than the else block will execute 
if (day == "Saturday" and temperature > 27) and not raining:
    print("Go swimming")
else:
    print("Learn Python")

## if the day is "Saturday" and the temperature is above 27 or it is not raining
## if temperature OR it is not raining is true than the if block will execute
if day == "Saturday" and (temperature > 27 or not raining):
    print("Go swimming")
else:
    print("Learn Python")


if 0:
    print("True")
else:
    print("False")



name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {0}".format(name))
else:
    print("Are you the man with no name?")














print('\n'*8)