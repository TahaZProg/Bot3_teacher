from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqllite_db
from reminders import client_rem
# from aiogram.types import ReplyKeyboardRemove

def week_day(day_of_week, type_ret = 1):
    name_day = ''
    if day_of_week == 0:
        name_day = 'понедельникам'
    elif day_of_week == 1:
        name_day = 'вторникам'
    elif day_of_week == 2:
        name_day = 'средам'
    elif day_of_week == 3:
        name_day = 'четвергам'
    elif day_of_week == 4:
        name_day = 'пятницам'
    elif day_of_week == 5:
        name_day = 'субботам'
    elif day_of_week == 6:
        name_day = 'воскресеньям'
    if type_ret ==1:
        return name_day
    else: return day_of_week

def time_of_lesson(hour,min):
    if min < 10:
        return str(hour)+'.0'+str(min)
    else: return str(hour)+'.'+str(min)

async def rem_sch(id=403753648):
    await bot.send_message(id, 'Скоро урок')


'''**************************Клиетнская часть********************'''
# @dp.message_handler(commands=['start','help'])
async def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \nhttps://t.me/qpwodjfhglacbvnxvbot')

# @dp.message_handler(commands=['Расписание_уроков'])
async def teacher_schedule_command(message:types.Message):
    #обработать для каждого пользователя отдельный ответ
    infos = await sqllite_db.sql_read_sch()
    str_answer = ''
    str_name = ''
    for info in infos:
        wday = week_day(info[1])
        time_start = time_of_lesson(info[2],info[3])
        time_end = time_of_lesson(info[4], info[5])
        # wday = info[1]
        if not(str_name == info[0]):
            if not(str_answer==''):
                await bot.send_message(message.from_user.id, str_answer)
            str_name = info[0]
            str_answer = info[0]+' занимается по '+wday+' c '+time_start+' по '+time_end
            if info[4] == 1:
                str_answer += ' (уведомления включены)'
            else: str_answer += ' (уведомления выключены)'
        else:
            str_answer += ' и по '+wday+' c '+time_start+' по '+time_end
            if info[4] == 1:
                str_answer += ' (уведомления включены)'
            else:
                str_answer += ' (уведомления выключены)'
    if not(str_answer==''):
        await bot.send_message(message.from_user.id, str_answer)
        # await client_rem.rem_sch()
        # await bot.send_message(403753648,'**403753648**')



# @dp.message_handler(commands=['Что_задано?'])
async def teacher_dz_command(message:types.Message):
    #обработать для каждого пользователя отдельный ответ
    await bot.send_message(message.from_user.id, 'Рабочая тетрадь, страница 78')

# @dp.message_handler(commands=['Скинь ДЗ']):
async def teacher_dz_in_chat(message:types.Message):
    file = types.InputFile
    file = open('static/pdf/Урок 6.pdf', 'rb')
    await bot.send_document(message.from_user.id, file)

    await bot.send_message(message.from_user.id, 'Файл отправлен')
    # await sqllite_db.sql_read_dz(message)

# регистрируем хендлеры
def register_handlers_client (dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(teacher_schedule_command, commands=['Расписание_уроков'])
    dp.register_message_handler(teacher_dz_command, commands=['Что_задано?'])
    dp.register_message_handler(teacher_dz_in_chat, commands=['Скинь_ДЗ'])
