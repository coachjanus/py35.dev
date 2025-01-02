# todo
from pathlib import Path
import typer
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

from todo import ERRORS, __app_name__, __version__, TITLE, config, model, helpers

from todo.model import Todo
from todo.todos import TodoList

from todo import db
from todo import config 

from typing_extensions import Annotated

app = typer.Typer()

console = Console()

header = Todo.make_header()

def show(tasks):
    console.print(F"[bold magenta]{__app_name__.upper()}[/bold magenta]", chr(128187), F"[bold magenta]{__version__}[/bold magenta]")

    table = Table(show_header=True, header_style="bold blue")

    for item in header:
        table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])

    for index, task in enumerate(tasks, start=1):

        c = Todo.get_category_color(task['category'])
        is_done = Todo.DONE if task['status'] == 2 else Todo.PENDING
        table.add_row(str(index), task['task'], f'[{c}]{task['category']}[/{c}]', is_done)

    console.print(table)

@app.command()
def init(
    db_path: Annotated[
        str,
        typer.Option("--db-path", "-db", prompt="to-do database location?"),
    ]=str(db.DEFAULT_DB_FILE_PATH),
) -> None:
    """Initialize the todo database."""
    app_init_error = config.init_app(db_path)

    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )

        raise typer.Exit(1)

    db_init_error = db.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )

        raise typer.Exit(1)

    typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


def get_todo_list():
    if config.CONFIG_FILE_PATH.exists():
        db_path = db.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "todo init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return TodoList(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "todo init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

@app.command()
def run():
    
    helpers.hello()
   
    while True:
        
        match helpers.make_your_choice():
            case 'a':
                todo_list = get_todo_list()
                category = helpers.choose_category()
                task = helpers.add_your_task()
                td, error = todo_list.add(task, category)

                if error:
                    typer.secho(f'Adding to-do failed with "{ERRORS[error]}"', fg=typer.colors.RED)
                    raise typer.Exit(1)
                else:
                    typer.secho(
                        f"""to-do: "{td}" with category: "{category}" added successfully to database!""",
                        fg=typer.colors.GREEN,
                    )

            case 'l':
                todo_list = get_todo_list()
                tasks, error = todo_list.get_todo_list()

                if error:
                    typer.secho(f'Fetching tasks failed with "{ERRORS[error]}"', fg=typer.colors.RED)
                    raise typer.Exit(1)
                else:
                    if len(tasks) == 0:
                        typer.secho("There are no tasks in the to-do list yet", fg=typer.colors.RED)
                        raise typer.Exit()
                    show(tasks)
            case 'u':
                position = Prompt.ask("Choose your todo ")
                todo_list.complete(int(position))
                tasks = todo_list.get_todo_list()
            case 'r':
                todo_list.delete(1)
            case "q":
                helpers.bye(TITLE)
                break
            case _:
                helpers.help_me()
