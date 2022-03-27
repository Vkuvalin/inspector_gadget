from aiogram import Bot, Dispatcher
import asyncio
import os
from config import TOKEN


loop = asyncio.get_event_loop()                                             # Создается поток с потощью asyncio, в котором обрабатываются все события
try:
    bot = Bot(token=os.getenv('TOKEN'))
except:
    bot = Bot(token=TOKEN)

dp = Dispatcher(bot, loop=loop)
