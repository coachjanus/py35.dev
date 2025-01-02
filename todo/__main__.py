""" To-Do entry point script. todo/__main__.py"""

from todo import cli, __app_name__

def main():
    """This is entry point function. """

    cli.app(prog_name = __app_name__)

if __name__ == "__main__":

    # 1 + "two"  # This line never runs, so no TypeError is raised
    # # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    main()

    # import doctest
    # doctest.testmod()


