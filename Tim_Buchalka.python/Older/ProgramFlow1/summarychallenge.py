import os
os.system("cls")
# print("Please choose your options from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5:\tGo to bed")
# print("0:\tExit")


# choice = "-"
# while True:
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your options from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")

#     choice = input()
choice = "-"
while choice != "0":  
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your options from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()



print("\n"*3)