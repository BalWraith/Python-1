import os
os.system("cls")

parrot = "Norwegian Blue"

letter = input("Enter a character: ")
# letter = letter.title()

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")






print("\n"*2)