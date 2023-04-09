from aiogram.utils import executor
from create_bot import dp
from data_base import sqllite_db
from reminders import client_rem


async def on_startup(_):
    print('Бот запущен')
    sqllite_db.sql_start()
    # await client_rem.sch_reminder()
    await client_rem.sch_reminder()


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp,skip_updates=True, on_startup=on_startup)
