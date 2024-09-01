import telebot
import os
import random

TOKEN = os.environ.get('TOKEN', 'значение не найдено')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id
    response = "Как я могу тебе помочь?"
    bot.send_message(chat_id, response)

@bot.message_handler(commands=['random'])
def send_randow(message):
    chat_id = message.chat.id
    number = random.randint(0, 100)
    response = f'Случайное число: {number}'
    bot.send_message(chat_id, response)


if __name__ == "__main__":
    bot.polling(none_stop=True)