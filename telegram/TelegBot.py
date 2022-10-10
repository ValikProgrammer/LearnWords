# @LearnWordsValikbot
from conf import *
import keep_alive as ka

@dp.message_handler(commands=['s','start',"on"])
async def start_cmd_handler(message: types.Message):
    if (message.from_user.username is None) :
        logging.info(f"Username is **null** : id {message.from_user.id}")

    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = [
        ('Repeate Words', 'repeate'),
        ('Add Words', 'add'),
        ("Write words","write")
    ]

    btnShare  = types.InlineKeyboardButton(text='Share',switch_inline_query="Хочешь владеть английским как носитель языка? Заходи! ")
    btnRating = types.InlineKeyboardButton(text='Rating',callback_data="rating")

    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns).add(btnRating,btnShare)

    await message.reply("Hi!\nChoose the Action:", reply_markup=keyboard_markup)
    

# catch callbcak from inline Buttons (Choose action)
@dp.message_handler(commands=['repeat'])
@dp.callback_query_handler(text='repeate')  
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    from modules import repeateWordsClass
    import importlib
    importlib.reload(repeateWordsClass)
    from modules import repeateWordsClass
    await repeateWordsClass.main(query.from_user.id,query.from_user.username)

@dp.message_handler(commands=['add'])
@dp.callback_query_handler(text='add') 
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    writeDictionary = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
    await writeDictionary.main(query.from_user.id)

@dp.message_handler(commands=['write'])
@dp.callback_query_handler(text='write') 
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    writeDictionary = __import__(WRITE_DATA_SCRIPT_PATH[:-3])
    await writeDictionary.main(query.from_user.id)

@dp.message_handler(commands=['rating'])
@dp.callback_query_handler(text='rating') 
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    showStat = __import__(SHOW_STATISTICS[:-3])
    await showStat.main(query.from_user.id)

@dp.message_handler(commands=['userrating'])
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    showStat = __import__(SHOW_STATISTICS[:-3])
    await showStat.userStatFunc(query.from_user.id)

@dp.message_handler(commands=['dictrating'])
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    showStat = __import__(SHOW_STATISTICS[:-3])
    await showStat.dictStatFunc(query.from_user.id)

@dp.message_handler(commands=['help'])
async def doNotUnderstand(message: types.Message):
    await message.reply("HELP: You need to write the commands . For example /start")


def main():
    logging.info("Stating script(main func Telebot.py)")
    # add all folders to the system path
    path, dirs, files = next(os.walk(PATH))
    for i in range (0,len(dirs)):
        sys.path.insert(i, dirs[i])

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    keep_alive()
    main()

