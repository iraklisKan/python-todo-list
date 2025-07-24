import file_ops
from my_time import print_current_time
from datetime import datetime

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("🎯 ADVANCED TODO LIST - CLI VERSION")
    print("="*50)
    print("Available commands:")
    print("  add     - Add a new todo item")
    print("  show    - Show all todos")
    print("  edit    - Edit an existing todo")
    print("  complete- Mark a todo as complete")
    print("  delete  - Delete a todo")
    print("  search  - Search todos")
    print("  stats   - Show statistics")
    print("  help    - Show this menu")
    print("  exit    - Exit the application")
    print("="*50)

def display_todos(todos=None, title="All Todos"):
    """Display todos in a formatted way"""
    if todos is None:
        todos = file_ops.read_todos()
    
    if not todos:
        print(f"\n📝 {title}: No todos found!")
        return
    
    print(f"\n📝 {title} ({len(todos)} items):")
    print("-" * 60)
    
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo['completed'] else "⏳"
        priority_emoji = {"High": "🔥", "Medium": "📅", "Low": "💤"}.get(todo.get('priority', 'Medium'), "📅")
        
        print(f"{i:2d}. {status} {todo['text']}")
        print(f"     📁 {todo.get('category', 'General')} | {priority_emoji} {todo.get('priority', 'Medium')} Priority")
        print(f"     📅 Created: {datetime.fromisoformat(todo['created_at']).strftime('%Y-%m-%d %H:%M')}")
        if todo.get('due_date'):
            print(f"     🎯 Due: {todo['due_date']}")
        print()

def add_todo_interactive():
    """Interactive todo addition"""
    print("\n➕ Adding a new todo...")
    
    text = input("📝 Enter todo text: ").strip()
    if not text:
        print("❌ Todo text cannot be empty!")
        return
    
    category = input("📁 Category (default: General): ").strip() or "General"
    
    print("🔥 Priority levels:")
    print("  1. High")
    print("  2. Medium (default)")
    print("  3. Low")
    
    priority_choice = input("Choose priority (1-3): ").strip()
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(priority_choice, "Medium")
    
    due_date = input("🎯 Due date (YYYY-MM-DD, optional): ").strip()
    if due_date and len(due_date) != 10:
        due_date = None
        print("⚠️  Invalid date format, skipping due date")
    
    todo = file_ops.add_todo(text, category, priority, due_date)
    print(f"✅ Todo added successfully! (ID: {todo['id']})")

def edit_todo_interactive():
    """Interactive todo editing"""
    todos = [t for t in file_ops.read_todos() if not t['completed']]
    if not todos:
        print("❌ No todos available to edit!")
        return
    
    display_todos(todos, "Available Todos to Edit")
    
    try:
        choice = int(input("Enter the number of the todo to edit: ")) - 1
        if 0 <= choice < len(todos):
            todo = todos[choice]
            todo_id = todo['id']
            
            print(f"\n✏️ Editing: {todo['text']}")
            print("Leave empty to keep current value:")
            
            new_text = input(f"📝 New text ({todo['text']}): ").strip()
            new_category = input(f"📁 New category ({todo.get('category', 'General')}): ").strip()
            
            print("🔥 Priority levels:")
            print("  1. High")
            print("  2. Medium")
            print("  3. Low")
            priority_choice = input(f"New priority ({todo.get('priority', 'Medium')}): ").strip()
            priority_map = {"1": "High", "2": "Medium", "3": "Low"}
            new_priority = priority_map.get(priority_choice, todo.get('priority', 'Medium'))
            
            new_due_date = input(f"🎯 New due date ({todo.get('due_date', 'None')}): ").strip()
            
            # Prepare updates
            updates = {}
            if new_text:
                updates['text'] = new_text
            if new_category:
                updates['category'] = new_category
            if priority_choice:
                updates['priority'] = new_priority
            if new_due_date and new_due_date.lower() != 'none':
                updates['due_date'] = new_due_date if len(new_due_date) == 10 else todo.get('due_date')
            
            if updates:
                file_ops.update_todo(todo_id, **updates)
                print("✅ Todo updated successfully!")
            else:
                print("ℹ️  No changes made.")
        else:
            print("❌ Invalid todo number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def complete_todo_interactive():
    """Interactive todo completion"""
    todos = [t for t in file_ops.read_todos() if not t['completed']]
    if not todos:
        print("❌ No todos available to complete!")
        return
    
    display_todos(todos, "Available Todos to Complete")
    
    try:
        choice = int(input("Enter the number of the todo to complete: ")) - 1
        if 0 <= choice < len(todos):
            todo = todos[choice]
            file_ops.update_todo(todo['id'], completed=True)
            print(f"✅ Todo '{todo['text']}' marked as complete!")
        else:
            print("❌ Invalid todo number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_todo_interactive():
    """Interactive todo deletion"""
    todos = file_ops.read_todos()
    if not todos:
        print("❌ No todos available to delete!")
        return
    
    display_todos(todos, "All Todos")
    
    try:
        choice = int(input("Enter the number of the todo to delete: ")) - 1
        if 0 <= choice < len(todos):
            todo = todos[choice]
            confirm = input(f"⚠️  Are you sure you want to delete '{todo['text']}'? (y/N): ").lower()
            if confirm == 'y':
                file_ops.delete_todo(todo['id'])
                print("🗑️ Todo deleted successfully!")
            else:
                print("ℹ️  Deletion cancelled.")
        else:
            print("❌ Invalid todo number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def search_todos_interactive():
    """Interactive todo search"""
    query = input("🔍 Enter search query: ").strip()
    if not query:
        print("❌ Search query cannot be empty!")
        return
    
    results = file_ops.search_todos(query)
    if results:
        display_todos(results, f"Search Results for '{query}'")
    else:
        print(f"❌ No todos found matching '{query}'!")

def show_statistics():
    """Display todo statistics"""
    todos = file_ops.read_todos()
    if not todos:
        print("❌ No todos available for statistics!")
        return
    
    total = len(todos)
    completed = len([t for t in todos if t['completed']])
    pending = total - completed
    
    # Category stats
    categories = {}
    priorities = {"High": 0, "Medium": 0, "Low": 0}
    
    for todo in todos:
        cat = todo.get('category', 'General')
        categories[cat] = categories.get(cat, 0) + 1
        prio = todo.get('priority', 'Medium')
        priorities[prio] = priorities.get(prio, 0) + 1
    
    print("\n📊 TODO STATISTICS")
    print("="*40)
    print(f"📝 Total todos: {total}")
    print(f"✅ Completed: {completed}")
    print(f"⏳ Pending: {pending}")
    print(f"📈 Completion rate: {(completed/total*100):.1f}%")
    
    print("\n📁 By Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    
    print("\n🔥 By Priority:")
    for prio, count in priorities.items():
        if count > 0:
            emoji = {"High": "🔥", "Medium": "📅", "Low": "💤"}[prio]
            print(f"  {emoji} {prio}: {count}")

def main():
    """Main CLI application loop"""
    print(f"🕐 Current date and time: {print_current_time().strftime('%d-%m-%Y %H:%M')}")
    display_menu()
    
    while True:
        try:
            user_action = input("\n🎯 Enter command: ").strip().lower()
            
            if user_action.startswith('add'):
                add_todo_interactive()
            
            elif user_action.startswith('show'):
                display_todos()
            
            elif user_action.startswith('edit'):
                edit_todo_interactive()
            
            elif user_action.startswith('complete'):
                complete_todo_interactive()
            
            elif user_action.startswith('delete'):
                delete_todo_interactive()
            
            elif user_action.startswith('search'):
                search_todos_interactive()
            
            elif user_action.startswith('stats'):
                show_statistics()
            
            elif user_action.startswith('help'):
                display_menu()
            
            elif user_action.startswith('exit'):
                print("👋 Goodbye! Have a productive day!")
                break
            
            else:
                print("❌ Unknown command! Type 'help' to see available commands.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Have a productive day!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again or type 'help' for available commands.")

if __name__ == "__main__":
    main()
