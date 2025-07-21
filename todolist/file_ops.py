import os
filepath = 'todoText/todos.txt'
def read_todos(filename=filepath):
    if not os.path.exists(filename):
        # Create the file if it doesn't exist
        with open(filename, 'w') as file:
            pass
    with open(filename, 'r') as file:
        return file.readlines()

def write_todos(todos, filename=filepath):
    with open(filename, 'w') as file:
        file.writelines(todos)