import telebot
from config import TOKEN
from telebot import types
from wikipedia import *

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('🔎 Search', '⚙️ Settings')

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    msg = f"<b>Welcome {user}</b>"
    bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def do_bot(message):
    if message.text == '🔎 Search':
        msg = f"<i>What do you want to know about?</i>"
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
    elif message.text == '⚙️ Settings':
        msg = f"<i>The settings are not ready yet</i>"
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
    else:
        try:
            wk = wikipedia.summary(message.text)
            bot.send_message(message.chat.id, wk, reply_markup=markup)
        except exceptions.DisambiguationError:
            bot.send_message(message.chat.id, 'Hech qanday ma\'lumot topilmadi.', reply_markup=markup)

bot.polling(none_stop=True)
