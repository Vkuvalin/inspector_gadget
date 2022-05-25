from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# Анотация к импортам
"""
1. ReplyKeyboardMarkup  - это создание обычной клавиатуры.   Размер - resize_keyboard=True, Сворачивает - one_time_keyboard=True
2. KeyboardButton       - с помощью него создается кнопка.
3. ReplyKeyboardRemove  - короче она типа нужна, чтобы клава удалялась.
"""


# Создание кнопок и именование их
b1 = KeyboardButton('И тебе привет!')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/Ксю')
b4 = KeyboardButton('Гуру-мастер')

b10 = KeyboardButton('/отключить_клавиатуру')

# Данные кнопки благодаря второму аргументу будут возвращать отличные от названия сообщения.
# b4 = KeyboardButton('Поделиться номером', request_contact=True)     # Телефон. Скидывает номер юзера (он должен разрешить)
# b5 = KeyboardButton('Отправить где я', request_location=True)       # Телефон. Скидывает геолокацию юзера (он должен разрешить)


# Создаём клавиатуру и заполняем
'''
1. resize_keyboard      - меняет размер кнопок.
2. one_time_keyboard    - сворачивает клавиатуру после выбора.
3. row_width=           - устанавливает кол-во кнопок в одном ряду.
                          не распространяется на метод row
# Для callback кнопок
4. callback_data=       - значение, на которое будет реагировать хендлер (типа команды)
5. show_allert=         - выдает не простро всплывающее, но с подтверждением "ок". До 200 символов
'''
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2, b3).insert(b4).add(b10)

# Есть 3 типа добавления:
# add()         - добавляет тупо с новой строки
# insert()      - добавляет справа, если есть место
# row(b1, b2)   - все кнопки в строку



"""Создание inline клавиатуры"""
# Подробная информация в файле inline.py
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')

# Также крайне круто, что кнопки можно засунуть в список
x = [InlineKeyboardButton(text='Ссылка2', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка2', url='https://google.com'),
     InlineKeyboardButton(text='Ссылка2', url='https://google.com')]

urlkb.add(urlButton, urlButton2).row(*x)

# Нужно отметить, что ссылки добавляются непосредственно к ответному сообщению
"""
@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)
"""


# Функционал реализации поиска фотографий для Ксю
# Общий выбор
'''*********************ФОРМА-(Ксю)*************************'''
ksu_С_1 = KeyboardButton('Рандом')
ksu_С_2 = KeyboardButton('Дата')
ksu_С_3 = KeyboardButton('За месяц')
ksu_С_4 = KeyboardButton('Отмена')
kb_ksu_С = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ksu_С.row(ksu_С_1, ksu_С_2, ksu_С_3).add(ksu_С_4)


# Рандом
ksu_R_1 = KeyboardButton('Одно фото')
ksu_R_2 = KeyboardButton('Как повезет')
ksu_R_3 = KeyboardButton('Назад')
ksu_R_4 = KeyboardButton('Пожалуй, пойду')
kb_ksu_R = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ksu_R.row(ksu_R_1, ksu_R_2).add(ksu_R_3).insert(ksu_R_4)

# Месяцы
ksu_M_1 = KeyboardButton('01')
ksu_M_2 = KeyboardButton('02')
ksu_M_3 = KeyboardButton('03')
ksu_M_4 = KeyboardButton('04')
ksu_M_5 = KeyboardButton('05')
ksu_M_6 = KeyboardButton('06')
ksu_M_7 = KeyboardButton('07')
ksu_M_8 = KeyboardButton('08')
ksu_M_9 = KeyboardButton('09')
ksu_M_10 = KeyboardButton('10')
ksu_M_11 = KeyboardButton('11')
ksu_M_12 = KeyboardButton('12')
kb_ksu_M = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
kb_ksu_M.row(ksu_M_1, ksu_M_2, ksu_M_3, ksu_M_4).row(ksu_M_5, ksu_M_6, ksu_M_7, ksu_M_8).row(ksu_M_9, ksu_M_10, ksu_M_11, ksu_M_12)
'''*********************************************************'''
