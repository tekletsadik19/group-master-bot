from telegram.ext import Updater, CommandHandler, MessageHandler, ContextTypes
from telegram import Update
from constants import *

def start(update:Update, context:ContextTypes):
    update.message.reply_text("MI#43")

def main():
    updater = Updater(TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    #Handlers
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()