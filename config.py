TOKEN = "5194627649:AAEmIdgm6SjKA0Yxm_tVYQEDOO5blCakuuE"
admin_id = 5009372827









'''***********************************СВАЛКА*****************************************************************'''

'''
if message.from_user.username == "Steppz" or message.from_user.username == "yazabavnya":
    await message.answer(text="Здарова, Влад")
text = f"Привет, ты написал мне: {message.text}"
await bot.send_message(chat_id=message.from_user.id, text=text)
text_2 = f"Вот оно, если потерял: {message.text}"
await  message.reply(text_2)
'''

# Основные данные
"""
message.from_user.id
message.from_user.first_name
message.from_user.last_name
message.from_user.username
"""




# Варианты написания
"""
await message.answer(message.text)                                      # Просто отвечает
await message.reply(message.text)                                       # Отвечает с цитатой
await bot.send_message(message.from_user.id, message.text)              # Отвечает только если запущен личный чат
"""

# Просто оставляю на память, чтобы видеть, как работает логика
""" @dp.message_handler(commands=['matoff', 'maton']) """

"""
# Прикольно, что он реагирует на любую последовательность! Можно что-то прикольное сделать
@dp.message_handler(lambda message: 'слово' in message.text):
async def word(message: Message):
    await message.answer(message.text)

# Этот друг определяет, с нужного ли слова начинается предложение
@dp.message_handler(lambda message: message.text.startswith('слово')):
"""