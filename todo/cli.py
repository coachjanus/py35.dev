# 
from todo.model import Todo
from todo.todos import TodoList

from rich.console import Console
from rich.table import Table
from pathlib import Path
from todo import __app_name__, __version__, TITLE, helpers, ERRORS

from todo import db, config, todos

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
def init(db_path = typer.Option(str(db.DEFAULT_DB_FILE_PATH), prompt="Database location?")):
    app_init_error = config.init_app(db_path)

    if app_init_error:
        typer.secho(
            f"Creating config file failed with {ERRORS[app_init_error]}", fg=typer.colors.RED)
        raise typer.Exit(1)
    
    db_init_error = db.init_database(Path(db_path))

    if db_init_error:
        typer.secho(
            f"Creating database failed with {ERRORS[db_init_error]}", fg=typer.colors.RED)
        raise typer.Exit(1)
    
    typer.secho(
            f"The database is {db_path}", fg=typer.colors.GREEN)


def get_todo_list():
    if config.CONFIG_FILE_PATH.exists():
        db_path = db.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            f"Config file NOT found. Please run todo init", fg=typer.colors.RED)
        raise typer.Exit(1)
    
    if db_path.exists():
        return todos.TodoList(db_path)
    else:
        typer.secho(
            f"Databse NOT found. Please run todo init", fg=typer.colors.RED)
        raise typer.Exit(1)
    

@app.command()
def run():

    helpers.hello()

    todo_list = get_todo_list()

    # todo_list.add('To do somethong', 'Work')
    # todo_list.add('To do somethong other', 'Study')

    while True:
        match helpers.make_your_choice():
            case 'a':
                category = helpers.choose_category()
                task = helpers.add_your_task()

                td, error = todo_list.add(task, category)

                if error:
                    typer.secho(
                        f"Adding todo failed with {ERRORS[error]}.", fg=typer.colors.RED)
                    raise typer.Exit(1)
                else:
                    typer.secho(f"Task was added successfuly", fg=typer.colors.GREEN)


            case 'l':
                tasks, error = todo_list.get_todo_list()
               
                if error:
                    typer.secho(
                        f"Fatching tasksd failed with {ERRORS[error]}.", fg=typer.colors.RED)
                    raise typer.Exit(1)
                else:
                    if len(tasks == 0):
                        typer.secho(f"There are no tasks in the todo list yet", fg=typer.colors.GREEN)
                    else:
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


