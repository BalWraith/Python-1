todos = [];import os; os.system('cls')
txt = "Ardit_Sulce_python/todos.txt"
while True:
    ## Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete: ")
    user_action = user_action.strip()

    match user_action:
        ## Add to the todos list 
        case 'add':
           #Runs until you enter exit
           while "exit" != True:
            todo = input("Enter a todo or exit: ").casefold()
            if todo != "exit":
                with open(txt,'r') as file:
                    todos = file.readlines()

                
                todos.append(f"{todo} \n")
                with open(txt,'w') as file:
                    file.writelines(todos)
            else:
                break

        # Shows the list without being able to edit or add to it
        case 'show':
            with open(txt, "r") as file:
                 todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')          
                row = f"{index + 1}-{item}"
                print(row)

        # Edit the todos list and shows the list
        case 'edit':
            while "exit" != True:
                with open(txt, "r") as file:
                    todos = file.readlines()
                    number = int(input("Number of the todo to edit or exit: ")) -1 
                if number != "exit":
                    os.system('cls')   
                    for index, item in enumerate(todos):
                        item = item.strip('\n')          
                        row = f"{index + 1}-{item}"
                        print(row)                  

                    new_todo = input("Enter new todo: ")
                    todos[number] = new_todo + '\n'
                    
                    with open(txt, 'w') as file:
                        file.writelines(todos)
                else:
                    break

            # Removes a todo from the list
        case 'complete':
            while "exit" != True:
                file = open(txt, "r")
                file.readlines()
                file.close()
                number = input("Enter the number of the todo to complete: ")

                if number == "exit":
                    break
                else:
                    todos.pop(int(number) -1)
            
        case 'exit':
            file.close()
            break


print("Bye!")

print("\n"*5)




