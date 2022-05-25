# https://www.youtube.com/watch?v=siSRd4s7_ro - урок по данной теме

import sqlite3
# 1. Данная БД может работать прямо из кода(файлов) + можно прям в pycharm её включить.
# 2. Является однопоточной (одновременная запись невозможна).
# 3. Ухты! В ней нет необходимости указывать типизацию (динамическая типизация).
    # Но можно и указать:
    # text      - строка    # integer   - целое число
    # real      - float     # blob      - любой тип данных
    # null      - None
"""
Если, например, в тип text будет передано число, то оно просто сконвертируется в str. 
Так и в других случаях. Поэтому особо нет смысла их указывать, как обычно и делают.
"""

# from file import x                          импорт файла с массовыми данными
# Внутренности файла:
x = [["user0", "1000000"], ["user1", "1000001"], ["user2", "1000002"]]



base = sqlite3.connect('new.db') # Либо создает, либо коннектится
cur = base.cursor()              # Нужен для чтения и внесения изменения


base.execute('CREATE TABLE IF NOT EXISTS data(login PRIMARY KEY, password)')  # Создание таблицы
base.commit()      # Сохраняет изменения в БД

# Обычное внесение данныых
cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny123', '123123'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?)', ('bon123', '19993'))
base.commit()

# Массовое внесение данных, например, из большого списка из списки
cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
base.commit()

# Замена значений в БД. Одиночное
cur.execute('UPDATE data SET password="xyi" where login="bon123"')
base.commit()


# Получени данных из БД
getBD = cur.execute('SELECT * FROM data').fetchall()
r = cur.execute('SELECT password FROM data WHERE login="jonny123"').fetchone()

# Удаление данных
cur.execute('DELETE FROM data') # Всех данных
cur.execute('DELETE FROM data WHERE login="jonny123"') # Точечно
base.commit()

# Удаление БД к херам
base.execute('DROP TABLE IF EXISTS data')
base.commit()

# Безопасное отключение от БД
base.close()