# -*- coding: utf-8 -*-
"""файл app.py, імпортуємо всі необхідні бібліотеки, 
конфігураційні файли та api. 
Якщо деякі бібліотеки відсутні, встановіть їх через pip.
"""
import telebot
import json

import jubber.config as config
import jubber.api as api

from jubber import HOROSCOPE, GREETINGS, HELP_MESSAGES, get_edited_signature, get_exchange_diff, serialize_ex

from jubber.horo import get_daily_horoscope, get_monthly_horoscope, get_weekly_horoscope

bot = telebot.TeleBot(config.TOKEN)


# Декоратор message_handler обробляє нове вхідне повідомлення будь-якого типу - текст, фотографію, наклейку тощо. Усі обробники повідомлень виконуються в порядку їх додавання.


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
   """ Функція, яка декорована обробником повідомлень може 
       мати будь-яке ім’я, але вона може
       приймати лише один параметр (повідомлення)."""
   # Метод reply_to - відправляє повідомлення у відповідь на повідомлення від користувача.    
   bot.reply_to(message, GREETINGS)


@bot.message_handler(commands=['help'])
def send_help(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Message the developer', url='telegram.me/couchjanus'
       )
   )
   bot.reply_to(message, HELP_MESSAGES, reply_markup=keyboard)




# horoscope
# ========================================
@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = HOROSCOPE
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


# https://horoscope-app-api.vercel.app/
def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, *WEEK* or *MONTH*."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    day = message.text.capitalize()
    print("challenging_days", day)
    if day == 'Week':
        horoscope = get_weekly_horoscope(sign)
        print("WEEK", horoscope)
        challenging_days = "week"
    elif day == 'Month':
        horoscope = get_monthly_horoscope(sign)
        challenging_days = "month"
    else:
        horoscope = get_daily_horoscope(sign, day)
        challenging_days = "date" 
    
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data[challenging_days]}'
    
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")






# ===============exchange===============
@bot.message_handler(commands=['exchange'])
def send_exchange(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'), telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'))

    bot.reply_to(message, 'Click on the currency of choice:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data.startswith('get-'):
       get_ex_callback(query)

# Let’s implement the get_ex_callback method:

def get_ex_callback(query):
   bot.answer_callback_query(query.id)
   send_exchange_result(query.message, query.data[4:])

def send_exchange_result(message, ex_code):
   bot.send_chat_action(message.chat.id, 'typing')
   ex = api.get_exchange(ex_code)
   bot.send_message(
       message.chat.id, serialize_ex(ex),
       reply_markup=get_update_keyboard(ex),
       parse_mode='HTML'
   )

def get_update_keyboard(ex):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.row(
       telebot.types.InlineKeyboardButton(
           'Update',
           callback_data=json.dumps({
               't': 'u',
               'e': {
                   'b': ex['buy'],
                   's': ex['sale'],
                   'c': ex['ccy']
               }
           }).replace(' ', '')
       ),
       telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy'])
   )
   return keyboard


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data.startswith('get-'):
       get_ex_callback(query)
   else:
       try:
           if json.loads(data)['t'] == 'u':
               edit_message_callback(query)
       except ValueError:
           pass

def edit_message_callback(query):
   data = json.loads(query.data)['e']
   exchange_now = api.get_exchange(data['c'])
   text = serialize_ex(
       exchange_now,
       get_exchange_diff(
           get_ex_from_iq_data(data),
           exchange_now
       )
   ) + '\n' + get_edited_signature()
   if query.message:
       bot.edit_message_text(
           text,
           query.message.chat.id,
           query.message.message_id,
           reply_markup=get_update_keyboard(exchange_now),
           parse_mode='HTML'
       )
   elif query.inline_message_id:
       bot.edit_message_text(
           text,
           inline_message_id=query.inline_message_id,
           reply_markup=get_update_keyboard(exchange_now),
           parse_mode='HTML'
       )


def get_ex_from_iq_data(exc_json):
   return {
       'buy': exc_json['b'],
       'sale': exc_json['s']
   }



# Обробляє всі повідомлення
@bot.message_handler(func=lambda message: True)
def echo_all(message):
   bot.reply_to(message, message.text)
