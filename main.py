#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================
# =======ADD NEW WORDS=======
# ===========================
# 
# =======INSTUCTION==========
# + get document with irrugular worbs in whitch you must have
# this strucure : V1 V2 V3 translation
# + than you shold to copy this document , run this programm ,
# input your coppied document
# + than in console you will see ready object
# + copy and paste it into your programm
# 
# =======CODE===============
# // let obj = {}
# 
# // let arr = prompt("arr:");
# // let res = arr.replace(/ /g, "").split('\n')
# 
# // for(let i = 0 ; i < res.length; i+=4) {
# //   obj[ res[i+3] ] = `${res[i]} ${res[i+1]} ${res[i+2]}`
# // }
# // console.log("+++++++++++++++++++++++++")
# // console.log(obj)
# 



# ===========================
# =======APP LEARN WORDS=====
# ===========================
# =======UNSTRUCTION=========
# - this programm was made to help you learn irregular verbs
# YOU CAN ENTER DATA DIFFERENT:
# + if 3 froms of the verb is the same you can enter  "V1 = =" or "V1 V2 ="
# + if 2 and 3 from of the verb is the same you can enter  "V1 V2 ="
# + if 3 froms of the verb is different you can enter "V1 V2 V3" but
# if this forms is different by some letters you can enter "V1 letter letter"
# for example (stink stank stunk - вонять ) stink a u
# for example (dream dreamt dreamt ) dream t t
# for example (sew sewed sewn) sew sewed n
# MY PRIDE: (sew sewed sewn) sew ed n (maiun logic in compare and comment:3 froms different)


#=======SOURCES===========
# colourful text - https://habr.com/ru/post/119436/
# another wariant to get colored text
# from termcolor import colored
# print(colored('hello', 'red'), colored('world', 'green'))

# #===VARIABLES & PREPARATORY ACTIONS===
import random
import os
import sys

PRINT_RESULT_SCRIPT_NAME = "printResult.py"
WRITE_DATA_SCRIPT_NAME = "witeDataToDictionary.py"

# actions for fluent working with dictionaries (because they are in folder)
folderWithDictionaries = "dictionaries"
path = os.getcwd()
pathToFolderWithDictionaries, dirs, arrDictionaries = next(os.walk(path+"/"+folderWithDictionaries))
sys.path.insert(0, pathToFolderWithDictionaries)

arrOptions = [ # options for servey at the end of the dictionary
  "Continue working with this dictionary",
  "Choose another dictionary",
  "STOP and EXIT"
] 

class colors:
  INCORRECT = '\033[31m' # red
  CORRECT = '\033[32m' # green
  WARNING = '\033[33m'#'\033[33m' # orange
  BLUE = '\033[35m' # blue
  UNDERLINED = '\033[4m'
  BOLD = '\033[1m'
  END = '\033[0m' # simple text (stop colourful text)
# print smth with color :print(f"{colors.INCORRECT}Error : Test message !{colors.END}") 

# #===========FUNCTIONS==================
# ##======STARTING SMTH==================
def newDictionary(arrDictionaries=arrDictionaries):
  print("\nAvailable Dictionaries : ")
  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{colors.WARNING}{i}{colors.END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"
  num = int(input(f"\nChoose the dictionary. Press the number[{colors.WARNING}0{colors.END}-{colors.WARNING}{len(arrDictionaries)-1}{colors.END}]: "))
 
  module = __import__(arrDictionaries[num][:-3])
  dictionary =  module.getDictionary()
  
  return dictionary

def newLoop (dictionary) :
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
  i = mistakesBLUE = 0
  print(f"Amount of all words:{colors.BLUE}{len(keys)}{colors.END}") 
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
  if programmTranslation == userTranslation: return f"{colors.CORRECT}[OK]{colors.END} : {colors.WARNING}{programmTranslation}{colors.END}"

  arrUserTranslation = userTranslation.split(' ')
  arrProgrammTranslation = programmTranslation.split(' ')
  if (len(arrUserTranslation) == 3 ):
    if(arrUserTranslation[0] == arrProgrammTranslation[0]):
      # if 3 forms of the verb is the same
      if(arrProgrammTranslation[0] == arrProgrammTranslation[1] == arrProgrammTranslation[2]):  
          if(arrUserTranslation[1] == arrUserTranslation[2] == "="  or "."):
            return f"{colors.CORRECT}[OK]{colors.END} : {colors.WARNING}{programmTranslation}{colors.END}"
      # if 1 from different and 2from == 3form 
      if (arrProgrammTranslation[1] == arrProgrammTranslation[2]):
        if(arrUserTranslation[1] == arrProgrammTranslation[1]):
          if(arrUserTranslation[2] == "=" or "."):
            return f"{colors.CORRECT}[OK]{colors.END} : {colors.WARNING}{programmTranslation}{colors.END}"
      # if 3 forms all different
      if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[1]) == arrUserTranslation[1] or arrProgrammTranslation[1] == arrUserTranslation[1]):
        if (charThatNotEquals(arrProgrammTranslation[0],arrProgrammTranslation[2]) == arrUserTranslation[2] or arrProgrammTranslation[2] == arrUserTranslation[2]):
          return f"{colors.CORRECT}[OK]{colors.END} : {colors.WARNING}{programmTranslation}{colors.END}"
  #return f"{colors.INCORRECT}[ERROR]{colors.END} : {colors.WARNING}{programmTranslation}{colors.END}"
  return f"{colors.INCORRECT}[ERROR]{colors.END} : {colors.INCORRECT}{programmTranslation}{colors.END}"

def showResult(i,m):
  # print(f"========RESULT={colors.BLUE}{round(( (i-m)/i )*100)}{colors.END}%========")
  
  moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_NAME[:-3]))
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
    print(f"{colors.BOLD}{colors.BLUE}{resultArr[j]}")

  print(f"{colors.END}{'='*lenOfRavno}")
  print("WORDS     MISTAKES   CORRECT")
  print(f"  {colors.BLUE}{i:<3}        {m:<3}       {i-m:<3}{colors.END}")
  print("="*lenOfRavno)
  
# def getWordsAndTraslation():
#   pass





print(f"======INSTRUCTUON=======\nYOU can :\n\t[{colors.WARNING}0{colors.END}] : repeate dictionaries\n\t[{colors.WARNING}1{colors.END}] : write data to them.\n========================")
chose = int(input(f"Chose the option.Press the number [{colors.WARNING}0{colors.END}-{colors.WARNING}1{colors.END}] : "))
if (chose == 0 ):
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
        print(f"\t[{colors.WARNING}{i}{colors.END}] : {arrOptions[i]}")
      choose = int(input(f"\nChoose the option.Press the number[{colors.WARNING}0{colors.END}-{colors.WARNING}{len(arrOptions)-1}{colors.END}] : "))
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

    print(f"\n{colors.BLUE}{i}.{colors.END}{programmWord}") 
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


elif (chose  == 1):
  writeResult = __import__(WRITE_DATA_SCRIPT_NAME[:-3])
  writeResult.main()