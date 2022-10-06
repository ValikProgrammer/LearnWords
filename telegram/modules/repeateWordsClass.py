import os
import sys
import random
from datetime import datetime
from prettytable import PrettyTable
from conf import * #bot , dp


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================

class myWord:
  
  def __init__(self):
    self.programmWord = ""
    self.programmTranslation = ""

  async def newPair(self,id):
      dict = globals()[f"dict{id}"]
      index = dict.arrIndex[dict.i]
      programmWord = (dict.keys[index])
      programmTranslation = (dict.dictionary[programmWord])
      dict.i +=1
      await bot.send_message(id,f"<i>{dict.i}</i>. <b>{programmWord}</b>")

      self.programmWord = programmWord
      self.programmTranslation = programmTranslation



  def compare (self,id,userTranslation):
    userTranslation = userTranslation.lower().strip()
    if type(self.programmTranslation) != list : 
      self.programmTranslation = [self.programmTranslation]

    for progTrans in self.programmTranslation:
      progTrans = progTrans.lower().strip()

      if progTrans == userTranslation: 
        return  {
              "userTrans": userTranslation,
              "correct":True,
              "msg": f"<b>[OK]</b> <i>{self.programmTranslation[0]}</i>" 
          }


    return  {
      "userTrans": userTranslation,
      "correct":False,
      "msg": f"<b>[ERROR]</b> <i>{self.programmTranslation[0]}</i>"
      }


class myDict:
    
  def __init__(self):
    self.dictName = ""
    self.dictionary = {}
    self.arrIndex = []
    self.keys = []
    self.i = 0
    self.arrDictionaries = next(os.walk(DICTIONARIES_PATH))[2]
    self.haveChosenDict = False


  def loadDict(self,dictName):
    dictionary = json.load(open(DICTIONARIES_PATH+"/"+dictName))
    keys = list(dictionary.keys()) # get keys from object
    arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
    arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...
    self.dictName = dictName
    self.dictionary = dictionary
    self.arrIndex = arrNumbersRandomSorted
    self.keys = keys
    self.i = 0
    self.haveChosenDict = True
    # self.arrDictionaries = next(os.walk(DICTIONARIES_PATH))[2]

  async def showAvaibleDictionaries(self,id):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    # _, _, arrDictionaries = next(os.walk(DICTIONARIES_PATH))
    # self.arrDictionaries = arrDictionaries
    for dictName in self.arrDictionaries:
      button =  types.InlineKeyboardButton(dictName[:-5],callback_data=dictName)
      keyboard_markup.add(button)

    await bot.send_message(id,"ChooseDictionary:", reply_markup=keyboard_markup)


class myStatistics:
  def userStatistics(self):
    logging.info("refreshing user statistics")
    dict = getDataFromJson(STATISTICS_USER_SCORE)
    if (dict.get(self.userName,"NO_USER") == "NO_USER"):
      dict[self.userName] = [self.score]
    else:
      dict[self.userName].append(self.score)
    writeDataToJson(STATISTICS_USER_SCORE,dict)

  def dictStatistics(self):
    logging.info("refreshing user statistics")
    dictName = self.dictName
    dict = getDataFromJson(STATISTICS_DICT)
    if (dict.get(dictName,"NO_DICT") == "NO_DICT"):
      dict[dictName] = 1
    else:
      dict[dictName] += 1;
    writeDataToJson(STATISTICS_DICT,dict)
  

  def __init__(self):
    self.mistakesArr = []
    self.startTime = 0
    self.correct = 0
    self.hasShownResult = 0
    self.score = 0
    self.dictName = ""
    self.userName = ""
    self.score = ""
    
  async def showResult(self,id,i):
    dict = globals()[f"dict{id}"]
    m = len(self.mistakesArr)
    SCORE = round(( (i-m)/i )*100)
    self.score = SCORE


    endTime  = datetime.now()
    duration = (endTime - self.startTime)
    
    result = f"ID:{id}\n<b><i>YOUR RESULTS:</i></b>\n<b>{datetime.now().strftime('%Y:%m:%d-%H:%M:%S')}</b> \nscore : <b>{SCORE}%</b>\nall:{i} \nmistakes:{m} \ncorrect:{i-m} \nduration : {str(duration)[:-7]}\ndictionary:{dict.dictName}"
    print(result,"\n")
    addDataToFile(RESULT_LOG_SCRIPT_PATH,result+"\n\n")
    
    moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_PATH[:-3]))
    console = "\n".join(moduleResultPrinting.getResult(SCORE))

    await bot.send_message(id,"YOUR MISTAKES :\n"+'\n'.join(self.mistakesArr))
    await bot.send_message(id,f"WORDS     MISTAKES   CORRECT\n      <b>{i:<8}           {m:<3}             {i-m:<3}</b>\nDuration: <b>{str(duration)[:-7]}</b>")
    await bot.send_message(id,f"<code>{console}</code>")
    


      





# ##======HANDLERS (FOR chosenDict and answers)==================

@dp.callback_query_handler(text=next(os.walk(DICTIONARIES_PATH))[2])
async def start(call:types.CallbackQuery):
    dict = globals()[f"dict{call.from_user.id}"]
    stat = globals()[f"stat{call.from_user.id}"]
    stat.dictName = call.data

    dict.loadDict(call.data)
    await bot.send_message(call.from_user.id,f"Your dict is <i>{call.data[:-6]}</i>")
    await bot.send_message(call.from_user.id,f"Amount of all words:<b>{len(dict.keys)}</b>")

    stat = globals()[f"stat{call.from_user.id}"]
    stat.startTime = datetime.now()
    stat.hasShownResult = 0

    word = globals()[f"word{call.from_user.id}"]
    await word.newPair(call.from_user.id)



@dp.message_handler()
async def checkPair(message:types.Message,state: FSMContext):

  stat = globals()[f"stat{message.from_user.id}"]
  word = globals()[f"word{message.from_user.id}"]
  dict = globals()[f"dict{message.from_user.id}"]
  if dict.haveChosenDict:
    if (stat.hasShownResult != 1):
      resp = word.compare(id,message.text)
      await bot.send_message(message.from_user.id,resp["msg"])
      if resp["correct"]:
        stat.correct += 1
      else:
        stat.mistakesArr.append(resp["userTrans"])

    if (dict.i != len(dict.keys)):
      await word.newPair(message.from_user.id)
    else:
      if (stat.hasShownResult != 1):
          stat.hasShownResult  = 1
          await message.reply("You have repeated all words ! ")
          await stat.showResult(message.from_user.id,dict.i)
          stat.userName = message.from_user.username
          stat.userStatistics()
          stat.dictStatistics()
          # await stat.user
          
      else:
        await message.reply("You have repeated all words. Start bot againg : /start")
        # executor.stop_poll()
        # from TelegBot import main
        # import importlib

        # # t = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
        # importlib.reload(TelegBot)
        # from TelegBot import main
  else:
    await message.reply("You should press the button :) If you want to get out - start the bot againg: /start")
    await dict.showAvaibleDictionaries(message.from_user.id)


async def main(id,username) :
  logging.info(f"{username} ({id}) зашел выучить английский!")
  path, dirs, files = next(os.walk(PATH))
  for i in range (0,len(dirs)):
      sys.path.insert(i, dirs[i])

  globals()[f"word{id}"] = myWord()
  globals()[f"dict{id}"] = myDict()
  globals()[f"stat{id}"] = myStatistics()

  dict = globals()[f"dict{id}"]
  await dict.showAvaibleDictionaries(id)

