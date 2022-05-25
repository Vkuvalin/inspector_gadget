import os
from config import admin_id
from create_bot import dp, bot
from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext   # Указывает, что данный хендлер используется в Машине-состоянии
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb



'''****************************************СЛУЖЕБНАЯ ЧАСТЬ***************************************************'''
'''*********************ЗАДАНИЯ***********************'''
async def send_to_admin(dp):
    print('Вывод служебной информации: подключение к БД и тп')
    try:
        await bot.send_message(chat_id=os.getenv('admin_id'), text="Бот запущен")
    except:
        await bot.send_message(chat_id=admin_id, text="Бот запущен")
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
'''*********************ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ*********************'''
ID = None
'''**********************************************************************************************************'''



'''*******************************************ОСНОВНАЯ ЧАСТЬ*************************************************'''
'''*********************MODERATOR*********************'''
# Для группы. Проверяет является ли человек модератором. Можно использовать в хуеве туче функций.
async def make_changes_command(message: Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Доступ разрешен.', reply_markup=admin_kb.kb_admin)
    await message.delete()
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''



'''*********************ФОРМА*************************'''
# Алгоритм загрузки фоток в БД - "telki"
class FSMadmin(StatesGroup):
    photo = State()
    name = State()

# Начало диалога загрузки.
async def cm_start(message: Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Загрузи фото')

# Функция выхода из состояния -------------------------------- ВЫХОДА
async def cancel_handler(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("Не парься, бывает)")
# Функция выхода из состояния -------------------------------- ВЫХОДА

# Ловим первый ответ и пишем в словарь
async def load_photo(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply("Теперь введи название")

# Второй
async def load_name(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text.capitalize()
        await FSMadmin.next()

        await sqlite_db.sql_add_command(state)
        await message.reply("Форма заполнена")
        await state.finish()  # После данной команды очищается полностью память
'''**********************************************************************************************************'''



'''***********************************ЗАПУСК ФУНКЦИЙ*********************************************************'''
def register_message_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)

    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
'''**********************************************************************************************************'''