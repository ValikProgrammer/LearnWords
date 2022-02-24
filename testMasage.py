import sys
import os


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()


PATH = "/home/valentin13/Desktop/Programming/Python/LearnWords"
print(PATH)
# add all folders to the system path
path, dirs, files = next(os.walk(PATH))
print(dirs)
for i in range (0,len(dirs)):
    # print(f"I added : {i} {dirs[i]}")
    sys.path.insert(i, dirs[i])


CONSTANTS_FILE_NAME = "CONSTANTS.py"
CONSTANTS = __import__(CONSTANTS_FILE_NAME[:-3])

# print(CONSTANTS.MASSAGES.TEST)

arr = [10,99,999]
i = 10

# s = CONSTANTS.MASSAGES.TEST[1:]

# CONSTANTS.PRINT_MASSAGE("TEST",[i])

# print(s)

print("====================")
CONSTANTS.PRINT_MASSAGE("0")
print("====================")
CONSTANTS.PRINT_MASSAGE("1",[i])
print("====================")
CONSTANTS.PRINT_MASSAGE("2",arr)
print("====================")

#     print(f"\t[{CONSTANTS.WARNING}{i}{CONSTANTS.END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"

# print(f"Amount of all words:{CONSTANTS.BLUE}{len(keys)}{CONSTANTS.END}") 



# s = f"\n Press the number[{i}]   {0}: "

# print(s.format(999))