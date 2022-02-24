import os
import sys
import random

from CONSTANTS import *
# CONSTANTS_FILE_NAME = "CONSTANTS.py"
# CONSTANTS = __import__(CONSTANTS_FILE_NAME[:-3])



# class CONSTANTS.CONSTANTS.CONSTANTS.colors:
#   INCORRECT = '\033[31m' # red
#   CORRECT = '\033[32m' # green
#   WARNING = '\033[33m'#'\033[33m' # orange
#   BLUE = '\033[35m' # blue
#   UNDERLINED = '\033[4m'
#   BOLD = '\033[1m'
#   END = '\033[0m' # simple text (stop colourful text)

# actions for fluent working with dictionaries (because they are in folder)
# CONSTANTS.DICTIONARIES_PATH = "dictionaries"
# path = os.getcwd()

blaBla, dirs, arrDictionaries = next(os.walk(PATH+"/"+DICTIONARIES_PATH))
# sys.path.insert(0, pathToCONSTANTS.DICTIONARIES_PATH)

arrOptions = [ # options for servey at the end of the dictionary

] 


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================
def newDictionary(arrDictionaries=arrDictionaries):
  PRINT_MASSAGE(FILE="REPEATE",NAME="NEW_DICTIONARY_HEADER")
  PRINT_MASSAGE(FILE="TEMPLATES",NAME="DICTIONARIES_PRINTING",DATA=arrDictionaries)
  arrLen = len(arrDictionaries) -1
  # print(f"\n\n{INCORRECT}need = len(arrDictionaries) -1 {need}")
  PRINT_MASSAGE(FILE="TEMPLATES",NAME="CHOSE",DATA=[arrLen])
  # for i in range(0,len(arrDictionaries)) :
  #   print(f"\t[{WARNING}{i}{END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"
  

  # num = int(input(f"\nChoose the dictionary. Press the number[{WARNING}0{END}-{WARNING}{len(arrDictionaries)-1}{END}]: "))
  num = int(input())
  module = __import__(arrDictionaries[num][:-3])
  dictionary =  module.getDictionary()
  


  return dictionary

def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesBLUE = 0
  # print(f"Amount of all words:{BLUE}{len(keys)}{END}") 
  arrLen = len(keys) -1
  # print(f"\n\n{INCORRECT}need = len(keys) -1 {need}")
  PRINT_MASSAGE(FILE="REPEATE",NAME="AMOUNT",DATA=[arrLen])
  return [i , mistakesBLUE , keys  , arrNumbersRandomSorted]
# ##======MAIN WORK==================
def charThatNotEquals (s1,s2) :
  arr = []
  # for i in range(0,len(s1)):
  #   if(s1[i] != s2[i]):
  #     arr.append(s2[i])
  # return arr[0]
  if (len(s2) > len(s1)):
    # return s2[-1]
    need = len(s2) - len(s1)
    #    print(len(s2),len(s1),need)
    for i in range (len(s2)-need,len(s2)):
        arr.append(s2[i])
    #   print("s2>",s1,s1,''.join(arr)  )
    return ''.join(arr)    
  for i in range(0,min(len(s2),len(s1)) ):
    if(s1[i] != s2[i]):
      arr.append(s2[i])
  #print(s1,s1,''.join(arr)  )
  return ''.join(arr) 

def compare (programmTranslation,userTranslation):
  if programmTranslation == userTranslation: return f"{CORRECT}[OK]{END} : {WARNING}{programmTranslation}{END}"

  arrUserTranslation = userTranslation.split(' ')
  arrProgrammTranslation = programmTranslation.split(' ')
  if (len(arrUserTranslation) == 3 ):
    if(arrUserTranslation[0] == arrProgrammTranslation[0]):
      # if 3 forms of the verb is the same
      if(arrProgrammTranslation[0] == arrProgrammTranslation[1] == arrProgrammTranslation[2]):  
          if(arrUserTranslation[1] == arrUserTranslation[2] == "="  or "."):
            return f"{CORRECT}[OK]{END} : {WARNING}{programmTranslation}{END}"
      # if 1 from different and 2from == 3form 
      if (arrProgrammTranslation[1] == arrProgrammTranslation[2]):
        if(arrUserTranslation[1] == arrProgrammTranslation[1]):
          if(arrUserTranslation[2] == "=" or "."):
            return f"{CORRECT}[OK]{END} : {WARNING}{programmTranslation}{END}"
      # if 3 forms all different
      if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[1]) == arrUserTranslation[1] or arrProgrammTranslation[1] == arrUserTranslation[1]):
        if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[2]) == arrUserTranslation[2] or arrProgrammTranslation[2] == arrUserTranslation[2]):
          return f"{CORRECT}[OK]{END} : {WARNING}{programmTranslation}{END}"
  #return f"{INCORRECT}[ERROR]{END} : {WARNING}{programmTranslation}{END}"
  return f"{INCORRECT}[ERROR]{END} : {INCORRECT}{programmTranslation}{END}"

def showResult(i,m):
  # print(f"========RESULT={CONSTANTS.BLUE}{round(( (i-m)/i )*100)}{END}%========")
  score = round(( (i-m)/i )*100)

  moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_PATH[:-3]))
  console = moduleResultPrinting.getResult(score)
  # massageScore = "Score: "
  # lenOfRavno = len(resultArr[0])+len(massageScore)
  # middle = len(resultArr)//2


  

  # for j in range (0,len(resultArr)):
  #   copy_line = resultArr[j]
  #   if(j == middle):
  #     resultArr[middle] = massageScore + copy_line 
  #   else :
  #     # print(f"te{' '*len(massageScore)}te")
  #     resultArr[j] = str(" "*(len(massageScore)) ) + copy_line
  #   print(f"{CONSTANTS.BOLD}{CONSTANTS.BLUE}{resultArr[j]}")
  PRINT_MASSAGE(FILE="REPEATE",NAME="RESULT",DATA=console)
  # PRINT_MASSAGE(FILE="REPEATE",NAME="STATISTICS",DATA=[i],NUM=[m])

  # print(f"{END}{'='*lenOfRavno}")
  print("WORDS     MISTAKES   CORRECT")
  print(f"  {BLUE}{i:<3}        {m:<3}       {i-m:<3}{END}")
  print("="*30)
  
# def getWordsAndTraslation():
#   pass



def main() :

  dictionary = newDictionary()
  while (dictionary == {}):
    # print("This dictionary is empty.Choose anothe one!")
    PRINT_MASSAGE(FILE="REPEATE",NAME="EMPTY_DICTIONARY")
    dictionary = newDictionary()
  i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)

  while True :

  # servey
    if (i == len(keys)) :
      showResult(i,mistakesBLUE)
      PRINT_MASSAGE(FILE="REPEATE",NAME="END_HEADER")
      options = PRINT_MASSAGE(FILE="REPEATE",NAME="END_OPTIONS")
      PRINT_MASSAGE(FILE="REPEATE",NAME="END_CHOSE",DATA=[(len(options))])
      

      choose = int(input(" "))

      if (choose == 0):
        i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)
      elif(choose == 1):
        dictionary = newDictionary(arrDictionaries)
        while (dictionary == {}):
          PRINT_MASSAGE(FILE="REPEATE",NAME="EMPTY_DICTIONARY")
          dictionary = newDictionary()
        i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)
      else :
        break;
    # word and translation
    index = arrIndex[i]
    programmWord = keys[index]
    programmTranslation = dictionary[programmWord]

    PRINT_MASSAGE(FILE="REPEATE",NAME="WORD",DATA=[programmWord],NUM=i+1)
    userTranslation = str(input()).strip()

    if (userTranslation == "STOP"):
      showResult(i,mistakesBLUE)
      break;

    res = compare(programmTranslation,userTranslation.lower())
    print(res)
        # костыль хаххахаххха
    if (res[6] == "E"):
      mistakesBLUE+=1
    i+=1
