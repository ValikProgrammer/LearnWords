import os
import sys
import time
from CONSTANTS import *
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

PATH = os.getcwd() # path to main.py

# add all folders to the system path
path, dirs, files = next(os.walk(PATH))
for i in range (0,len(dirs)):
    # print(f"I added : {i}.{dirs[i]}")
    sys.path.insert(i, dirs[i])

# CONSTANTS_FILE_NAME = "CONSTANTS.py"
# CONSTANTS = __import__(CONSTANTS_FILE_NAME[:-3])

PRINT_MASSAGE(FILE="MAIN",NAME="INSTRUCTION_HEADER")
# PRINT_MASSAGE(FILE="MAIN",NAME="INSTRUCTION_OPTIONS")
# print("===============")
arrLen = len(PRINT_MASSAGE(FILE="MAIN",NAME="INSTRUCTION_OPTIONS"))-1
  # for i in range(0,len(arrDictionaries)) :
# DATA=[len(test)]
# print(f"=======hi!{len(test)}!ih========")
# print(f"======={test}=***===")
PRINT_MASSAGE(FILE="TEMPLATES",NAME="CHOSE",DATA=[arrLen])
chose = int(input(" "))

if (chose == 0 ):
  repeatWords = __import__(REPEAT_WORDS_PATH[:-3])
  repeatWords.main()
elif (chose  == 1):
  writeResult = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
  writeResult.main()

"""
  
  import os
import sys
import time

from CONSTANTS import *
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

PATH = os.getcwd() # path to main.py

# add all folders to the system path
path, dirs, files = next(os.walk(PATH))
for i in range (0,len(dirs)):
    print(f"I added : {i}.{dirs[i]}")
    sys.path.insert(i, dirs[i])

CONSTANTS_FILE_NAME = "CONSTANTS.py"
CONSTANTS = __import__(CONSTANTS_FILE_NAME[:-3])

CONSTANTS.PRINT_MASSAGE(NAME="MAIN_INSTRUCTION_HEADER")
CONSTANTS.PRINT_MASSAGE(NAME="MAIN_INSTRUCTION_OPTIONS")
CONSTANTS.PRINT_MASSAGE(NAME="MAIN_CHOSE")

chose = int(input(" "))

if (chose == 0 ):
  repeatWords = __import__(CONSTANTS.REPEAT_WORDS_PATH[:-3])
  repeatWords.main()
elif (chose  == 1):
  writeResult = __import__(CONSTANTS.WRITE_DATA_SCRIPT_PATH[:-3])
  writeResult.main()
  """