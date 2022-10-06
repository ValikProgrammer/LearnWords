import os
import sys

PATH = os.getcwd() # path to main.py

PRINT_RESULT_SCRIPT_PATH = "printResult.py"
WRITE_DATA_SCRIPT_PATH = "witeDataToDictionary.py"
REPEAT_WORDS_PATH = "repeateWords.py"
DICTIONARIES_PATH = PATH+"/"+"dictionaries"



INCORRECT = '\033[31m' # red
CORRECT = '\033[32m' # green
WARNING = '\033[33m'#'\033[33m' # orange
BLUE = '\033[35m' # blue
UNDERLINED = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m' # simple text (stop colourful text)
