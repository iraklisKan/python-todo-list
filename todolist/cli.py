from file_ops import read_todos, write_todos
from my_time import print_current_time

print(f"the current date and is {print_current_time().strftime('%d-%m-%Y %H:%M')}")
while True:

    user_action = input("Type Add,show,complete, or exit : ")
    user_action = user_action.strip().lower()


    if user_action.startswith('add'):
        todos = read_todos()
        todo = input("Enter a todo item: ")
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = read_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(input("Enter the number of the todo item to edit: "))
            number = number - 1
            todos = read_todos()
            new_todo = input("Enter the new todo item: ") 
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue       

    elif user_action.startswith('complete'):
        try:    
            number = int(input("Enter the number of the todo item to complete: "))
            todos = read_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue    
        
    elif user_action.startswith("exit"):
        break
print("Bye!")