import os
import sys

# actions for fluent working with dictionaries (because they are in folder)
folderWithDictionaries = "dictionaries"
path = os.getcwd()
pathToFolderWithDictionaries, dirs, arrDictionaries = next(os.walk(path+"/"+folderWithDictionaries))
sys.path.insert(0, pathToFolderWithDictionaries)


class colors:
  INCORRECT = '\033[31m' # red
  CORRECT = '\033[32m' # green
  WARNING = '\033[33m'#'\033[33m' # orange
  BLUE = '\033[35m' # blue
  UNDERLINED = '\033[4m'
  BOLD = '\033[1m'
  END = '\033[0m' # simple text (stop colourful text)
  


def chooseDictionary(arrDictionaries=arrDictionaries):
  print("\nAvailable Dictionaries : ")
  for i in range(0,len(arrDictionaries)) :
    print(f"\t[{colors.WARNING}{i}{colors.END}] : {arrDictionaries[i][:-3]}") # [:-3] - we need to delete ".py"
  num = int(input(f"Choose the dictionary. Press the number[{colors.WARNING}0{colors.END}-{colors.WARNING}{len(arrDictionaries)-1}{colors.END}]: "))

  return arrDictionaries[num][:-3] # dictionary name without ".py"


def writeData(dict,data,pathToFolderWithDictionaries=pathToFolderWithDictionaries):
  fullPath = pathToFolderWithDictionaries+"/"+dict+".py"

  with open(fullPath, 'r', encoding='utf-8') as file: 
    lines = file.readlines()

  with open(fullPath, 'w', encoding='utf-8') as file:
    for i in range (0,len(lines)):
      if lines[i].strip() == "}" :
        # lines[i] = f' "{data[0]}" : "{data[1]}" \n'
        lines[i] = " "*6 + f'"{data[0]}" : "{data[1]}"'+",\n" + " "*4 + "}"
      file.write(lines[i])


def getData() :
  question = input("Question : ")
  if (question == "STOP"):
    return ["STOP"]
  elif (question == "OTHER"):
    return ["OTHER"]
  answer = input("Answer : ")
  return [question,answer] # lower() не надо

print("======INSTRUCTUON=======\n[STOP] : stop programm\n[OTHER] : choose another dictionary ")

def main ():
  dictName = chooseDictionary()

  while True:
    data = getData()
    
    if data[0] == "STOP":
      break;
    elif data[0] == "OTHER":
      dictName = chooseDictionary()
    else :      
      writeData(dictName,data)
