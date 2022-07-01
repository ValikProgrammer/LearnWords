import os
from CONSTANTS import * 

# add all folders to the system path
path, dirs, files = next(os.walk(PATH))
for i in range (0,len(dirs)):
    # print(f"I added : {i}.{dirs[i]}")
    sys.path.insert(i, dirs[i])

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

# print(f"======INSTRUCTUON=======\nYOU can :\n\t[{WARNING}0{END}] : repeate dictionaries\n\t[{WARNING}1{END}] : write data to them.\n========================")
# chose = int(input(f"Chose the option.Press the number [{WARNING}0{END}-{WARNING}1{END}] : {WARNING}"))
# print(f"{END}")
chose = 0
if (chose == 0 ):
  repeatWords = __import__(REPEAT_WORDS_PATH[:-3])
  repeatWords.main()
elif (chose  == 1):
  writeResult = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
  writeResult.main()

