# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def bop(bot, update):
    bot.message.reply_text('24岁，事学生')
def tellstory(bot,update):
    bot.message.reply_text("雷澳事木毛")
def help(bot,update):
    bot.message.reply_text("""
                           开发中。。。
                           botcreator: @cedar_234
                           """)

def main():
    updater = Updater('1675454535:AAEaF_IHzhdwQkVruUSPpByeNzZzvCtIt3s')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('selfintroduce',bop))
    dp.add_handler(CommandHandler("tellastory",tellstory))
    dp.add_handler(CommandHandler("help",help))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
