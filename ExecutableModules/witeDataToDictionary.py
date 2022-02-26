import os
import sys
from CONSTANTS import *
# actions for fluent working with dictionaries (because they are in folder)
pathToFolderWithDictionaries, dirs, arrDictionaries = next(os.walk(DICTIONARIES_PATH))

def chooseDictionary():
  global arrDictionaries
  print("\nAvailable Dictionaries : ")

  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{WARNING}{i}{END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"

  num = int(input(f"Choose the dictionary. Press the number[{WARNING}0{END}-{WARNING}{len(arrDictionaries)-1}{END}]: "))
  return arrDictionaries[num][:-3] # dictionary name without ".py"


def writeData(dict,data):
  global pathToFolderWithDictionaries
  fullPath = pathToFolderWithDictionaries+"/"+dict+".py"

  with open(fullPath, 'r', encoding='utf-8') as file: 
    lines = file.readlines()

  with open(fullPath, 'w', encoding='utf-8') as file:
    for i in range (0,len(lines)):
      if lines[i].strip() == "}" :
        lines[i] = " "*6 + f'"{data[0]}" : {data[1]}'+",\n" + " "*4 + "}"
      file.write(lines[i])


def getData() :
  question = input("\nQuestion : ").strip()
  if (question == "STOP"):
    return ["STOP"]
  elif (question == "OTHER"):
    return ["OTHER"]
  num = int(input("how many answers will you type [number]: "))
  answers = []
  for i in range (0,num):
    answers.append(input("Answer : ").strip())
  return [question,answers] # lower() не надо


print(f"======INSTRUCTUON=======\n[{WARNING}STOP{END}]  : stop programm\n[{WARNING}OTHER{END}] : choose another dictionary ")

def main ():
  dictName = chooseDictionary()

  addedWords = 0
  while True:
    data = getData()
    
    if data[0] == "STOP":
      break;
    elif data[0] == "OTHER":
      dictName = chooseDictionary()
    else :      
      writeData(dictName,data)
      addedWords += 1
  print(f"You have added {addedWords} words")
