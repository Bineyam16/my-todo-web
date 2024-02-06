FILEPATH = 'todo.txt'
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(write_todos, filepath=FILEPATH):
    with open(filepath, 'w') as file_writer:
        file_writer.writelines(write_todos)


if __name__ == "__main__":
    print("hello from function")