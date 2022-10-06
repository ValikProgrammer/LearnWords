from conf import *



def average(scors):
    sum = 0 
    for score in scors:
        sum += score
    return round(sum / len(scors))


async def userStatFunc(id):
    logging.info("Sending user statisctics.")

    userStatDict1 = getDataFromJson(STATISTICS_USER_SCORE)
    userStatDict = {k: v for k, v in sorted(userStatDict1.items(), key=lambda item: item[1],reverse=True)}
    userStat = f"Users Statisctics (by score):\n"

    maxLenUserName  = 0
    for k in userStatDict.keys():
        maxLenUserName = max(maxLenUserName,len(k))

    for user,scors in userStatDict.items():
            userStat += f"<code><b>{user:<{maxLenUserName}}</b></code> : {average(scors)}%\n"

    await bot.send_message(id,userStat)

async def dictStatFunc(id):
    logging.info("Sending dict statisctics.")

    dictStatDict1 = getDataFromJson(STATISTICS_DICT)
    dictStatDict = {k: v for k, v in sorted(dictStatDict1.items(), key=lambda item: item[1],reverse=True)}
    dictStat = "Dictionary Statisctics (by using):\n"

    maxLenDictName  = 0
    for k in dictStatDict.keys():
        maxLenDictName = max(maxLenDictName,len(k))

    for dictName,amount in dictStatDict.items():
        dictStat += f"<code><b>{dictName:<{maxLenDictName}}</b></code>  : {amount}\n"

    await bot.send_message(id,dictStat)





async def main(id):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    text_and_data = [
        ('Dict Rating', 'dictrating'),
        ('User Rating', 'userrating'),
    ]

    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns)

    await bot.send_message(id,"Choose the rating:", reply_markup=keyboard_markup)
    

@dp.message_handler(commands=['dictrating'])
@dp.callback_query_handler(text='dictrating')  
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await dictStatFunc(query.from_user.id)


@dp.message_handler(commands=['userrating'])
@dp.callback_query_handler(text='userrating') 
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await userStatFunc(query.from_user.id)


    
    

    

   


    

