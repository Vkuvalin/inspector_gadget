import sqlite3, os
from create_bot import bot

# Для создания физического файла
""" #790
def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
"""

async def sql_read(message, date=None, mode=0):
    try:
        global cur, base
        base = sqlite3.connect('imageKsu.db')
        cur = base.cursor()
        print("Подключен к SQLite")

        if mode == 0:
            if cur.execute('SELECT photo, name FROM photos WHERE name=? LIMIT 1', (date,)).fetchall() != []:
                return 'ok'

        if mode == 1:
            for ret in cur.execute('SELECT photo, name FROM photos WHERE name=? LIMIT 1', (date,)).fetchall():
                try:
                    await bot.send_photo(message.from_user.id, ret[0], f'\n Дата: {ret[1]}')
                except:
                    continue

        if mode == 2:
            for ret in cur.execute('SELECT photo, name FROM photos WHERE name=?', (date,)).fetchall():
                try:
                    await bot.send_photo(message.from_user.id, ret[0], f'\n Дата: {ret[1]}')
                except:
                    continue

        # Продолжение
        """ #790
        for row in cur.execute('SELECT photo, name FROM photos WHERE name=?', (name,)).fetchall():
            name  = row[0]
            photo = row[1]
            photo_path = os.path.join("C:/Users/VLAD/Desktop/telegram_bot/data_base/", name + ".jpg")
            write_to_file(photo, photo_path)
            os.remove(photo_path)
        """
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if base:
            base.close()
            print("Соединение с SQLite закрыто")

""" Вариант с открытием из папки"""

# photo = open(f'F:\PycharmProjects\TelegramBots\bot\{random_file}', 'rb').read()
# await bot.send_photo(message.from_user.id, photo)
