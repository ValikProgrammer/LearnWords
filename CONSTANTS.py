import os
import sys
import time

PRINT_RESULT_SCRIPT_PATH = "printResult.py"
WRITE_DATA_SCRIPT_PATH = "witeDataToDictionary.py"
REPEAT_WORDS_PATH = "repeateWords.py"
DICTIONARIES_PATH = "dictionaries"

TEST = "HEllo world"

PATH = os.getcwd() # path to main.py

# class COLORS:
#   INCORRECT = '\033[31m' # red
#   CORRECT = '\033[32m' # green
#   WARNING = '\033[33m'#'\033[33m' # orange
#   BLUE = '\033[35m' # blue
#   UNDERLINED = '\033[4m'
#   BOLD = '\033[1m'
#   END = '\033[0m' # simple text (stop colourful text)
INCORRECT = '\033[31m' # red
CORRECT = '\033[32m' # green
WARNING = '\033[33m'#'\033[33m' # orange
BLUE = '\033[35m' # blue
UNDERLINED = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m' # simple text (stop colourful text)
# print smth with color :print(f"{colors.INCORRECT}Error : Test message !{colors.END}") 

# ARR_OPTIONS_MAIN = [
#   "======INSTRUCTUON======",
#   "YOU can :",

#   "[{WARNING}{i}{END}] : repeate dictionaries",
#   "[{WARNING}{i}{CONSTANTS.END}] : write data to them"
# ]
# print(f"======INSTRUCTUON=======\nYOU can :\n\t[{CONSTANTS.WARNING}0{CONSTANTS.END}] : repeate dictionaries\n\t[{CONSTANTS.WARNING}1{CONSTANTS.END}] : write data to them.\n========================")
# chose = int(input(f"Chose the option.Press the number [{CONSTANTS.WARNING}0{CONSTANTS.END}-{CONSTANTS.WARNING}1{CONSTANTS.END}] : "))

# CONSTANTS.PRINT_MASSAGE(NAME="MAIN_INSTRUCTION",DATA=CONSTANTS.ARR_OPTIONS_MAIN)
# chose = int(input(CONSTANTS.PRINT_MASSAGE(NAME="CHOSE",LENGTH=len(CONSTANTS.ARR_OPTIONS_MAIN))))









def getMassage(FILE="TEMPLATES",NAME="ERROR",DATA=[0],i=0,NUM=[0]):
  MASSAGES = {
    "TEMPLATES":{
        "CHOSE":[
          "Choose the option.Press the number[{WARNING}0{END}-{WARNING}{DATA[0]}{END}]: ",
        ],
        # "TEST" : f"\n Press the number[{WARNING}0{END}-{WARNING}{DATA}{END}]: ",
        # "ARRAY" : f"Press the number[{WARNING}0{END}-{WARNING}{DATA}{END}]: ",
        # "0":"some print",
        # "1":f"some indo {DATA}",
        "ARR_PRINTING":[
          "  {BLUE}{i} | {DATA}{END}",
        ],
        "DICTIONARIES_PRINTING":[
          "  [{WARNING}{i}{END}] : {BLUE}{str(DATA[i])}{END}",
        ],
        "ERROR":[
          "SOme error occured while printing DATA!",
        ],

    },
    "MAIN":{
        "INSTRUCTION_HEADER":[
              "======INSTRUCTUON======",
              "YOU can :"
          ],
          "INSTRUCTION_OPTIONS":[
              "\t[{WARNING}0{END}] : repeate dictionaries",
              "\t[{WARNING}1{END}] : write data to them",
          ],
    },
    "REPEATE":{
          "WORD":[
            "{BLUE}{NUM}.{END}{DATA}"
          ],
          "AMOUNT":[
            "Amount of all words:{BLUE}{DATA}{END}"
          ],
          "NEW_DICTIONARY_HEADER":[
            "Available Dictionaries :"
          ],
          "NEW_DICTIONARY_OPTIONS":[
            "Amount of all words:{BLUE}{DATA}{END}"
          ],
          "END_HEADER" :[
            "You have repeated all words in a dictionary !"
          ],
          "END_OPTIONS" :[
            "\tContinue working with this dictionary",
            "\tChoose another dictionary",
            "\tSTOP and EXIT"
          ],
          "END_CHOSE" : [
            "Chose he option.Press the number [{WARNING}0{END}-{WARNING}{DATA}{END}] : "
          ],
          "EMPTY_DICTIONARY" : [
            "This dictionary is empty.Choose anothe one!"
          ],
          "RESULT" : [
            "{BOLD}{BLUE}{DATA}{END}",
          ],
          "STATISTICS":[
            "WORDS     MISTAKES   CORRECT",
            "  {BLUE}{DATA:<3}        {DATA:<3}       {DATA:<3}{END}",
            '{"="*30}',
          ],
    },



    "smth": {
      "helo":[
        "world",
        "Valik",
        "MAMA",
      ],
      "my":"hobby"
    }
  
  }
  # print(f"==={i}++++{DATA}=======")
  return MASSAGES[FILE][NAME]

def PRINT(data):
  # print()
  # print(f"===={data}===")
  if (type(data) == str):
    # print("=========hello string=============")
    for char in data:
      # time.sleep(0.01)
      sys.stdout.write(char)
      sys.stdout.flush()
  elif (type(data) == list):
    # print("========hello list======")
    for string in data:
      PRINT(string)





def PRINT_MASSAGE(FILE,NAME,DATA=[0],NUM=0):
  # print(f"\nDATA:{DATA}")
  # DATA = [DATA]
  # print(f"DATA:{DATA}")
  # index = 0
  # print("DATA:",DATA,len(DATA))

    # TEST = f"Hi it is test massage{CORRECT}!he!"
  # if (type(DATA) == list):
  # if len(DATA) == 0: # it means that it is just single print(massage) without any variables
  #   # PRINT("len(DATA) == 0:")
  #   data = list(getMassage(FILE=FILE,NAME=NAME) )
  #   if len(data) > 0:
  #     for i in range(0,len(data)):
  #       PRINT(getMassage(FILE=FILE,NAME="ARR_PRINTING",DATA=data,i=i))
  #   else:
  #     for i in range(0,len(data)):
  #       PRINT(data[i])
  # elif len (DATA) == 1 : # it means it is just string with some variable
  #   # PRINT("(len (DATA) == 1):")
  #   data = [(getMassage(FILE=FILE,NAME=NAME,DATA=DATA))]
  #   for i in range(0,len(data)):
  #     PRINT(data[i])
  # else : #if len(DATA) > 1: #it means that is  an DATAay of some DATA
  #   while len(DATA)  != index:
  #     # print()
  #     PRINT(getMassage(FILE=FILE,NAME=NAME,DATA=DATA,i=index))
  #     index+=1

  # print("=============")
  output = []
  i = 0
  # print(f"\nFILE:{BLUE}{FILE}{END}\nNAME:{BLUE}{NAME}{END}\n")#DATA:{BLUE}{DATA}{END}
  test = (getMassage(FILE=FILE,NAME=NAME))
  for i in range(0 , len(DATA)):
    # print(f"===DATA[i]:{DATA[i]}")
    for j in range(0,len(test)):
      s = f"f'{test[j]}'"
      # print(s)
      output.append(eval(s))
  for el in output:
    print(el)
    # PRINT(output[i])
  # print(f"\n================{len(output)}") 

  # if len(output) == 1:
  #   # test = (getMassage(FILE=FILE,NAME=NAME,DATA=(DATA[i]),i=i,NUM=NUM))
  #   print(output[0])
  # else :
  #   for j in range(0,len(output)):
  #     # print(j)
  #     for el in output[j]:
  #       print(el)
  # for j in range(0,len(output)):
  # # print(j)
  #   for el in output[j]:
  #     print(el)
  # END = [
  #   "1",
  #   "2",
  #   "3"
  # ]
  # # END = *END
  # print(END)
  # print(type(END))
  return getMassage(FILE=FILE,NAME=NAME,DATA=DATA[i],i=i,NUM=NUM)
  # print(data)
  # print(type(data))
  # for index in range(0,len(data)):
  #   PRINT(getMassage(FILE=FILE,NAME=NAME,DATA=DATA,i=index))
  # return data

  # else : #if len(DATA) > 1: #it means that is  an DATAay of some DATA
  # while len(DATA)  != index:
  #   # print()
  #   PRINT(getMassage(FILE=FILE,NAME=NAME,DATA=DATA,i=index))
  #   index+=1

  
  # if (type(num) == int):
  #   data = list(getMassage(FILE=FILE,NAME=NAME,NUM=num))
  #   for i in range(0,len(data)):
  #     PRINT(data[i])
# CONSTANTS_ARR = [
#     PRINT_RESULT_SCRIPT_PATH,
#     WRITE_DATA_SCRIPT_PATH ,
#     DICTIONARIES_PATH ,
#     COLORS_PATH,
# ]


# # pathToFolderWithDictionaries, dirs, DATADictionaries = next(os.walk(path+"/"+folderWithDictionaries))
# for i in range (0,len(CONSTANTS_ARR)):
#     sys.path.insert(i, PATH+"/"+CONSTANTS_ARR[i])


# i = 999