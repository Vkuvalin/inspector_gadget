from aiogram.types import Message
from create_bot import dp, bot


'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
async def startRun(message: Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!')
        # await message.delete()
    except:
        await message.reply('Бот не добавлен. Необходимо добавиться к нему: \n@Multi_vlad_bot')


async def command_start_2(message: Message):
    await bot.send_message(message.from_user.id, 'Отправляю фото!')

'''**********************************************************************************************************'''

'''***********************************ЗАПУСК ФУНКЦИЙ*********************************************************'''
dp.register_message_handler(startRun, commands=['start', 'help'])
dp.register_message_handler(command_start_2, commands=['Новая_команда'])
'''**********************************************************************************************************'''