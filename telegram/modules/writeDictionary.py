from conf import *


# States
class Form(StatesGroup):
    dictName = State()  # Will be represented in storage as 'Form:name'
    text = State()  # Will be represented in storage as 'Form:age'

# @dp.message_handler(commands='start')
async def cmd_start(id):
    """
    Conversation's entry point
    """
    # Set state
    await Form.dictName.set()

    await bot.send_message(id,"Hi there! What's your dictName?")


# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.dictName)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process dict name
    """
    async with state.proxy() as data:
        data['dictName'] = message.text

    await Form.next()
    await message.reply("Enter the text from Englsih Book:?")


@dp.message_handler(state=Form.text)
async def process_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        """
        userMessage = str(message)
        finalText = message.text
        print(userMessage[-1],userMessage[-2],userMessage[-3],userMessage[-4],userMessage[-5])
        
        if ( "}" == userMessage[-1]):
            print("only object")

        else:
            print("WARNING message too long . Was splited")
            # это значит что сообщение слишком большое 
            # когда сообщение большое то телеграм разделяет сообщение на несколько сообщений
            # "}" это конец обьекта message который мы получили
            # если в строке тольео этот обьект , это значит что размер сообщения < 4096 и сообшение находиться в атрибуте text
            # а если после этого обьекта еще что-то есть , то это как раз
            # те самые отсальные сообщения которые разбил телеграм
            # и мы их просто достаем из строки
            indexObjectEnd = userMessage.rindex("}")
            otherMessages = userMessage[indexObjectEnd:]
            finalText    += "\n==FUCK==\n\n\n\n\n\=====\n\\n\n\n"+ otherMessages

        writeDataToFile("seeText.txt",finalText)
        """
        cleanText = __import__(CLEAN_TEXT_ALGORITHM[:-3])
        jsonText = cleanText.main(message.text)
        writeDataToFile(f"dictionaries/{data['dictName']}.json",jsonText)


        # Remove keyboard
        markup = types.ReplyKeyboardRemove()
        await bot.send_message(message.from_user.id, text=f"Thanks! Your added <b>{data['dictName']}</b> . To repeate this dictionary start the bot againg:/start.",reply_markup=markup)
    # Finish conversation
    await state.finish()


async def main(id):
    await cmd_start(id)

