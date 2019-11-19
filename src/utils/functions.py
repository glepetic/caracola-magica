import sys
from random import randint
from time import sleep


def join_script_arguments():
    sys.argv.pop(0)
    return "".join(sys.argv)


def get_file_content(file_path):
    f = open(file_path, "r")
    if f.mode == "r":
        return f.read()


def choose_replies_file():
    return choose_random_value(["positive", "neutral", "negative"])


def choose_random_value(values_list):
    return values_list[randint(0, len(values_list) - 1)]


def overwriter_string(string):
    return "\r{}".format(string)


def overwrite_print(string):
    print(overwriter_string(string), end="")


def loader():
    loader_msg = "Pensando"
    for _ in range(0, 5):
        loader_msg += "."
        overwrite_print(loader_msg)
        sleep(1)
    overwrite_print(len(loader_msg) * " ")
