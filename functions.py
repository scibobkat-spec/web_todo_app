FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):

    """Reads todos from a file and returns a list of strings"""

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):

    """ Writes todos to a file"""

    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    todos = get_todos()
    write_todos(todos)