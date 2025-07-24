# 🚀 Advanced Todo List Application

A feature-rich todo list application built with Python that comes in two powerful versions:
- **🖥️ Command-line interface (CLI)** for terminal power users
- **🌐 Web interface** using Streamlit for modern browser experience

## ✨ Key Features

### 🎯 Core Functionality
- ➕ **Add** new todo items with rich metadata
- 📋 **View** all todos with beautiful formatting
- ✏️ **Edit** existing todos inline
- ✅ **Complete/Uncomplete** tasks with one click
- 🗑️ **Delete** finished or unwanted tasks
- 🔍 **Search** through your todos
- 📊 **Statistics** and analytics dashboard

### 🏷️ Enhanced Organization
- 📁 **Categories** - Organize todos by type (Work, Personal, Shopping, etc.)
- 🔥 **Priority Levels** - High, Medium, Low with visual indicators
- 📅 **Due Dates** - Set deadlines for important tasks
- 🕐 **Timestamps** - Track when todos were created
- 🎯 **Status Tracking** - Visual completion indicators

### 🎨 Modern Web Interface
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🎨 **Beautiful UI** - Clean, modern interface with custom styling
- 📊 **Interactive Charts** - Visual statistics with Plotly
- 🔧 **Bulk Operations** - Mass complete, delete, or modify todos
- 💾 **Export/Import** - CSV data exchange capabilities
- 🔍 **Advanced Filtering** - Filter by category, priority, completion status

### 🖥️ Enhanced CLI Experience
- 🌈 **Emoji-rich Interface** - Visual icons for better UX
- 📋 **Formatted Display** - Clean, organized todo listings
- 🎯 **Interactive Menus** - Guided input for all operations
- 📊 **Statistics View** - Command-line analytics
- 🔍 **Search Function** - Find todos quickly from terminal

## 🏗️ Project Structure

```
todolist/
├── 🌐 web.py              # Advanced Streamlit web application
├── 🖥️ cli.py              # Enhanced command-line interface
├── 🔧 file_ops.py         # Advanced file operations & data management
├── ⏰ my_time.py          # Date/time utilities
├── 📦 requirements.txt    # Python dependencies
├── 📁 todoText/           # Data storage directory
│   ├── todos.json         # Modern JSON data format
│   └── todos.txt.backup   # Legacy format backup (auto-created)
└── 📚 simioseis/          # Learning notes directory
    └── simioseis.txt      # Python learning reference
```

## 🚀 How to Run

### 🌐 Web Version (Recommended)

#### Option 1: Live Demo
Visit the live demo: [Streamlit Cloud](https://irakliskan-python-todo-list-todolistweb-7mqa2v.streamlit.app/)

#### Option 2: Local Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/iraklisKan/python-todo-list.git
   cd python-todo-list/todolist
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web app**
   ```bash
   streamlit run web.py
   ```

4. **Open your browser** to `http://localhost:8501`

### 🖥️ Command-Line Version

1. **Navigate to the project directory**
   ```bash
   cd python-todo-list/todolist
   ```

2. **Run the CLI**
   ```bash
   python cli.py
   ```

3. **Follow the interactive prompts**

## 📋 Web Interface Features

### 🏠 Main Dashboard
- **Quick Statistics** - Total, pending, and completed todos at a glance
- **Filter & Search** - Real-time filtering by category, priority, or text
- **Sort Options** - Order by date, priority, category, or due date
- **Bulk Actions** - Select and modify multiple todos

### ➕ Add Todo Page
- **Rich Input Form** - Text, category, priority, and due date
- **Smart Defaults** - Intelligent category suggestions
- **Instant Feedback** - Success animations and validation

### 📊 Statistics Dashboard
- **Visual Analytics** - Interactive charts and graphs
- **Completion Rates** - Track your productivity over time
- **Category Breakdown** - See where you spend most time
- **Priority Analysis** - Understand your task urgency patterns
- **Timeline View** - Todo creation trends

### ⚙️ Settings & Tools
- **Export Data** - Download todos as CSV for backup
- **Import Data** - Upload CSV files to restore data
- **Bulk Operations** - Mass complete/delete operations
- **Data Management** - Safe data reset options

## 🖥️ CLI Commands

```bash
🎯 Available Commands:
  add      - Add a new todo with category, priority, and due date
  show     - Display all todos with formatting and details
  edit     - Edit existing todos interactively
  complete - Mark todos as completed
  delete   - Remove todos with confirmation
  search   - Find todos by text content
  stats    - View detailed statistics
  help     - Show command reference
  exit     - Close the application
```

## 💾 Data Format

The application uses a modern JSON format for enhanced functionality:

```json
{
  "id": 1,
  "text": "Complete project documentation",
  "completed": false,
  "created_at": "2025-01-24T10:30:00",
  "category": "Work",
  "priority": "High",
  "due_date": "2025-01-25"
}
```

## 🔄 Migration from Legacy Format

The application automatically detects and migrates old `todos.txt` files to the new JSON format while preserving your data. Legacy files are backed up as `todos.txt.backup`.

## 🛠️ Technology Stack

- **🐍 Python 3.12+** - Core language
- **🌐 Streamlit** - Modern web framework
- **📊 Plotly** - Interactive visualizations
- **🐼 Pandas** - Data manipulation
- **📅 datetime** - Date/time handling
- **📄 JSON** - Modern data storage

## 🎨 Design Philosophy

This application follows modern software design principles:

- **📱 Mobile-First** - Responsive design for all devices
- **🎯 User-Centric** - Intuitive interface and workflows
- **⚡ Performance** - Fast, efficient operations
- **🔒 Data Safety** - Automatic backups and validation
- **🎨 Visual Appeal** - Beautiful, engaging interface
- **♿ Accessibility** - Clear navigation and feedback

## 🚀 Future Enhancements

- 🔔 **Notifications** - Reminders for due dates
- 🌙 **Dark Mode** - Theme switching
- 👥 **Collaboration** - Shared todo lists
- 📱 **Mobile App** - Native mobile version
- 🔄 **Sync** - Cloud synchronization
- 🏆 **Gamification** - Achievement system

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**🎯 Made with ❤️ using Python & Streamlit**

[⭐ Star this repo](https://github.com/iraklisKan/python-todo-list) | [🐛 Report Bug](https://github.com/iraklisKan/python-todo-list/issues) | [💡 Request Feature](https://github.com/iraklisKan/python-todo-list/issues)

</div>
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
