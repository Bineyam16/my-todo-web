import streamlit as st
from modules.functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    write_todos(todos)


todos = get_todos()
st.title("TODO APP")
st.subheader("This is a todo app")
st.write("For increaseing your performace")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
