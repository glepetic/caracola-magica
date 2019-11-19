import sys
from os.path import dirname
import utils.functions as f

# Script arguments validator
if len(sys.argv) == 1:
    print("Si?")
    user_input = input()
else:
    user_input = f.join_script_arguments()

# Verify that it's a question
if user_input.endswith("?"):

    # Read file and turn content to list
    content = f.get_file_content(dirname(__file__) + "/../resources/{}".format(f.choose_replies_file()))
    replies = content.split("\n")

    # Load then choose reply
    f.loader()
    print(f.overwriter_string(f.choose_random_value(replies)))

else:
    print("Pero hace una pregunta boludo")
