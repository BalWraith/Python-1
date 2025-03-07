while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            

            todos.append(todo)

            file = open('todos.txt', 'w')#file object
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", 'r')#r turns the string into a row string disregarding any special characters like(\)
            todos = file.readlines()
            file.close()

            

            for index, item in enumerate(todos):

                # new_todos = [item.strip('\n') for item in todos]
                
                item = item.strip('\n')#this is to take away the extra space when printed
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
          number = int(input("Number of the todo to complete: "))
          todos.pop(number - 1)
        case 'exit':
            break
print()
print("Bye!")

