import os
import json
from datetime import datetime
from typing import List, Dict, Any

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, 'todoText', 'todos.json')
legacy_filepath = os.path.join(script_dir, 'todoText', 'todos.txt')

def migrate_legacy_todos():
    """Migrate from old txt format to new json format"""
    if os.path.exists(legacy_filepath) and not os.path.exists(filepath):
        try:
            with open(legacy_filepath, 'r') as file:
                old_todos = file.readlines()
            
            new_todos = []
            for i, todo in enumerate(old_todos):
                todo = todo.strip()
                if todo:
                    new_todos.append({
                        'id': i + 1,
                        'text': todo,
                        'completed': False,
                        'created_at': datetime.now().isoformat(),
                        'category': 'General',
                        'priority': 'Medium',
                        'due_date': None
                    })
            
            write_todos(new_todos)
            # Backup old file
            os.rename(legacy_filepath, legacy_filepath + '.backup')
        except Exception as e:
            print(f"Migration failed: {e}")

def read_todos(filename=filepath) -> List[Dict[str, Any]]:
    """Read todos from JSON file"""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Check for legacy migration
    migrate_legacy_todos()
    
    if not os.path.exists(filename):
        # Create the file if it doesn't exist
        with open(filename, 'w') as file:
            json.dump([], file)
        return []
    
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, Exception):
        # If file is corrupted, return empty list
        return []

def write_todos(todos: List[Dict[str, Any]], filename=filepath):
    """Write todos to JSON file"""
    try:
        with open(filename, 'w') as file:
            json.dump(todos, file, indent=2)
    except Exception as e:
        print(f"Error writing todos: {e}")

def add_todo(text: str, category: str = "General", priority: str = "Medium", due_date: str = None) -> Dict[str, Any]:
    """Add a new todo item"""
    todos = read_todos()
    
    # Generate new ID
    max_id = max([todo.get('id', 0) for todo in todos], default=0)
    new_id = max_id + 1
    
    new_todo = {
        'id': new_id,
        'text': text.strip(),
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'category': category,
        'priority': priority,
        'due_date': due_date
    }
    
    todos.append(new_todo)
    write_todos(todos)
    return new_todo

def update_todo(todo_id: int, **updates) -> bool:
    """Update a specific todo by ID"""
    todos = read_todos()
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo.update(updates)
            write_todos(todos)
            return True
    return False

def delete_todo(todo_id: int) -> bool:
    """Delete a todo by ID"""
    todos = read_todos()
    
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos.pop(i)
            write_todos(todos)
            return True
    return False

def get_todo_by_id(todo_id: int) -> Dict[str, Any]:
    """Get a specific todo by ID"""
    todos = read_todos()
    
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def get_todos_by_category(category: str) -> List[Dict[str, Any]]:
    """Get todos filtered by category"""
    todos = read_todos()
    return [todo for todo in todos if todo.get('category', 'General') == category]

def get_todos_by_priority(priority: str) -> List[Dict[str, Any]]:
    """Get todos filtered by priority"""
    todos = read_todos()
    return [todo for todo in todos if todo.get('priority', 'Medium') == priority]

def search_todos(query: str) -> List[Dict[str, Any]]:
    """Search todos by text content"""
    todos = read_todos()
    query = query.lower()
    return [todo for todo in todos if query in todo['text'].lower()]

# Legacy functions for backward compatibility
def read_todos_legacy():
    """Legacy function that returns todos as text lines"""
    todos = read_todos()
    return [todo['text'] + '\n' for todo in todos if not todo['completed']]

def write_todos_legacy(todo_lines):
    """Legacy function that accepts text lines"""
    todos = []
    for i, line in enumerate(todo_lines):
        text = line.strip()
        if text:
            todos.append({
                'id': i + 1,
                'text': text,
                'completed': False,
                'created_at': datetime.now().isoformat(),
                'category': 'General',
                'priority': 'Medium',
                'due_date': None
            })
    write_todos(todos)