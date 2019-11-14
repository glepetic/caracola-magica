import sys
from os.path import dirname
from utils.functions import join_script_arguments, get_file_content, loader, overwriter_string, overwrite_print, choose_random_value


# Script arguments validator
if len(sys.argv) == 1:
    print("Si?")
    user_input = input()
else:
    user_input = join_script_arguments()

# Verify that it's a question
if user_input.endswith("?"):

    # Read file and turn content to list
    content = get_file_content(dirname(__file__) + "/../resources/replies")
    replies = content.split("\n")

    # Load then choose reply
    loader()
    print(overwriter_string(choose_random_value(replies)))

else:
    print("Pero hace una pregunta boludo")
