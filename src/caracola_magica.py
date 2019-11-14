import sys
from os.path import dirname
from random import randint


def join_script_arguments():
    sys.argv.pop(0)
    return "".join(sys.argv)


def get_file_content(file_path):
    f = open(file_path, "r")
    if f.mode == "r":
        return f.read()


def choose_random_value(values_list):
    return values_list[randint(0, len(values_list) - 1)]


user_input = ""

# Script arguments validator
if len(sys.argv) == 1:
    print("Diga?")
    user_input = input()
else:
    user_input = join_script_arguments()

if user_input.endswith("?"):
    # Read file and turn content to list
    content = get_file_content(dirname(__file__) + "/../resources/replies")
    replies = content.split("\n")

    print(choose_random_value(replies))
else:
    print("Pero hace una pregunta tarado")
