import os
import sys
import random
from CONSTANTS import *


_, _, arrDictionaries = next(os.walk(DICTIONARIES_PATH))

arrOptions = [ # options for servey at the end of the dictionary
  "Continue working with this dictionary",
  "Choose another dictionary",
  "STOP and EXIT"
] 


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================
def newDictionary():
  global arrDictionaries
  print(f"{BLUE}Available Dictionaries : {END}")

  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{WARNING}{i}{END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"

  num = int(input(f"\nChoose the dictionary. Press the number[{WARNING}0{END}-{WARNING}{len(arrDictionaries)-1}{END}]: {WARNING}"))
  print(f"{END}")
 
  module = __import__(arrDictionaries[num][:-3])
  dictionary =  module.getDictionary()
  
  return dictionary

def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesAmount = 0
  print(f"Amount of all words:{BLUE}{len(keys)}{END}") 
  return [i , mistakesAmount , keys  , arrNumbersRandomSorted]

# ##======MAIN WORK==================
def charThatNotEquals (s1,s2) :
  arr = []

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
  if type(programmTranslation) != list : programmTranslation = [programmTranslation]
  
  userTranslation = userTranslation.lower()
  correctAnswer = f"{CORRECT}[OK]{END} : {CORRECT}{f'{END} or {CORRECT}'.join(programmTranslation)}{END}" # programmTranslation[0] - moct correct
  incorrectAnswer = f"{INCORRECT}[ERROR]{END} : {INCORRECT}{f'{END} or {INCORRECT}'.join(programmTranslation)}{END}"

  for progTrans in programmTranslation:
    progTrans = progTrans.lower()

    if progTrans == userTranslation: return correctAnswer

    arrUserTranslation = userTranslation.split(' ')
    arrProgrammTranslation = progTrans.split(' ')
    if (len(arrUserTranslation) == 3 ):
      if(arrUserTranslation[0] == arrProgrammTranslation[0]):
        # if 3 forms of the verb is the same
        if(arrProgrammTranslation[0] == arrProgrammTranslation[1] == arrProgrammTranslation[2]):  
            if(arrUserTranslation[1] == arrUserTranslation[2] == "="  or "."):
              return correctAnswer
        # if 1 from different and 2from == 3form 
        if (arrProgrammTranslation[1] == arrProgrammTranslation[2]):
          if(arrUserTranslation[1] == arrProgrammTranslation[1]):
            if(arrUserTranslation[2] == "=" or "."):
              return correctAnswer
        # if 3 forms all different
        if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[1]) == arrUserTranslation[1] or arrProgrammTranslation[1] == arrUserTranslation[1]):
          if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[2]) == arrUserTranslation[2] or arrProgrammTranslation[2] == arrUserTranslation[2]):
            return correctAnswer

  return incorrectAnswer

def showResult(i,m):
  moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_PATH[:-3]))
  SCORE = round(( (i-m)/i )*100)
  console = moduleResultPrinting.getResult(SCORE)
  for line in console:
      print(f"{BLUE}{line}{END}")
  print("WORDS     MISTAKES   CORRECT")
  print(f"  {BLUE}{i:<3}        {m:<3}       {i-m:<3}{END}")
  print("="*30)
  
# def getWordsAndTraslation():
#   pass



def main() :

  dictionary = newDictionary()
  while (dictionary == {}):
    print("This dictionary is empty.Choose anothe one!")
    dictionary = newDictionary()
  i , mistakesAmount , keys , arrIndex = newLoop(dictionary)

  while True :
  # servey
    if (i == len(keys)) :
      showResult(i,mistakesAmount)
      print("You have repeated all words in a dictionary !\n")
      
      for i in range(0,len(arrOptions)) :
        print(f"\t[{WARNING}{i}{END}] : {arrOptions[i]}")
      choose = int(input(f"Choose the option.Press the number[{WARNING}0{END}-{WARNING}{len(arrOptions)-1}{END}] : {WARNING}"))
      print(f"{END}")
      if (choose == 0):
        i , mistakesAmount , keys , arrIndex = newLoop(dictionary)
      elif(choose == 1):
        dictionary = newDictionary()
        while (dictionary == {}):
          print("This dictionary is empty.Choose anothe one!")
          dictionary = newDictionary()
        i , mistakesAmount , keys , arrIndex = newLoop(dictionary)
      else :
        break;
    # word and translation
    index = arrIndex[i]
    programmWord = (keys[index]).strip()
    programmTranslation = (dictionary[programmWord]).strip()

    userTranslation = str(input(f"\n{BLUE}{i+1}.{END}{programmWord.capitalize()} : ")).strip()

    if (userTranslation == "STOP"):
      if (i != 0 ): # if i == 0 we will have mistake in showResult() named "division by zero"
        showResult(i,mistakesAmount)
      break;

    res = compare(programmTranslation,userTranslation.lower())
    print(res)
    # костыль хаххахаххха
    if (res[6] == "E"):
      mistakesAmount+=1
    i+=1



"""
import os
import sys
import random
from CONSTANTS import *


_, _, arrDictionaries = next(os.walk(DICTIONARIES_PATH))

arrOptions = [ # options for servey at the end of the dictionary
  "Continue working with this dictionary",
  "Choose another dictionary",
  "STOP and EXIT"
] 


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================
def newDictionary():
  global arrDictionaries
  print(f"{BLUE}Available Dictionaries : {END}")

  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{WARNING}{i}{END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"

  num = int(input(f"\nChoose the dictionary. Press the number[{WARNING}0{END}-{WARNING}{len(arrDictionaries)-1}{END}]: {WARNING}"))
  print(f"{END}")
 
  module = __import__(arrDictionaries[num][:-3])
  dictionary =  module.getDictionary()
  
  return dictionary

def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesAmount = 0
  print(f"Amount of all words:{BLUE}{len(keys)}{END}") 
  return [i , mistakesAmount , keys  , arrNumbersRandomSorted]

# ##======MAIN WORK==================
def charThatNotEquals (s1,s2) :
  arr = []

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

def compare_test(s1,s2):
    arr = []
    for i in range (0 , min( len(s1),len(s2)  )):
        if  ( s1[i] != s2[i]):
            arr.append(i)
    return arr # array of indexes

def compare (programmTranslation,userTranslation):
  if type(programmTranslation) != list : programmTranslation = [programmTranslation]
  
  userTranslation = userTranslation.lower()
  correctAnswer = f"{CORRECT}[OK]{END} : {CORRECT}{f'{END} or {CORRECT}'.join(programmTranslation)}{END}" # programmTranslation[0] - moct correct
  incorrectAnswer = f"{INCORRECT}[ERROR]{END} : {INCORRECT}{f'{END} or {INCORRECT}'.join(programmTranslation)}{END}"

  for progTrans in programmTranslation:
    progTrans = progTrans.lower()

    if progTrans == userTranslation: return correctAnswer

    arrUserTranslation = userTranslation.split(' ')
    arrProgrammTranslation = progTrans.split(' ')
    if (len(arrUserTranslation) == 3 ):
      if(arrUserTranslation[0] == arrProgrammTranslation[0]):
        # if 3 forms of the verb is the same
        if(arrProgrammTranslation[0] == arrProgrammTranslation[1] == arrProgrammTranslation[2]):  
            if(arrUserTranslation[1] == arrUserTranslation[2] == "="  or "."):
              return correctAnswer
        # if 1 from different and 2from == 3form 
        if (arrProgrammTranslation[1] == arrProgrammTranslation[2]):
          if(arrUserTranslation[1] == arrProgrammTranslation[1]):
            if(arrUserTranslation[2] == "=" or "."):
              return correctAnswer
        # if 3 forms all different
        if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[1]) == arrUserTranslation[1] or arrProgrammTranslation[1] == arrUserTranslation[1]):
          if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[2]) == arrUserTranslation[2] or arrProgrammTranslation[2] == arrUserTranslation[2]):
            return correctAnswer

  arr_test = compare_test(programmTranslation,userTranslation)
  string_test = ""
  print(arr_test)

  for i in range (0,len(programmTranslation)):
    if i in arr_test:
        print("in arr",i)
        string_test +=INCORRECT + programmTranslation[i] +END
    else:
        string_test += programmTranslation[i]
  if string_test == "":
    string_test = programmTranslation
  print(string_test)    
  return string_test

def showResult(i,m):
  moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_PATH[:-3]))
  SCORE = round(( (i-m)/i )*100)
  console = moduleResultPrinting.getResult(SCORE)
  for line in console:
      print(f"{BLUE}{line}{END}")
  print("WORDS     MISTAKES   CORRECT")
  print(f"  {BLUE}{i:<3}        {m:<3}       {i-m:<3}{END}")
  print("="*30)
  
# def getWordsAndTraslation():
#   pass



def main() :

  dictionary = newDictionary()
  while (dictionary == {}):
    print("This dictionary is empty.Choose anothe one!")
    dictionary = newDictionary()
  i , mistakesAmount , keys , arrIndex = newLoop(dictionary)

  while True :
  # servey
    if (i == len(keys)) :
      showResult(i,mistakesAmount)
      print("You have repeated all words in a dictionary !\n")
      
      for i in range(0,len(arrOptions)) :
        print(f"\t[{WARNING}{i}{END}] : {arrOptions[i]}")
      choose = int(input(f"Choose the option.Press the number[{WARNING}0{END}-{WARNING}{len(arrOptions)-1}{END}] : {WARNING}"))
      print(f"{END}")
      if (choose == 0):
        i , mistakesAmount , keys , arrIndex = newLoop(dictionary)
      elif(choose == 1):
        dictionary = newDictionary()
        while (dictionary == {}):
          print("This dictionary is empty.Choose anothe one!")
          dictionary = newDictionary()
        i , mistakesAmount , keys , arrIndex = newLoop(dictionary)
      else :
        break;
    # word and translation
    index = arrIndex[i]
    programmWord = keys[index]
    programmTranslation = dictionary[programmWord]

    userTranslation = str(input(f"\n{BLUE}{i+1}.{END}{programmWord.capitalize()} : ")).strip()

    if (userTranslation == "STOP"):
      if (i != 0 ): # if i == 0 we will have mistake in showResult() named "division by zero"
        showResult(i,mistakesAmount)
      break;

    res = compare(programmTranslation,userTranslation.lower())
    print(res)
    # костыль хаххахаххха
    if (res[6] == "E"):
      mistakesAmount+=1
    i+=1
"""