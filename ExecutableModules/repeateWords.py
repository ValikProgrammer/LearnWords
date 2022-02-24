import os
import sys
import random

CONSTANTS_FILE_NAME = "CONSTANTS.py"
CONSTANTS = __import__(CONSTANTS_FILE_NAME[:-3])

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

blaBla, dirs, arrDictionaries = next(os.walk(CONSTANTS.PATH+"/"+CONSTANTS.DICTIONARIES_PATH))
# sys.path.insert(0, pathToCONSTANTS.DICTIONARIES_PATH)

arrOptions = [ # options for servey at the end of the dictionary
  "Continue working with this dictionary",
  "Choose another dictionary",
  "STOP and EXIT"
] 


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================
def newDictionary(arrDictionaries=arrDictionaries):
  print("\nAvailable Dictionaries : ")
  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{CONSTANTS.WARNING}{i}{CONSTANTS.END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"
  num = int(input(f"\nChoose the dictionary. Press the number[{CONSTANTS.WARNING}0{CONSTANTS.END}-{CONSTANTS.WARNING}{len(arrDictionaries)-1}{CONSTANTS.END}]: "))
 
  module = __import__(arrDictionaries[num][:-3])
  dictionary =  module.getDictionary()
  
  return dictionary

def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesBLUE = 0
  print(f"Amount of all words:{CONSTANTS.BLUE}{len(keys)}{CONSTANTS.END}") 
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
  if programmTranslation == userTranslation: return f"{CONSTANTS.CORRECT}[OK]{CONSTANTS.END} : {CONSTANTS.WARNING}{programmTranslation}{CONSTANTS.END}"

  arrUserTranslation = userTranslation.split(' ')
  arrProgrammTranslation = programmTranslation.split(' ')
  if (len(arrUserTranslation) == 3 ):
    if(arrUserTranslation[0] == arrProgrammTranslation[0]):
      # if 3 forms of the verb is the same
      if(arrProgrammTranslation[0] == arrProgrammTranslation[1] == arrProgrammTranslation[2]):  
          if(arrUserTranslation[1] == arrUserTranslation[2] == "="  or "."):
            return f"{CONSTANTS.CORRECT}[OK]{CONSTANTS.END} : {CONSTANTS.WARNING}{programmTranslation}{CONSTANTS.END}"
      # if 1 from different and 2from == 3form 
      if (arrProgrammTranslation[1] == arrProgrammTranslation[2]):
        if(arrUserTranslation[1] == arrProgrammTranslation[1]):
          if(arrUserTranslation[2] == "=" or "."):
            return f"{CONSTANTS.CORRECT}[OK]{CONSTANTS.END} : {CONSTANTS.WARNING}{programmTranslation}{CONSTANTS.END}"
      # if 3 forms all different
      if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[1]) == arrUserTranslation[1] or arrProgrammTranslation[1] == arrUserTranslation[1]):
        if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[2]) == arrUserTranslation[2] or arrProgrammTranslation[2] == arrUserTranslation[2]):
          return f"{CONSTANTS.CORRECT}[OK]{CONSTANTS.END} : {CONSTANTS.WARNING}{programmTranslation}{CONSTANTS.END}"
  #return f"{CONSTANTS.INCORRECT}[ERROR]{CONSTANTS.END} : {CONSTANTS.WARNING}{programmTranslation}{CONSTANTS.END}"
  return f"{CONSTANTS.INCORRECT}[ERROR]{CONSTANTS.END} : {CONSTANTS.INCORRECT}{programmTranslation}{CONSTANTS.END}"

def showResult(i,m):
  # print(f"========RESULT={CONSTANTS.BLUE}{round(( (i-m)/i )*100)}{CONSTANTS.END}%========")
  
  moduleResultPrinting = (__import__(CONSTANTS.PRINT_RESULT_SCRIPT_PATH[:-3]))
  SCORE = round(( (i-m)/i )*100)
  resultArr = moduleResultPrinting.getResult(SCORE)
  massageScore = "Score: "
  lenOfRavno = len(resultArr[0])+len(massageScore)
  middle = len(resultArr)//2


  print("="*lenOfRavno)

  for j in range (0,len(resultArr)):
    copy_line = resultArr[j]
    if(j == middle):
      resultArr[middle] = massageScore + copy_line 
    else :
      # print(f"te{' '*len(massageScore)}te")
      resultArr[j] = str(" "*(len(massageScore)) ) + copy_line
    print(f"{CONSTANTS.BOLD}{CONSTANTS.BLUE}{resultArr[j]}")

  print(f"{CONSTANTS.END}{'='*lenOfRavno}")
  print("WORDS     MISTAKES   CORRECT")
  print(f"  {CONSTANTS.BLUE}{i:<3}        {m:<3}       {i-m:<3}{CONSTANTS.END}")
  print("="*lenOfRavno)
  
# def getWordsAndTraslation():
#   pass



def main() :

  dictionary = newDictionary()
  while (dictionary == {}):
    print("This dictionary is empty.Choose anothe one!")
    dictionary = newDictionary()
  i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)

  while True :

  # servey
    if (i == len(keys)) :
      showResult(i,mistakesBLUE)
      print("You have repeated all words in a dictionary !\n")
      for i in range(0,len(arrOptions)) :
        print(f"\t[{CONSTANTS.WARNING}{i}{CONSTANTS.END}] : {arrOptions[i]}")
      choose = int(input(f"\nChoose the option.Press the number[{CONSTANTS.WARNING}0{CONSTANTS.END}-{CONSTANTS.WARNING}{len(arrOptions)-1}{CONSTANTS.END}] : "))
      if (choose == 0):
        i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)
      elif(choose == 1):
        dictionary = newDictionary(arrDictionaries)
        while (dictionary == {}):
          print("This dictionary is empty.Choose anothe one!")
          dictionary = newDictionary()
        i , mistakesBLUE , keys , arrIndex = newLoop(dictionary)
      else :
        break;
    # word and translation
    index = arrIndex[i]
    programmWord = keys[index]
    programmTranslation = dictionary[programmWord]

    print(f"\n{CONSTANTS.BLUE}{i+1}.{CONSTANTS.END}{programmWord}") 
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
