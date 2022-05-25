from aiogram import Bot, Dispatcher
import asyncio
import os
from config import TOKEN

# Данный класс позвоняет хранить данные в оперативной памяти.
# Тут же ещё есть встроенные БД (монго и редис). Их лучше использовать для важных данных. + оперативка обнуляется.
from aiogram.contrib.fsm_storage.memory import MemoryStorage


'''**********************************************************************************************************'''
# Создается поток с потощью asyncio, в котором обрабатываются все события
loop = asyncio.get_event_loop()
storage = MemoryStorage()

try:
    bot = Bot(token=os.getenv('TOKEN'))
except:
    bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage, loop=loop)
'''**********************************************************************************************************'''