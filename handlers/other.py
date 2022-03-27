import json, string
from aiogram.types import Message
from create_bot import dp, bot



'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
# Включение/отключение мата
matStatus = 1
async def mat_start(message: Message):
    global matStatus
    if message.text[1:] == 'matoff':
        await bot.send_message(message.from_user.id, 'Мат отключен!')
        matStatus = 0

    if message.text[1:] == 'maton':
        await bot.send_message(message.from_user.id, 'Мат включен!')
        matStatus = 1
'''**********************************************************************************************************'''
'''***********************************ЗАПУСК ФУНКЦИЙ(С ПАРАМЕТРАМИ)******************************************'''
dp.register_message_handler(mat_start, commands=['matoff', 'maton'])
'''**********************************************************************************************************'''





'''***********************************СЛУЖЕБНАЯ ЧАСТЬ/ПОДВАЛ*************************************************'''
@dp.message_handler()
async def echo_send(message: Message):
    # Фильтер для мата
    if ({i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set()) and matStatus == 0:
        await message.reply('Мат запрещен!')
        await message.delete()
'''***********************************************************************************************************'''
'''***********************************ЗАПУСК ФУНКЦИЙ(БЕЗ ПАРАМЕТРОВ)******************************************'''
dp.register_message_handler(echo_send)
'''***********************************************************************************************************'''












'''***********************************СВАЛКА*****************************************************************'''
'''
if message.from_user.username == "Steppz":
    await message.answer(text="Здарова, Влад")
text = f"Привет, ты написал мне: {message.text}"
await bot.send_message(chat_id=message.from_user.id, text=text)
text_2 = f"Вот оно, если потерял: {message.text}"
await  message.reply(text_2)
'''

# Варианты написания
"""
await message.answer(message.text)                                      # Просто отвечает
await message.reply(message.text)                                       # Отвечает с цитатой
await bot.send_message(message.from_user.id, message.text)              # Отвечает только если запущен личный чат
"""

# Просто оставляю на память, чтобы видеть, как работает логика
""" @dp.message_handler(commands=['matoff', 'maton']) """