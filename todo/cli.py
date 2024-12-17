# 
from todo.model import Todo
from todo.todos import TodoList

from rich.console import Console
from rich.table import Table

from todo import __app_name__, __version__

console = Console()
header = Todo.make_header()



def show(tasks):
    console.print(f"[bold magenta] {__app_name__.upper()} [/bold magenta]", chr(128187), f"[bold magenta] {__version__} [/bold magenta]")
    table = Table(show_header=True, header_style="bold blue")

    for item in header:
        table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])

    for index, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task._category)
        is_done = Todo.DONE if task._status == 2 else Todo.PENDING
        table.add_row(str(index), task._task, f"[{c}]{task._category}[/{c}]", is_done)

    console.print(table)

def app():
    print(Todo.DONE, Todo.PENDING)
    # print(Todo.make_header())

    todo_list = TodoList()

    td1 = Todo('To do somethong', 'Work')
    print(td1)
    todo_list.add(td1)

    td2 = Todo('To do somethong other', 'Stidy')
    print(td2)
    todo_list.add(td2)

    tasks = todo_list.get_todo_list()

    show(tasks)

    todo_list.complete(2)
    tasks = todo_list.get_todo_list()
    show(tasks)


    