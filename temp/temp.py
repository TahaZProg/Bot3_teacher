import schedule
import time
import telebot

bot = telebot.TeleBot("1262777671:AAHdMRsubEP-CxKppEClVs12WOOP-TP8nio")

def send_message():
    bot.send_message(403753648, 'Привет, как дела?')

schedule.every().day.at("20:55").do(send_message)
schedule.every().day.at("20:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)