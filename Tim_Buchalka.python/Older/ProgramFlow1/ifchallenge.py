import os
os.system("cls")

name = input("What is your name? ")
age = int(input("Hello {0}, how old are you? ".format(name)))

if age >= 18 and age <= 30:
    print("Welcome to the holiday")
else:
    print("I'm sorry {}, you can't come".format(name))