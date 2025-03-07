import os 
os.system("cls")
computer_parts = ["computer",
                   "monitor",
                    "keyboard",
                    "mouse",
                    "mouse mat"
                    ]
print(computer_parts)

#item in place 3 in the list computer_parts is replaced with trackball
# computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["tackball"]#this get rid of item 3 on and replaces it with trackball
print(computer_parts)










print("\n"*3)