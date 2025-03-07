import os;os.system('cls')
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) # turns age into a Integer(number)
# print(age)

# if age >= 18:
    # print("You are old enough to vote!")
    # print("Please put an X in the box")
# else:
    # print("Please come back in {0} years".format(18 - age))

if age < 18 & age > 90:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote!")
    print("Please put an X in the box")



























print('\n'*8)