import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data_base import sqllite_db
from create_bot import dp, bot


async def temp_print(id,text):
    now = datetime.datetime.now()
    await bot.send_message(text=text+str(now), chat_id=id)
    print(now)

async def sch_reminder(): # напоминает об уроке
    infos = await sqllite_db.sql_read_sch()
    dzs = await sqllite_db.sql_read_dz()
    print(infos)
    print(dzs)
    scheduler = AsyncIOScheduler()
    scheduler.start()
    # scheduler.add_job(temp_print,'interval', seconds=5) # работает
    # scheduler.add_job(temp_print,'date', run_date=datetime.datetime(2023, 3, 31, 20, 56)) # Работает
    # min = 35
    # scheduler.add_job(temp_print,'cron',day_of_week=6 , hour=16, minute=min, second=0,args=['Задача 1 ---- ']) # Работает
    # scheduler.add_job(temp_print,'cron',day_of_week=6 , hour=16, minute=min, second=10,args=['Задача 2 ---- ']) # Работает
    # scheduler.add_job(temp_print,'cron',day_of_week=6 , hour=16, minute=min, second=20,args=['Задача 3 ---- ']) # Работает
    # scheduler.add_job(temp_print,'cron',day_of_week=6 , hour=16, minute=min, second=30,args=['Задача 4 ---- ']) # Работает

    for info in infos:
        if info[6] == 1:
            scheduler.add_job(temp_print,'cron',day_of_week=info[1], hour=info[2], minute=info[3],args=[info[7], info[0]])
            print(info[0]+', день '+str(info[1])+' время '+str(info[2])+':'+str(info[3])+' --- '+str(info[7]))

# def dz_reminder(): # напоминает о домашнем задании
#     pass