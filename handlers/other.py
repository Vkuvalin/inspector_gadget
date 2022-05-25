import json, string
from aiogram.types import Message
from aiogram import Dispatcher
from create_bot import dp, bot
from config import admin_id


'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
# Включение/отключение мата
matStatus = 1
async def mat_start(message: Message):
    if message.from_user.id == admin_id:
        global matStatus
        if message.text[1:] == 'matoff':
            await bot.send_message(message.from_user.id, 'Мат отключен!')
            matStatus = 0

        if message.text[1:] == 'maton':
            await bot.send_message(message.from_user.id, 'Мат включен!')
            matStatus = 1
'''**********************************************************************************************************'''


'''***********************************СЛУЖЕБНАЯ ЧАСТЬ/ПОДВАЛ*************************************************'''
async def echo_send(message: Message):
    # Фильтер для мата
    if ({i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set()) and matStatus == 0:
        await message.reply('Мат запрещен!')
        await message.delete()
'''***********************************************************************************************************'''

'''***********************************ЗАПУСК ФУНКЦИЙ**********************************************************'''
def register_message_other(dp: Dispatcher):
    dp.register_message_handler(mat_start, commands=['matoff', 'maton'])




    dp.register_message_handler(echo_send)  # Вот эта хрень, вроде как, должна быть всегда в самом низу.
'''***********************************************************************************************************'''