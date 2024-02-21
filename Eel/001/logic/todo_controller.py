
import eel

from data.todo import Todo

todo_app = Todo()

@eel.expose
def add(task):
    todo_app.add(task)

@eel.expose
def delete(task):
    todo_app.delete(task)

@eel.expose
def get_tasks():
    return todo_app.get_tasks()