# Simple Todo List Application

A command-line todo list application built with Python that allows you to manage your daily tasks.

## Features

- **Add** new todo items
- **Show** all current todos with numbering
- **Edit** existing todo items
- **Complete** (delete) finished tasks
- **Date/Time display** when starting the application
- **Persistent storage** in text file

## Files Structure

```
todolist/
├── main.py           # Main application with user interface
├── file_ops.py       # File operations (read/write todos)
├── my_time.py        # Date/time utilities
├── todoText/         # Data storage directory
│   └── todos.txt     # Todo items storage file
└── simioseis/        # Learning notes directory
    └── simioseis.txt # Python learning reference
```

## How to Run

1. Make sure you have Python 3.6+ installed
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

When you run the application, you'll see the current date and time, then a prompt:

```
Type Add,show,complete, or exit :
```

### Commands

- **add**: Add a new todo item
- **show**: Display all current todos
- **edit**: Modify an existing todo item (by number)
- **complete**: Remove a completed todo item (by number)
- **exit**: Close the application

### Example Session

```
the current date and is 21-07-2025 14:30
Type Add,show,complete, or exit : add
Enter a todo item: Buy groceries

Type Add,show,complete, or exit : show
1-Buy groceries

Type Add,show,complete, or exit : complete
Enter the number of the todo item to complete: 1

Type Add,show,complete, or exit : exit
Bye!
```

## Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only built-in modules)
- **Storage**: Plain text file (`todoText/todos.txt`)
- **Architecture**: Modular design with separated concerns

## Error Handling

- Invalid input validation for edit/complete commands
- Automatic file creation if todos.txt doesn't exist
- Index error handling for out-of-range todo numbers

## Contributing

Feel free to fork this project and submit pull requests for improvements!
