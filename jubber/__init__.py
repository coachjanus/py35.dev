# jubber/__init__.py

import pytz
import datetime

__app_name__ = "jubber"

TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'
P_TIMEZONE = pytz.timezone(TIMEZONE)




GREETINGS = '''
  Hawaii! 
  Get daily horoscope for your zodiac sign.
    - To get daily horoscope press /horoscope
  I can show you PrivatBank exchange rates.
    - To get the exchange rates press /exchange.
    - To get help press /help.
'''

HELP_MESSAGES = '''
 1) To receive a list of available currencies press /exchange.
 2) Click on the currency you are interested in.
 3) You will receive a message containing information regarding the source and the target currencies, buying rates and selling rates.
 4) Click “Update” to receive the current information regarding the request. The bot will also show the difference between the previous and the current exchange rates.
 5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.
'''

HOROSCOPE = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."

EMOJI_UP = '''<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↗️" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/72x72/2197.png">" src="https://s.w.org/images/core/emoji/72x72/2197.png">'''

EMOJI_DOWN = '''<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↘️" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/72x72/2198.png">" src="https://s.w.org/images/core/emoji/72x72/2198.png">'''


def serialize_exchange_diff(diff):
   result = ''
   if diff > 0:
       result = f'({str(diff)} {EMOJI_UP})'
   elif diff < 0:
       result = f'({str(diff)[1:]} {EMOJI_DOWN})'
   return result

def get_exchange_diff(last, now):
    return {
       'sale_diff': float("%.6f" % (float(now['sale']) - float(last['sale']))),
       'buy_diff': float("%.6f" % (float(now['buy']) - float(last['buy'])))
    }


def get_edited_signature():
   return f'''<i>Updated {str(datetime.datetime.now(P_TIMEZONE).strftime('%H:%M:%S'))}({TIMEZONE_COMMON_NAME})</i>'''

# CCY is an abbreviation for the word, "currency."  Therefore, CCY = Currency.
# For Example: 50 CCY means 50 units of the base currency of your credit/debit card.

def serialize_ex(ex_json, diff=None):
   result = f'''<b>{ex_json['base_ccy']} -> {ex_json['ccy']}:</b>\n\nBuy: {ex_json['buy']}'''
   if diff:
       result += f''' {serialize_exchange_diff(diff['buy_diff'])}\nSell: {ex_json['sale']}  {serialize_exchange_diff(diff['sale_diff'])}\n'''
   else:
       result += f"\nSell: {ex_json['sale']}\n"
   return result