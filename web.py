import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)

st.title("FGC To-do App")
st.subheader("This is my to-do web app")
st.write("This app designed to improve your productivity!")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        # st.session_state.pop(i, None)
        st.rerun()


st.text_input(label="Add a new task", label_visibility="collapsed",
              placeholder="Add new todo ...", on_change=add_todo, key="new_todo" )



