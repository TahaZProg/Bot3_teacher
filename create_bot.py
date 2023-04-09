from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


storage = MemoryStorage()
# token1='1262777671:AAHdMRsubEP-CxKppEClVs12WOOP-TP8nio'
# bot = Bot(token=token1)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)


