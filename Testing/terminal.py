INCORRECT = '\033[31m' # red
CORRECT = '\033[32m' # green
WARNING = '\033[33m'#'\033[33m' # orange
BLUE = '\033[35m' # blue
UNDERLINED = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m' # simple text (stop colourful text)



import os
size = os.get_terminal_size()
print(size)

printResultScriptName = "test.py"
moduleResultPrinting = (__import__(printResultScriptName[:-3]))

SCORE = 100
#hi = ("✋")
# print("len c :",sys.getsizeof(hi) - sys.getsizeof(""))
# console = test(SIZE=8,SCORE="%",CHAR="#")


t1 = size.columns // len(str(SCORE))

console = moduleResultPrinting.test(SIZE=t1,SCORE=SCORE,CHAR=str(SCORE) )
for line in console:
    print(f"{BOLD}{CORRECT}{line}{END}")










"""
printResultScriptName = "printResult.py"
moduleResultPrinting = (__import__(printResultScriptName[:-3]))

# обычный размер будет равен sizeOFOneChar , а размер процента будет на 2 больше по высоте и на 2 больше по ширине
print(size)

SCORE = "100"

amountOfChars = len(SCORE)+1# we have "%"

width = size.columns

sizeOFOneChar = (width-2)//amountOfChars # -2 потому что процент

print(sizeOFOneChar)

resultArr = moduleResultPrinting.getResult(SCORE)

for i in resultArr:
  print(i)
"""
