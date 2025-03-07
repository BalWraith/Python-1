import os ; os.system('cls')
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")













## casefold() -Return a version of the string suitable for caseless comparisons.



## EXERCISE 
## Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11 
# for i in range(0,100,7):
#     if i % 11 == 0:
#         print(i)

























print('\n'*8)