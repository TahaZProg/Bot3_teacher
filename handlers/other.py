from aiogram import types
import json, string
from aiogram import types, Dispatcher
from create_bot import dp, bot

'''**************************Общая часть********************'''

# @dp.message_handler()
async def echo_send(message:types.Message):
    set_cenz = set(json.load(open('cenz.json')))
    set_of_mes = set(i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' '))
    if set_of_mes & set_cenz != set():
        await message.reply('Мы за чистую речь!\nГоворите и пишите правильно, пожалуйста!')
        await message.delete()
    else:
        await bot.send_message(message.from_user.id, 'Позвать админа?')

# регистрируем хендлеры
def register_handlers_other (dp: Dispatcher):
    dp.register_message_handler(echo_send)
