import os
os.system("cls")
lst = ["books", "pencils", "cyrons", "pens", "erasers"]

for i in lst:
    # print(i)
    if i == "pens":
        print(True)
        break # to exit out of loop


string = ""
while True:
    user_input = input("Enter characters: ")

    if user_input == "quit":
        print(string)
        break

    string = string + user_input





print("\n"*8)