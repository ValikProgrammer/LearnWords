from CONSTANTS import * 

# import os
# import sys

# PRINT_RESULT_SCRIPT_PATH = "printResult.py"
# WRITE_DATA_SCRIPT_PATH = "witeDataToDictionary.py"
# REPEAT_WORDS_PATH = "repeateWords.py"
# DICTIONARIES_PATH = "dictionaries"
# COLORS_PATH = "sources/colors.py"

# PATH = os.getcwd() # path to main.py



# class colors:
#   INCORRECT = '\033[31m' # red
#   CORRECT = '\033[32m' # green
#   WARNING = '\033[33m'#'\033[33m' # orange
#   BLUE = '\033[35m' # blue
#   UNDERLINED = '\033[4m'
#   BOLD = '\033[1m'
#   END = '\033[0m' # simple text (stop colourful text)
# # print smth with color :print(f"{colors.INCORRECT}Error : Test message !{colors.END}") 


# add all folders to the system path
path, dirs, files = next(os.walk(PATH))
for i in range (0,len(dirs)):
    # print(f"I added : {i}.{dirs[i]}")
    sys.path.insert(i, dirs[i])

print(f"======INSTRUCTUON=======\nYOU can :\n\t[{WARNING}0{END}] : repeate dictionaries\n\t[{WARNING}1{END}] : write data to them.\n========================")
chose = int(input(f"Chose the option.Press the number [{WARNING}0{END}-{WARNING}1{END}] : "))

if (chose == 0 ):
  repeatWords = __import__(REPEAT_WORDS_PATH[:-3])
  repeatWords.main()
elif (chose  == 1):
  writeResult = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
  writeResult.main()



# from Testing.test import *
# main()