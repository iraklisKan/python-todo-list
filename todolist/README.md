# Simple Todo List Application

A todo list application built with Python that comes in two versions:
- **Command-line interface (CLI)** for terminal use
- **Web interface** using Streamlit for browser use

## 🌐 Live Demo

**Try the web app here:**  
If the deployment URL changes, check the repository description or the Streamlit Cloud dashboard for the latest link.  
Consider setting up a custom domain for easier access.

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
├── cli.py            # Command-line version (formerly main.py)
├── web.py            # Streamlit web application
├── file_ops.py       # File operations (read/write todos)
├── my_time.py        # Date/time utilities
├── requirements.txt  # Python dependencies for web app
├── todoText/         # Data storage directory
│   └── todos.txt     # Todo items storage file
└── simioseis/        # Learning notes directory
    └── simioseis.txt # Python learning reference
```

## How to Run

### Web Version (Recommended)
Visit the live demo: [https://irakliskan-python-todo-list-todolistweb-7mqa2v.streamlit.app/](https://irakliskan-python-todo-list-todolistweb-7mqa2v.streamlit.app/)

### Local Web Version
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run web.py`

### Command-Line Version

1. Make sure you have Python 3.6+ installed
2. Clone this repository:
   ```bash
   git clone https://github.com/iraklisKan/python-todo-list.git
   cd python-todo-list/todolist
   ```
3. Run the CLI application:
   ```bash
   python cli.py
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

### Web Version
- **Framework**: Streamlit
- **Language**: Python 3.12
- **Deployment**: Streamlit Cloud
- **Features**: Interactive checkboxes, real-time updates, modern UI

### CLI Version
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
