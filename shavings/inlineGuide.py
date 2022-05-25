from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import TOKEN

# Комментарии
"""
Данные кнопки удобно использовать локально (не обязательно выносить в отдельный файл)
https://www.youtube.com/watch?v=gpCIfQUbYlY&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&index=9
Остановился на 25.00 - там дальше уже пошел код
"""



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
answ = dict()       # Для хранения голосов. Лучше пользоваться БД, тк словарь при рестарте будет обнулен


# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка4', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x)

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

# Call-back кнопки
inkb = InlineKeyboardMarkup(row_width=1)
inButton1 = InlineKeyboardButton(text='Нажми меня', callback_data='www')
inButton2 = InlineKeyboardButton(text='Like', callback_data='like_1')
inButton3 = InlineKeyboardButton(text='Не Like', callback_data='like_-1')

inkb.add(inButton1).row(inButton2, inButton3)

@dp.message_handler(commands='test')
async def url_command(message: types.Message):
    await message.answer('Какое-то голосование', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_')) # Можно указать как на прямую: text='команда из callback_data'
async def www_call(callback : CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)

"""
    # Если хочу выводить текстом
    await callback.message.answer('Нажата кнопка')
    await callback.answer('Тут могу записать сообщение об усп. выполнении')
    # Если всплывающим окном
    await callback.answer('Нажата кнопка')
"""



executor.start_polling(dp, skip_updates=True)

# Идеи по реализации inline и callback кнопок
"""
1. Добавлять к фоткам (сделать только для админа) кнопки удаления из бд
2. Сделать лайки. Думаю, не для Ксю, но ещё какой-нибудь фишки.
3. 
"""