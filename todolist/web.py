import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import file_ops
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="Advanced Todo App",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .todo-item {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        background-color: #f8f9fa;
    }
    
    .priority-high {
        border-left-color: #dc3545 !important;
    }
    
    .priority-medium {
        border-left-color: #ffc107 !important;
    }
    
    .priority-low {
        border-left-color: #28a745 !important;
    }
    
    .completed-todo {
        opacity: 0.6;
        text-decoration: line-through;
    }
    
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Todo List"
    if 'edit_todo_id' not in st.session_state:
        st.session_state.edit_todo_id = None
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""
    if 'filter_category' not in st.session_state:
        st.session_state.filter_category = "All"
    if 'filter_priority' not in st.session_state:
        st.session_state.filter_priority = "All"
    if 'show_completed' not in st.session_state:
        st.session_state.show_completed = False

def get_filtered_todos():
    """Get todos based on current filters"""
    todos = file_ops.read_todos()
    
    # Filter by completion status
    if not st.session_state.show_completed:
        todos = [todo for todo in todos if not todo['completed']]
    
    # Filter by search query
    if st.session_state.search_query:
        todos = [todo for todo in todos if st.session_state.search_query.lower() in todo['text'].lower()]
    
    # Filter by category
    if st.session_state.filter_category != "All":
        todos = [todo for todo in todos if todo.get('category', 'General') == st.session_state.filter_category]
    
    # Filter by priority
    if st.session_state.filter_priority != "All":
        todos = [todo for todo in todos if todo.get('priority', 'Medium') == st.session_state.filter_priority]
    
    return todos

def get_categories():
    """Get all unique categories"""
    todos = file_ops.read_todos()
    categories = set([todo.get('category', 'General') for todo in todos])
    return sorted(list(categories))

def render_sidebar():
    """Render the sidebar with navigation and filters"""
    st.sidebar.title("🎯 Todo App")
    
    # Navigation
    pages = ["Todo List", "Add Todo", "Statistics", "Settings"]
    st.session_state.current_page = st.sidebar.selectbox("Navigate", pages, index=pages.index(st.session_state.current_page))
    
    st.sidebar.markdown("---")
    
    # Filters (only show on Todo List page)
    if st.session_state.current_page == "Todo List":
        st.sidebar.subheader("🔍 Filters")
        
        # Search
        st.session_state.search_query = st.sidebar.text_input("Search todos", value=st.session_state.search_query)
        
        # Category filter
        categories = ["All"] + get_categories()
        st.session_state.filter_category = st.sidebar.selectbox("Category", categories, index=categories.index(st.session_state.filter_category) if st.session_state.filter_category in categories else 0)
        
        # Priority filter
        priorities = ["All", "High", "Medium", "Low"]
        st.session_state.filter_priority = st.sidebar.selectbox("Priority", priorities, index=priorities.index(st.session_state.filter_priority))
        
        # Show completed
        st.session_state.show_completed = st.sidebar.checkbox("Show completed", value=st.session_state.show_completed)
        
        if st.sidebar.button("Clear Filters"):
            st.session_state.search_query = ""
            st.session_state.filter_category = "All"
            st.session_state.filter_priority = "All"
            st.session_state.show_completed = False
            st.rerun()

def render_todo_item(todo: Dict):
    """Render a single todo item"""
    priority_class = f"priority-{todo.get('priority', 'medium').lower()}"
    completed_class = "completed-todo" if todo['completed'] else ""
    
    with st.container():
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        
        with col1:
            # Todo text and details
            st.markdown(f"""
                <div class="todo-item {priority_class} {completed_class}">
                    <h4>{todo['text']}</h4>
                    <small>
                        📁 {todo.get('category', 'General')} | 
                        🔥 {todo.get('priority', 'Medium')} | 
                        📅 {datetime.fromisoformat(todo['created_at']).strftime('%Y-%m-%d %H:%M')}
                        {f" | 🎯 Due: {todo['due_date']}" if todo.get('due_date') else ""}
                    </small>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Complete/Uncomplete toggle
            new_status = st.checkbox("✅", value=todo['completed'], key=f"complete_{todo['id']}")
            if new_status != todo['completed']:
                file_ops.update_todo(todo['id'], completed=new_status)
                st.rerun()
        
        with col3:
            # Edit button
            if st.button("✏️", key=f"edit_{todo['id']}", help="Edit todo"):
                st.session_state.edit_todo_id = todo['id']
                st.rerun()
        
        with col4:
            # Delete button
            if st.button("🗑️", key=f"delete_{todo['id']}", help="Delete todo"):
                file_ops.delete_todo(todo['id'])
                st.success("Todo deleted!")
                st.rerun()

def render_todo_list():
    """Render the main todo list page"""
    st.markdown('<h1 class="main-header">📝 My Advanced Todo List</h1>', unsafe_allow_html=True)
    
    # Quick stats
    all_todos = file_ops.read_todos()
    total_todos = len(all_todos)
    completed_todos = len([t for t in all_todos if t['completed']])
    pending_todos = total_todos - completed_todos
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class="stats-card">
                <h3>{total_todos}</h3>
                <p>Total Todos</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="stats-card">
                <h3>{pending_todos}</h3>
                <p>Pending</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="stats-card">
                <h3>{completed_todos}</h3>
                <p>Completed</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Edit modal
    if st.session_state.edit_todo_id:
        todo = file_ops.get_todo_by_id(st.session_state.edit_todo_id)
        if todo:
            st.subheader("✏️ Edit Todo")
            
            with st.form("edit_todo_form"):
                new_text = st.text_area("Todo text", value=todo['text'])
                new_category = st.text_input("Category", value=todo.get('category', 'General'))
                new_priority = st.selectbox("Priority", ["High", "Medium", "Low"], index=["High", "Medium", "Low"].index(todo.get('priority', 'Medium')))
                new_due_date = st.date_input("Due date", value=date.fromisoformat(todo['due_date']) if todo.get('due_date') else None)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("💾 Save Changes"):
                        file_ops.update_todo(
                            st.session_state.edit_todo_id,
                            text=new_text,
                            category=new_category,
                            priority=new_priority,
                            due_date=new_due_date.isoformat() if new_due_date else None
                        )
                        st.session_state.edit_todo_id = None
                        st.success("Todo updated!")
                        st.rerun()
                
                with col2:
                    if st.form_submit_button("❌ Cancel"):
                        st.session_state.edit_todo_id = None
                        st.rerun()
            
            st.markdown("---")
    
    # Display todos
    todos = get_filtered_todos()
    
    if not todos:
        st.info("🎉 No todos found! Add some tasks or adjust your filters.")
    else:
        st.subheader(f"📋 Todos ({len(todos)} items)")
        
        # Sort options
        sort_by = st.selectbox("Sort by", ["Created Date", "Priority", "Category", "Due Date"])
        reverse_order = st.checkbox("Reverse order")
        
        if sort_by == "Created Date":
            todos.sort(key=lambda x: x['created_at'], reverse=reverse_order)
        elif sort_by == "Priority":
            priority_order = {"High": 3, "Medium": 2, "Low": 1}
            todos.sort(key=lambda x: priority_order.get(x.get('priority', 'Medium'), 2), reverse=not reverse_order)
        elif sort_by == "Category":
            todos.sort(key=lambda x: x.get('category', 'General'), reverse=reverse_order)
        elif sort_by == "Due Date":
            todos.sort(key=lambda x: x.get('due_date', '9999-12-31') or '9999-12-31', reverse=reverse_order)
        
        for todo in todos:
            render_todo_item(todo)

def render_add_todo():
    """Render the add todo page"""
    st.markdown('<h1 class="main-header">➕ Add New Todo</h1>', unsafe_allow_html=True)
    
    with st.form("add_todo_form"):
        st.subheader("📝 Todo Details")
        
        todo_text = st.text_area("What needs to be done?", placeholder="Enter your todo item here...")
        
        col1, col2 = st.columns(2)
        with col1:
            category = st.text_input("Category", value="General", placeholder="Work, Personal, Shopping, etc.")
            priority = st.selectbox("Priority", ["High", "Medium", "Low"], index=1)
        
        with col2:
            due_date = st.date_input("Due date (optional)", value=None)
            
        if st.form_submit_button("➕ Add Todo", type="primary"):
            if todo_text.strip():
                file_ops.add_todo(
                    text=todo_text.strip(),
                    category=category.strip() or "General",
                    priority=priority,
                    due_date=due_date.isoformat() if due_date else None
                )
                st.success("✅ Todo added successfully!")
                st.balloons()
            else:
                st.error("❌ Please enter a todo item!")

def render_statistics():
    """Render the statistics page"""
    st.markdown('<h1 class="main-header">📊 Todo Statistics</h1>', unsafe_allow_html=True)
    
    todos = file_ops.read_todos()
    
    if not todos:
        st.info("📈 No data available. Add some todos to see statistics!")
        return
    
    # Prepare data
    df = pd.DataFrame(todos)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['category'] = df['category'].fillna('General')
    df['priority'] = df['priority'].fillna('Medium')
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Todos", len(todos))
    
    with col2:
        completed = len(df[df['completed'] == True])
        st.metric("Completed", completed)
    
    with col3:
        completion_rate = (completed / len(todos) * 100) if todos else 0
        st.metric("Completion Rate", f"{completion_rate:.1f}%")
    
    with col4:
        high_priority = len(df[df['priority'] == 'High'])
        st.metric("High Priority", high_priority)
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Todos by Category")
        category_counts = df['category'].value_counts()
        fig_category = px.pie(values=category_counts.values, names=category_counts.index, 
                            title="Distribution by Category")
        st.plotly_chart(fig_category, use_container_width=True)
    
    with col2:
        st.subheader("🔥 Todos by Priority")
        priority_counts = df['priority'].value_counts()
        colors = {'High': '#dc3545', 'Medium': '#ffc107', 'Low': '#28a745'}
        fig_priority = px.bar(x=priority_counts.index, y=priority_counts.values,
                            title="Distribution by Priority",
                            color=priority_counts.index,
                            color_discrete_map=colors)
        st.plotly_chart(fig_priority, use_container_width=True)
    
    # Timeline
    st.subheader("📈 Todo Creation Timeline")
    df['date'] = df['created_at'].dt.date
    daily_counts = df.groupby('date').size().reset_index(name='count')
    fig_timeline = px.line(daily_counts, x='date', y='count', 
                          title="Todos Created Over Time")
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Completion analysis
    st.subheader("✅ Completion Analysis")
    completion_by_category = df.groupby('category')['completed'].agg(['count', 'sum']).reset_index()
    completion_by_category['completion_rate'] = (completion_by_category['sum'] / completion_by_category['count'] * 100).round(1)
    completion_by_category = completion_by_category.rename(columns={'count': 'total', 'sum': 'completed'})
    
    st.dataframe(completion_by_category, use_container_width=True)

def render_settings():
    """Render the settings page"""
    st.markdown('<h1 class="main-header">⚙️ Settings & Tools</h1>', unsafe_allow_html=True)
    
    # Export/Import section
    st.subheader("💾 Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📤 Export Data**")
        todos = file_ops.read_todos()
        if todos:
            df = pd.DataFrame(todos)
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv_data,
                file_name=f"todos_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        else:
            st.info("No todos to export")
    
    with col2:
        st.markdown("**📤 Import Data**")
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Preview:")
                st.dataframe(df.head())
                
                if st.button("Import Data"):
                    # Convert dataframe back to todos format
                    imported_todos = df.to_dict('records')
                    file_ops.write_todos(imported_todos)
                    st.success("Data imported successfully!")
                    st.rerun()
            except Exception as e:
                st.error(f"Error importing file: {e}")
    
    st.markdown("---")
    
    # Bulk operations
    st.subheader("🔧 Bulk Operations")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Mark All Complete"):
            todos = file_ops.read_todos()
            for todo in todos:
                if not todo['completed']:
                    file_ops.update_todo(todo['id'], completed=True)
            st.success("All todos marked as complete!")
            st.rerun()
    
    with col2:
        if st.button("🔄 Mark All Incomplete"):
            todos = file_ops.read_todos()
            for todo in todos:
                if todo['completed']:
                    file_ops.update_todo(todo['id'], completed=False)
            st.success("All todos marked as incomplete!")
            st.rerun()
    
    with col3:
        if st.button("🗑️ Delete Completed", type="secondary"):
            todos = file_ops.read_todos()
            for todo in todos:
                if todo['completed']:
                    file_ops.delete_todo(todo['id'])
            st.success("Completed todos deleted!")
            st.rerun()
    
    st.markdown("---")
    
    # Danger zone
    st.subheader("⚠️ Danger Zone")
    
    with st.expander("🚨 Delete All Data"):
        st.warning("This action cannot be undone!")
        confirm_text = st.text_input("Type 'DELETE ALL' to confirm:")
        if confirm_text == "DELETE ALL":
            if st.button("🗑️ Delete Everything", type="secondary"):
                file_ops.write_todos([])
                st.success("All data deleted!")
                st.rerun()

def main():
    """Main application function"""
    init_session_state()
    render_sidebar()
    
    # Route to appropriate page
    if st.session_state.current_page == "Todo List":
        render_todo_list()
    elif st.session_state.current_page == "Add Todo":
        render_add_todo()
    elif st.session_state.current_page == "Statistics":
        render_statistics()
    elif st.session_state.current_page == "Settings":
        render_settings()
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>🚀 Advanced Todo App - Built with Streamlit & Python</p>
            <p>💡 <a href="https://github.com/iraklisKan/python-todo-list" target="_blank">View on GitHub</a></p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
