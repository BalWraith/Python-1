waiting_list = ["sen", "ben", "john"];import os;os.system('cls')
waiting_list.sort() 

for index,list in enumerate(waiting_list):
    print(f"{index + 1}. {list.title()}")
