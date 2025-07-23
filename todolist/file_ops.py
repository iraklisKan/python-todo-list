import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, 'todoText', 'todos.txt')
def read_todos(filename=filepath):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    if not os.path.exists(filename):
        # Create the file if it doesn't exist
        with open(filename, 'w') as file:
            pass
    with open(filename, 'r') as file:
        return file.readlines()

def write_todos(todos, filename=filepath):
    with open(filename, 'w') as file:
        file.writelines(todos)