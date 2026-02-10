'''
avalin boti k sakhtime

template --> telegram_test1.py
'''

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes

TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad start --> in matno barash bfrs
    #await update.message.reply_text('salam khoosh oomadin')
    await update.message.reply_text('سلام به ربات فناوری مهندسی اینگلیسی خوش آمدید .')


#in hatamn hamine
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

def main():
    application = Application.builder().token(TOKEN).build()

    #ag kasi roye /start zad vaslesh kon b start_func()
    application.add_handler(CommandHandler('start',start_func))



    application.add_error_handler(error_handler)
    application.run_polling()

if __name__ == "__main__":
    main()