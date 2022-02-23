import os
import sys

PRINT_RESULT_SCRIPT_PATH = "printResult.py"
WRITE_DATA_SCRIPT_PATH = "witeDataToDictionary.py"
REPEAT_WORDS_PATH = "repeateWords.py"
DICTIONARIES_PATH = "dictionaries"
COLORS_PATH = "sources/colors.py"

PATH = os.getcwd() # path to main.py

class colors:
  INCORRECT = '\033[31m' # red
  CORRECT = '\033[32m' # green
  WARNING = '\033[33m'#'\033[33m' # orange
  BLUE = '\033[35m' # blue
  UNDERLINED = '\033[4m'
  BOLD = '\033[1m'
  END = '\033[0m' # simple text (stop colourful text)
# print smth with color :print(f"{colors.INCORRECT}Error : Test message !{colors.END}") 

# CONSTANTS_ARR = [
#     PRINT_RESULT_SCRIPT_PATH,
#     WRITE_DATA_SCRIPT_PATH ,
#     DICTIONARIES_PATH ,
#     COLORS_PATH,
# ]


# # pathToFolderWithDictionaries, dirs, arrDictionaries = next(os.walk(path+"/"+folderWithDictionaries))
# for i in range (0,len(CONSTANTS_ARR)):
#     sys.path.insert(i, PATH+"/"+CONSTANTS_ARR[i])


# i = 999