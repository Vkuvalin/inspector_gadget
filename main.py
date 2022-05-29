# Библиотека для написания бота телеграм. Что-то вроде оболочки, под который скрыт официальны апи с его сылками get, post и тп
# Bot  -  класс бота (корорый имеет методы из api)  # Dispatcher -  доставщик апдейтов  # executor -  заускает работу бота
from aiogram import executor
from create_bot import dp
from data_base import sqlite_db



sqlite_db.sql_start()
print('Подключение к БД прошло удачно')

if __name__ == "__main__":                                     # Такая конструкция изолирует данный код, если он запускается именно из этого файла
    from handlers import client, admin, other


    client.register_message_client(dp)
    admin.register_message_admin(dp)
    other.register_message_other(dp)

    executor.start_polling(dp, skip_updates=True,
                           on_startup=admin.send_to_admin)     # skip_updates=True таким образом бот будет пропускать сообщения,
                                                               # которые приходили ему, когда он был не онлайн. В моем случае (за искл. последнего)
