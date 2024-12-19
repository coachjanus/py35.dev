# 
from todo.model import Todo
from todo.todos import TodoList

from rich.console import Console
from rich.table import Table

from todo import __app_name__, __version__, TITLE, helpers

import typer

console = Console()
app = typer.Typer()

header = Todo.make_header()

def show(tasks):
    table = Table(show_header=True, header_style="bold blue")

    for item in header:
        table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])

    for index, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task._category)
        is_done = Todo.DONE if task._status == 2 else Todo.PENDING
        table.add_row(str(index), task._task, f"[{c}]{task._category}[/{c}]", is_done)

    console.print(table)

@app.command()
def run():

    helpers.hello()

    todo_list = TodoList()

    todo_list.add('To do somethong', 'Work')
    todo_list.add('To do somethong other', 'Study')

    while True:
        match helpers.make_your_choice():
            case 'a':
                category = helpers.choose_category()
                task = helpers.add_your_task()
                todo_list.add(task, category)
            case 'l':
                tasks = todo_list.get_todo_list()
                show(tasks)

            case 'u':
                position = helpers.your_task()
                todo_list.complete(int(position))
                tasks = todo_list.get_todo_list()
            case 'r':
                position = helpers.your_task()
                todo_list.delete(int(position))
                tasks = todo_list.get_todo_list()
            case 'q':
                helpers.bye(TITLE)
                break
            case _:
                helpers.help_me()


