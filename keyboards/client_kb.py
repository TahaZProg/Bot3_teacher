from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # , ReplyKeyboardRemove

b1 = KeyboardButton('/Расписание_уроков')
b2 = KeyboardButton('/Что_задано?')
b3 = KeyboardButton('/Скинь_ДЗ')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(b1, b2, b3)