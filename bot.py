import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord


from email import message
from click import command
import requests
import logging
from tracemalloc import start
import wikipedia
from pyexpat.errors import messages
from urllib import request
from aiogram import *
from aiogram.dispatcher.filters import Text



API_TOKEN = 'You token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("🤖Uz_imlo Botiga Xush Kelibsiz \n\n  /rules 👈 bosing !")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler(commands="rules")
async def help_users(message: types.Message):
    await message.reply("Assalomu Alaykum hurmatli obunachi🖐\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n bot sizga yozgan so'zingizni to'g'ri yoki noto'g'riligini aytib beradi.➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n ✅ Адабиёт  ❌Adabiyot  \n\n /help 👈 bosing")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)



if __name__ == '__main__':
    executor.start_polling(dp)


################################################################################################
