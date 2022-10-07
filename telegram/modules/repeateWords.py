import os
import sys
import random
from datetime import datetime
from prettytable import PrettyTable
from conf import * #bot , dp

logging.info("find new arr dictionaris")
global arrDictionaries
_, _, arrDictionaries = next(os.walk(DICTIONARIES_PATH))


# #===========FUNCTIONS==================
# ##======STARTING SMTH==================


def newLoop (dictionary,id) :
  global i
  global mistakesArr
  mistakesArr = []
  keys = list(dictionary.keys()) # get keys from object
  arrNumbers = list(range(len(keys))) # 0 , 1, 2 ..   jsut get numbers from 0 to len(keys) 
  arrNumbersRandomSorted = random.sample(arrNumbers, len(arrNumbers)) # 0 , 2 , 1 ...

  i = 0
  return [i , keys  , arrNumbersRandomSorted]

# ##======MAIN WORK==================

async def showAvaibleDictionaries(id):
  keyboard_markup = types.InlineKeyboardMarkup(row_width=1)

  for dictName in arrDictionaries:
    button =  types.InlineKeyboardButton(dictName[:-4],callback_data=dictName)
    keyboard_markup.add(button)

  await bot.send_message(id,"ChooseDictionary:", reply_markup=keyboard_markup)



async def newPair(id):
    global i 
    global arrIndex

    if (i == 0 ) :
      # print("first time in new pair i ==0")
      global programmWord
      global programmTranslation

    index = arrIndex[i]
    programmWord = (keys[index])
    programmTranslation = (dictionary[programmWord])

    await bot.send_message(id,f"<i>{i}</i>. <b>{programmWord}</b>")
    i+=1;


def compare (programmTranslation,userTranslation):
  global mistakesArr
  userTranslation = userTranslation.lower().strip()

  if type(programmTranslation) != list : 
    programmTranslation = [programmTranslation]

  for progTrans in programmTranslation:
    progTrans = progTrans.lower().strip()

    if progTrans == userTranslation: 
      return f"<b>[OK]</b> <i>{programmTranslation[0]}</i>"
  mistakesArr.append(userTranslation)
  return f"<b>[ERROR]</b> <i>{programmTranslation[0]}</i>"


async def showResult(id,i,arr,startTime):
  m = len(arr)
  SCORE = round(( (i-m)/i )*100)

  endTime  = datetime.now()
  duration = (endTime - startTime)

  result = f"<b><i>YOUR RESULTS:</i></b>\n<b>{datetime.now().strftime('%Y:%m:%d-%H:%M:%S')}</b> \nscore : <b>{SCORE}%</b>\nall:{i} \nmistakes:{m}({mista}) \ncorrect:{i-m} \nduration : {str(duration)[:-7]}\n"
  await bot.send_message(id, result)
  print("\n",result,"\n")

  moduleResultPrinting = (__import__(PRINT_RESULT_SCRIPT_PATH[:-3]))
  console = "\n".join(moduleResultPrinting.getResult(SCORE))


  await bot.send_message(id,"YOUR MISTAKES :\n"+'\n'.join(mistakesArr))
  await bot.send_message(id,f"WORDS     MISTAKES   CORRECT\n        <b>{i:<8}           {m:<3}                {i-m:<3}</b>")
  await bot.send_message(id,f"<code>{console}</code>")


  addDataToFile("results.log",result+"\n")
    

 


# ##======HANDLERS (FOR chosenDict and answers)==================
@dp.callback_query_handler(text=arrDictionaries)
async def start(call:types.CallbackQuery):
    global arrIndex
    global keys
    global dictionary
    global startTime
    global i
    # global mistakesArr
    # mistakesArr = []

    dictionaryName = call.data
    dictionary     = json.load(open(DICTIONARIES_PATH+"/"+dictionaryName))
    i , keys , arrIndex  = newLoop(dictionary,id)

    await bot.send_message(call.from_user.id,f"Your dict is <i>{dictionaryName}</i>")
    await bot.send_message(call.from_user.id,f"Amount of all words:<b>{len(keys)}</b>")

    startTime = datetime.now()
    await newPair(call.from_user.id)

@dp.message_handler(commands=['cancel'])
async def checkPair(message:types.Message,state: FSMContext):

    current_state = await state.get_state()
    logging.info(f"in checl pair {current_state}")
    if current_state is None:
        return


@dp.message_handler()
async def checkPair(message:types.Message,state: FSMContext):
  
  global hasShownResult
  if (hasShownResult != 1):
    userTrans = message.text
    res = compare(programmTranslation,userTrans)
    await message.reply(res)
  if (i != len(keys)):
    await newPair(message.from_user.id)
  else:
    if (hasShownResult != 1):
        hasShownResult=1
        await message.reply("You have repeated all words ! ")
        print("mistakesArr (checkPair)",mistakesArr,len(mistakesArr),i,)
        await showResult(message.from_user.id,i,mistakesArr,startTime)
         
    else:
      await message.reply("You have repeated all words . Restart the bot,please")
      executor.stop_poll()
      # from TelegBot import main
      # import importlib

      # # t = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
      # importlib.reload(TelegBot)
      # from TelegBot import main







async def main(from_user_id) :

  path, dirs, files = next(os.walk(PATH))
  for i in range (0,len(dirs)):
      sys.path.insert(i, dirs[i])

  global hasShownResult
  hasShownResult = 0
  id = from_user_id
  await showAvaibleDictionaries(id)
