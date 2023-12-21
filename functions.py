def read_todos(filepath):
    """ Opens file in read mode and converts it into list """
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos

def write_todos(todos_arg, filepath):
    """ Opens the file in write mode and overwrites it with defined list"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# if __name__ == "__main__":
#     print("Hello")
#     print(read_todos(filepath))