import re
def welcome():
    print("""
**************************************
**    Welcome to MadLibs!   **
**    If needed, please read the rules belows.    **
**
** To quit at any time, type "quit" **
**************************************
        """)

def displayMenuForUser():
    print(""" 
GAME RULES GO HERE!!!
Hello there! The rules are simple for MadLib. We ask you for certain type of word and you will provide us answer for each word. Once all words have been filled, we read back your funny story!
          """)

def submitPrompt():
    print("""
************************************
** Please fill out required words **
** To submit answer, press Enter. **
************************************
        """)

def read_template(file_path):
  try:
    with open(file_path, 'r') as f:
      stripped = f.read().strip()
      return stripped
  except FileNotFoundError:
    raise FileNotFoundError('File cannot be found, sorry.')
  except Exception as e:
    return "Here's what wrong: " + e  
read_template("assets/dark_and_stormy_night_template.txt")
# read_template("assets/make_me_a_video_game_output.txt")

def parse_template(file_content):

  expected_stripped = file_content.format(Adjective = {}, Noun = {})
  expected_parts_list = re.findall(r'{([^}]*)}', file_content)
  expected_parts = tuple(expected_parts_list)
  return expected_stripped, expected_parts


def merge():
  return('setup')


