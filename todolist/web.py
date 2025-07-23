import streamlit as st
import file_ops


def add_todo():
    todo_item = st.session_state["new_todo"]
    if todo_item.strip():  # Only add if not empty
        todos = file_ops.read_todos()
        todos.append(todo_item + "\n")
        file_ops.write_todos(todos)
      

todos = file_ops.read_todos()

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("This app allows you to manage your todo items interactively.")


for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)  # Use strip to avoid leading/trailing spaces in keys
    if checkbox:
        todos.pop(index)
        file_ops.write_todos(todos)
        del st.session_state[todo]  
        st.rerun()


st.text_input(label="", placeholder="Add a new todo item",on_change=add_todo, key='new_todo')
