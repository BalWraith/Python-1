import os; os.system('cls')
date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: \n")

## makes a file in the journal folder with the name set to the date the users enters 
with open(f"Ardit_Sulce_python/journal/{date}.txt", "w") as file:

    ## wites the input variable mood and thoughts to the file 
    file.write(mood + '\n' * 2 )
    file.write(thoughts)

 























print('\n'*8)