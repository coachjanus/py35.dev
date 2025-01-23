# jubber/config.py
""" 
Файл налаштування config.py містить: 
 - токен бота 
 - часовий пояс, у якому він працюватиме 
 Часовий пояс потрібен, щоб вказати час оновлення повідомлення. 
 Telegram API не дозволяє дізнатися часовий пояс користувача,тому 
 оновлений час має відображатися з підказкою про часовий пояс.
"""

from os import environ as env

from dotenv import load_dotenv
load_dotenv()

# TOKEN = '2118247526:AAH-crDn7TaL8HbKYM-lr4oaIsCpcIckbiI'  

# TOKEN = '6106717184:AAErAY-mc8S8wDE5WrC-OE1vjkhNMvRTQH8'
# потрібно змінити на токен власного бота

TOKEN = env['TOKEN']
TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'
