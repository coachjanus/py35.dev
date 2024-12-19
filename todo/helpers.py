import typer
from rich.prompt import Prompt
from todo import __app_name__, __version__
from todo.model import Todo
from rich import print as rprint

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

def make_your_choice():
    return Prompt.ask("[bold green on blue] Make Your choice (a|l|u|r|q) [/]")


def bye(TITLE):
    typer.secho(f'Thanks for usong {TITLE}. Have a nice day!', fg=typer.colors.BRIGHT_GREEN)

def hello():
    rprint(f"[bold magenta] {__app_name__.upper()} [/bold magenta]", chr(128187), f"[bold magenta] {__version__} [/bold magenta]")


def join_category():
    res = ""
    for k,v in Todo.COLORS.items():
        res += f"[bold white on {v}] {k} [/]"
    return res


def make_title(fn):
    def wrapper():
        func = fn()
        output = func.title()
        return output
    return wrapper


@make_title
def choose_category():
    return Prompt.ask("[bold green on blue]Choose some category: [/]" + join_category(), default='Work')

@make_title
def add_your_task():
    return Prompt.ask("[bold green on blue]Text Your task: [/]", default='Tp do something other')

@make_title
def your_task():
    return Prompt.ask("[bold green on blue]Enter Your task: [/]", default=0)