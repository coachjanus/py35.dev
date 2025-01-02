import typer
from rich.prompt import Prompt
from todo import __app_name__, __version__

from rich import print as rprint
from rich.table import Table
from todo.model import Todo

def make_title(fn):
   '''This decorator function is a higher order function that takes a function as a parameter'''

   def wrapper():
       func = fn()
       output = func.title()
       return output

   return wrapper

def help_me():
    typer.secho(f"""
    All That You Can Do:
        l : List existing tasks
        a : Add new task
        u : Update existing task
        r : Remove existing task
        h : Print this help
        q : Exit
    """, fg=typer.colors.GREEN)


def hello():
    rprint(F"[bold magenta]{__app_name__.upper()}[/bold magenta]", chr(128187), F"[bold magenta]version: {__version__}[/bold magenta]")

def join_category():
    res = ""
    for k,v in Todo.COLORS.items():
        res += f"[bold white on {v}] {k} [/]"
    return res

@make_title
def choose_category():
    # return Prompt.ask("[bold green on blue] Choose some category: [/] [bold white on green] Study [/]|[bold white on red] Work [/]|[bold white on yellow] Learn [/]|[bold white on cyan] Sports [/]", default='Work')
    return Prompt.ask("[bold green on blue] Choose some category: [/] " + join_category(), default='Work')

def make_your_choice():
    return Prompt.ask("[bold green on blue] Make Your choice (a|l|u|r|q) [/]")

@make_title
def add_your_task():
    return Prompt.ask("[bold green on blue] Text Your task [/]", default='To Do something other')

def bye(TITLE):
	typer.secho(f'Thanks for using {TITLE}. Have a nice day!', fg=typer.colors.GREEN)


def make_table(tasks):

    table = Table(show_header=True, header_style="bold blue")

    for item in Todo.make_headers():
        table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])

    for idx, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task['category'])
        is_done_str = Todo.DONE if task['status'] == 2 else Todo.PENDING
        table.add_row(str(idx), task['task'], f'[{c}]{task['category']}[/{c}]', is_done_str)
    return table
