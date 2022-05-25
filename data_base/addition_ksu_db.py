# По сути нужен лишь для загрузки файлов в БД
import sqlite3 as lite
import os



# Получение списка файлов
imagesList = os.listdir('C:/Users/VLAD/Desktop/telegram_bot/images')

# Функция открытия изображения в бинарном режиме
def readImage(filename):
    fin = open('C:/Users/VLAD/Desktop/telegram_bot/images/' + filename, "rb")
    img = fin.read()
    fin.close()
    return img

# Создание соединения
def sql_addition_start():
    global base, cur
    base = lite.connect('imageKsu.db')
    cur = base.cursor()
    if base:
        print('Подключение прошло успешно.')
    # Создание таблицы
    base.execute('CREATE TABLE IF NOT EXISTS photos(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT PRIMARY KEY NOT NULL , photo BLOB NOT NULL, Data BLOB NOT NULL)')
    base.commit()
    return None

# Функция добавления изображения
def sql_add_command(data_tup):
    cur.execute('INSERT INTO photos(name, photo, Data) VALUES (?, ?, ?)', data_tup)
    base.commit()

# Инициализация процесса
def loadingDB():
    sql_addition_start() # Потом убрать, тк есть уже в main

    for i in range(len(imagesList)):
        filename = imagesList[i]

        name = filename.split(' ')[0]
        image = readImage(filename)
        binary = lite.Binary(image)
        data_tuple = (name, image, binary)

        sql_add_command(data_tuple)
        base.commit()
    base.close()
    print('Прошо успешно.')
    print("Соединение с SQLite закрыто")

loadingDB()