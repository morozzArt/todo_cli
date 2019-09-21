import click
from Adder import Adder
from Shower import Shower


def print_parentheses(func):
    def wrapper(*args):
        print("[", end="")
        func(*args)
        print("]", end=" ")
    return wrapper


@print_parentheses
def print_cell(cell):
    click.echo(click.style(cell, fg="green"), nl=False)


@click.group()
def todo():
    pass


@todo.command(help="Show all todo note")
def list():
    list_note = Shower.get_list_note()
    for note in list_note:
        print_cell(note.get_id)
        print_cell(note.get_symbol_status)
        print_cell(note.get_date.split()[0])
        print(note.get_text)


@todo.command(help="Add new todo note")
@click.argument('content', type=str)
def add(content):
    Adder.add_note(content)


@todo.command(help="Reset todo application. Clean all note")
def reset():
    Adder.reset()


if __name__ == '__main__':
    todo()
