from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton,\
    ReplyKeyboardMarkup, InputTextMessageContent, InlineQueryResultArticle, InlineQuery
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import asyncio
import hashlib

# Локальные импорты
from data_base import sqlite_db, open_db_file
from config import admin_id
from create_bot import dp, bot
from keyboards import kb_client, kb_ksu_С, kb_ksu_M, kb_ksu_R

# Для "Ксю"
from random import *
import datetime
import radar


'''***********************************ОБЩИЙ******************************************************************'''
list_word = ['Опаньки!', 'Маленькое чудо', 'Сердечко', 'Ой, какие же глазки!',
             'Шикарна!', 'Весело живете :)', 'Мне кажется, это любовь.']
'''**********************************************************************************************************'''

'''***********************************ОСНОВНАЯ ЧАСТЬ*********************************************************'''
# Стартовые команды
async def startRun(message: Message):
    try:
        if message.text[1:] == 'start':
            await bot.send_message(message.from_user.id, 'Приветствую тебя, мой друг!', reply_markup=kb_client)
            await message.delete()
            await bot.send_message(message.from_user.id, 'Советую посетить "/help" - там ты узнаешь все мои команды!')

        if message.text[1:] == 'help':
            await bot.send_message(message.from_user.id, 'Да мне бы кто помог...')
            await asyncio.sleep(2)  # Типа создает задержку! Офигенная функция
            await bot.send_message(message.from_user.id, 'Ладно-ладно... Сейчас что-нибудь придумаю.')
            await asyncio.sleep(2)
            await bot.send_message(message.from_user.id, 'Хм...')
            await asyncio.sleep(2)
            await bot.send_message(message.from_user.id, 'Прости. Я пока поленился заполнять это раздел...')
    except:
        await message.reply('Бот не может ответить - необходимо добавиться к нему: \n@Multi_vlad_bot')


# Что можно было бы сюда грузить?
async def kto(message: Message):
    await sqlite_db.sql_read(message)

# Отключение клавиатуры
async def keyboardRemove(message: Message):
    await bot.send_message(message.from_user.id, 'Пока-пока', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, 'Если снова понадоблюсь, напиши "/start"')



'''*********************ФОРМА-(Ксю)*************************'''
class Ksu_search(StatesGroup):
    choice = State()
    random = State()
    date = State()
    date2 = State()
    months = State()
    months2 = State()

# Начало диалога загрузки.
async def ksu(message: Message):
    if message.from_user.id == admin_id or message.from_user.username == "yazabavnya" or message.from_user.username == "Steppz":
        await Ksu_search.choice.set()
        await message.answer('Выбери режим: ', reply_markup=kb_ksu_С)
    else:
        await message.answer('Упс, прости, но доступ запрещен.')

# 0 - Основное меню
async def load_choice(message: Message):
    if message.from_user.id == admin_id or message.from_user.username == "yazabavnya" or message.from_user.username == "Steppz":
        if message.text == 'Рандом':
            await Ksu_search.random.set()
            await message.answer('Отлично! Сейчас поищу что-нибудь инетересное.', reply_markup=kb_ksu_R)

        elif message.text == 'Дата':
            await Ksu_search.date.set()
            await message.answer('Как ищем?', reply_markup=kb_ksu_R)

        elif message.text == 'За месяц':
            await Ksu_search.months.set()
            await bot.send_message(message.from_user.id, 'Я эту функцию не стал доделывать пока что. Выдает только за 1й год.')
            await message.answer('Как ищем?', reply_markup=kb_ksu_R)
        else:
            await message.answer('Ой, а я таких слов не знаю. Воспользуйся, пожалуйста, кнопками.')

# Функция выхода из состояния
async def cancel_handler(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("Ничего страшного", reply_markup=kb_client)

# 1 - Рандом
async def load_random(message: Message, state: FSMContext):
    if message.from_user.id == admin_id or message.from_user.username == "yazabavnya" or message.from_user.username == "Steppz":
        mode = None
        if message.text == 'Одно фото':
            mode = 1
        elif message.text == 'Как повезет':
            mode = 2
        elif message.text == 'Назад':
            await ksu(message)
            return None
        elif message.text == 'Пожалуй, пойду':
            await state.finish()
            await message.answer("Пока-пока! Заходи ещё", reply_markup=kb_client)
            return None
        else:
            await message.reply('Ой, а я таких слов не знаю. Воспользуйся, пожалуйста, кнопками.')
            await Ksu_search.random.set()
            return None


        date = str(radar.random_datetime(start='2021-01-29', stop=str(datetime.datetime.now()).split(' ')[0])).split(' ')[0]
        while await open_db_file.sql_read(message, date, 0) != 'ok':
            date = str(radar.random_datetime(start='2021-01-29', stop=str(datetime.datetime.now()).split(' ')[0])).split(' ')[0]

        await open_db_file.sql_read(message, date, mode)
        await bot.send_message(message.from_user.id, choice(list_word))



# 2 - Дата
async def load_date(message: Message, state: FSMContext):
    if message.from_user.id == admin_id or message.from_user.username == "yazabavnya" or message.from_user.username == "Steppz":
        mode = None
        if message.text == 'Одно фото':
            mode = 1
        elif message.text == 'Как повезет':
            mode = 2
        elif message.text == 'Назад':
            await ksu(message)
            return None
        elif message.text == 'Пожалуй, пойду':
            await state.finish()
            await message.answer("Пока-пока! Заходи ещё", reply_markup=kb_client)
            return None
        else:
            await message.reply('Ой, а я таких слов не знаю. Воспользуйся, пожалуйста, кнопками.')
            await Ksu_search.date.set()
            return None

        async with state.proxy() as data:
            data['mode'] = mode

        await Ksu_search.date2.set()
        await message.answer("Теперь введи интересующую дату вот так: 2021-10-10", reply_markup=ReplyKeyboardRemove())

# 2.1 - Дата-2
async def load_date2(message: Message, state: FSMContext):
    mode = None
    async with state.proxy() as data:
        mode = data['mode']

    date = message.text

    if await open_db_file.sql_read(message, date, 0) != 'ok':
        await message.reply('Прости, но этот день покрыт тайной.', reply_markup=kb_ksu_R)
        await Ksu_search.date.set()
        return None

    else:
        await open_db_file.sql_read(message, date, mode)
        await bot.send_message(message.from_user.id, choice(list_word), reply_markup=kb_ksu_R)
        await Ksu_search.date.set()
        return None



# 3 - За месяц
async def load_months(message: Message, state: FSMContext):
    if message.from_user.id == admin_id or message.from_user.username == "yazabavnya" or message.from_user.username == "Steppz":
        mode = None
        if message.text == 'Одно фото':
            mode = 1
        elif message.text == 'Как повезет':
            mode = 2
        elif message.text == 'Назад':
            await ksu(message)
            return None
        elif message.text == 'Пожалуй, пойду':
            await state.finish()
            await message.answer("Пока-пока! Заходи ещё", reply_markup=kb_client)
            return None
        else:
            await message.reply('Ой, а я таких слов не знаю. Воспользуйся, пожалуйста, кнопками.')
            await Ksu_search.months.set()
            return None

        async with state.proxy() as data:
            data['mode'] = mode

        await Ksu_search.months2.set()
        await message.answer("Выбери месяц. (Пока считаю от рождения)", reply_markup=kb_ksu_M)

# 3.1 - За месяц-2
async def load_months2(message: Message, state: FSMContext):
    mode = None
    async with state.proxy() as data:
        mode = data['mode']

    month = message.text

    date = str('2021' + '-' + str(month) + '-' + str(randint(0, 31)))
    count = 0
    while await open_db_file.sql_read(message, date, 0) != 'ok' and count < 100:
        date = str('2021' + '-' + str(month) + '-' + str(randint(0, 31)))
        count += 1

    await open_db_file.sql_read(message, date, mode)
    await bot.send_message(message.from_user.id, choice(list_word), reply_markup=kb_ksu_R)
    await Ksu_search.months.set()
    return None
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

'''*********************"Гуру-мастер"*************************'''
class Guru_master(StatesGroup):
    question = State()

# Начало диалога загрузки.
async def guru(message: Message):

    await message.answer(f'Привет, {message.from_user.first_name}. Я Всевидящий и знаю ответ на любой твой вопрос.')
    await asyncio.sleep(2)
    await message.answer('Я готов ответить на твои вопросы и указать тебе путь.')
    await asyncio.sleep(2)
    await message.answer('Задай свой вопрос так, чтобы ответ был "Да" или "Нет". Если с тебя хватит истины, просто скажи "Стоп"')
    await asyncio.sleep(2)
    await Guru_master.question.set()
    await message.answer('Напиши свой вопрос: ', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Стоп')))

async def guru_question(message: Message, state: FSMContext):
    if message.text == 'Стоп':
        await state.finish()
        await message.reply("Возвращайся, если возникнут вопросы!", reply_markup=kb_client)
        return None

    name = [message.from_user.first_name, 'Путник', 'Мылыш', 'Заблудший', 'Юнец', 'Странник']
    answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да",
           "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего",
           "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
           "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
           "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
           "Перспективы не очень хорошие", "Весьма сомнительно"]
    await message.reply(choice(answers))
    await asyncio.sleep(3)

    await Guru_master.question.set()
    await message.answer(f'Готов ли ты услышать ещё больше истины, {choice(name)}?')
    await message.answer(' Задай свой вопрос: ', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Стоп')))
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

'''*********************"Inline-mode"*************************'''
@dp.inline_handler()
async def inline_handelr(query: InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/'+text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [InlineQueryResultArticle(
        id = result_id,
        title='Статья Wikipedia:',
        url=link,
        input_message_content=InputTextMessageContent(
            message_text=link))]

    await query.answer(articles, cache_time=1, is_personal=True)
'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
'''**********************************************************************************************************'''




'''***********************************ЗАПУСК ФУНКЦИЙ*********************************************************'''
def register_message_client(dp : Dispatcher):
    dp.register_message_handler(startRun, commands=['start', 'help'])
    dp.register_message_handler(keyboardRemove, commands=['отключить_клавиатуру'])
    dp.register_message_handler(kto, commands=['Кто?'])

    '''*********************ФОРМА-(Ксю)*************************'''
    dp.register_message_handler(ksu, commands=['Ксю'], state=None)

    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(load_choice, state=Ksu_search.choice)
    dp.register_message_handler(load_random, state=Ksu_search.random)
    dp.register_message_handler(load_date, state=Ksu_search.date)
    dp.register_message_handler(load_date2, state=Ksu_search.date2)
    dp.register_message_handler(load_months, state=Ksu_search.months)
    dp.register_message_handler(load_months2, state=Ksu_search.months2)
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

    '''*********************"Гуру-мастер"*************************'''
    dp.register_message_handler(guru, Text(equals='гуру-мастер', ignore_case=True), state=None)
    dp.register_message_handler(guru_question, state=Guru_master.question)
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
'''**********************************************************************************************************'''