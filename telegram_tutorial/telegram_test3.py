'''
ino omadim az telegram_test2.py copy paste kardim

mikjaym message handler besazim
'''

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters


async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad start --> in matno barash bfrs
    #await update.message.reply_text('salam khoosh oomadin')
    print('start command rsid')
    await update.message.reply_text('سلام به ربات فناوری مهندسی اینگلیسی خوش آمدید .')


async def help_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad start --> in matno barash bfrs
    #await update.message.reply_text('salam khoosh oomadin')
    text = """
    سلام به بخش کمک بات خوش امدید
    دستورات موجود:

    استارت : /start
    کمک : /help
    """
    await update.message.reply_text(text)



async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zarf= update.message.text
    #in message e tarafe
    #print(zarf)

    if zarf =='salam':
        #print('salam to chetori)
        await update.message.reply_text('سلام خوبی؟')

    elif zarf =='khoobi':
        await update.message.reply_text('ممنون تو خوبی؟')

    else:
        await update.message.reply_text('من نمی فهمم چی می گی')

#esmesho taghir bede b text_handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zarf= update.message.text
    #in message e tarafe
    #print(zarf)
    await update.message.reply_text(f'you said :{zarf}')

    



#in hatamn hamine
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

def main():
    #az botfather gereftimesh
    TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
    application = Application.builder().token(TOKEN).build()

    #ag kasi roye /start zad vaslesh kon b start_func()
    application.add_handler(CommandHandler('start',start_func))
    application.add_handler(CommandHandler('help',help_func))

    #application , meesagehandlero biar
    #message haee k havie TEXT hast  ro
    #bede b function text_handler() 
    application.add_handler(MessageHandler(filters.TEXT,text_handler))



    application.add_error_handler(error_handler)
    application.run_polling()

if __name__ == "__main__":
    main()