import os; os.system('cls')
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            ## with is used for resource management and exception handling this will open and clsoe the file
            with open("Ardit_Sulce_python/todos.txt" , 'r') as file:
                 todos = file.readlines()

            todos.append(todo)

            with open("Ardit_Sulce_python/todos.txt", 'w') as file:
                 file.writelines(todos)
        case 'show':
            with open("Ardit_Sulce_python/todos.txt", "r") as file:
                 todos = file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')          
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            
            with open("Ardit_Sulce_python/todos.txt", "r") as file:
                 todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            with open("Ardit_Sulce_python/todos.txt", 'w') as file:
                 file.writelines(todos)

        case 'complete':
                number = int(input("Enter the number of the todo to complete: "))
                
                with open("Ardit_Sulce_python/todos.txt", "r") as file:
                     todos = file.readlines()
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open("Ardit_Sulce_python/todos.txt", 'w') as file:
                    file.writelines(todos)

                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)

        case 'exit':
            
            break


print("Bye!")

print("\n"*5)




