import sqlite3 as lite
from create_bot import bot

# Создание соединения
def sql_start():
    global base, cur
    base = lite.connect('kto.db')
    cur = base.cursor()
    if base:
        print('Подключение прошло успешно.')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY)')
    base.commit()

# Функция добавления изображения
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}')