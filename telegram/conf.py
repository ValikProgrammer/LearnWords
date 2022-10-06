import coloredlogs
coloredlogs.install()#(format="%(asctime)s %(levelname)-8s  %(message)s (%(filename)s %(funcName)s :%(lineno)s)")

import logging
import logging.config
import json


import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor





# logging.config.fileConfig('logging.conf')
# logging.basicConfig(format="%(asctime)s %(levelname)-8s  %(message)s (%(filename)s %(funcName)s :%(lineno)s)",level=logging.INFO)

API_TOKEN = '5752216179:AAHPlpXp5RHexs8L-rvTcDHWD8p-TPcvwVI'


bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def sendInfMain(from_user_id,text: str):
    await bot.send_message(from_user_id, text) 

def writeDataToFile(file,text):
    with open(file, "w") as file:
        file.write(text)
def addDataToFile(file,text):
    with open(file, "a") as file:
        file.write(text)
def getDataFromFile(file):
    with open(file, "r") as file:
        text = file.read()
    return text


def writeDataToJson(file,dict):
    with open(file, "w") as file:
        file.write(json.dumps(dict,indent=4,ensure_ascii=False))
def getDataFromJson(file):
    with open(file, "r") as file:
        text = file.read()
    return json.loads(text)






import os
import sys

PATH = os.getcwd() # path to main.py
PRINT_RESULT_SCRIPT_PATH = "printResult.py"
WRITE_DATA_SCRIPT_PATH = "writeDictionary.py"
REPEAT_WORDS_PATH = "repeateWordsClass.py"
DICTIONARIES_PATH = PATH+"/"+"dictionaries"
CLEAN_TEXT_ALGORITHM = "cleanTextAlgorithm.py"
RESULT_LOG_SCRIPT_PATH = "statistics/results.log"
STATISTICS_DICT = "statistics/dict.json"
STATISTICS_USER_SCORE = "statistics/user_score.json"
SHOW_STATISTICS = "showStatistics.py"

INCORRECT = '\033[31m' # red
CORRECT = '\033[32m' # green
WARNING = '\033[33m'#'\033[33m' # orange
BLUE = '\033[35m' # blue
UNDERLINED = '\033[4m'
BOLD = '\033[1m'
END = '\033[0m' # simple text (stop colourful text)
