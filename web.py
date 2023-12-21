import streamlit as st
import functions

fp = r'C:\Users\Jacek\PycharmProjects\web_app1\todos.txt'
todos = functions.read_todos(filepath=fp)


def add_todo():
    loc_todo = st.session_state['item'] + '\n'
    todos.append(loc_todo)
    functions.write_todos(todos_arg=todos, filepath=fp)


st.title('My to do app')
st.subheader('This is my todo app')
st.write('Please type in only the basic letters')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'{todo}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos_arg=todos, filepath=fp)
        del st.session_state['item']
        st.experimental_rerun()

st.text_input(label='Enter a todo', placeholder='Add a new todo...',
              on_change=add_todo, key='item')
