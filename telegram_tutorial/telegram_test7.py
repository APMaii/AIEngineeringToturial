'''
SECURITY SYSTEM
Nokte 1 --> hichvaght ramz, password, token , api key dakhele code nazar


dar jaee k file et hast , bayad yek file besazi bename .env


'''

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import ConversationHandler

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad start --> in matno barash bfrs
    #await update.message.reply_text('salam khoosh oomadin')

    #
    start_text  = f"""
    سلام به ربات زبان برنامه نویسی همراه با انگلیسی خوش آمدید 
    برای استفاده 
    ابتدا از ....
    """

    await update.message.reply_text(start_text)


async def dashboard_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad dashboard --> in matno barash bfrs
    #await update.message.reply_text('salam khoosh oomadin')

    #
    dashboard_text = f"""
    سلام اسمتون رو بفرمایید :‌
    """
    await update.message.reply_text(dashboard_text)

    #mikham bedamesh b ye tabe dggg
    return 'NAME'



async def name_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #mikham bedamesh b ye tabe dgg
    name = update.message.text

    #zakhriahs konm ,....

    await update.message.reply_text(f'سلام {name} خوش آمدید')
    await update.message.reply_text('سنتون چقدره')
    return 'AGE'


async def age_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    age = update.message.text

    if age.isdigit():
        age = int(age)
        if age >= 8:
            await update.message.reply_text('شما میتونید از ربات استفاده کنید')

            keyword = [
                [InlineKeyboardButton("پرمیوم", callback_data="permium")],
                [InlineKeyboardButton("ساده ", callback_data="basic")],
            ]
            reply_markup = InlineKeyboardMarkup(keyword)

            await update.message.reply_text('لطفا یک گزینه انتخاب کن',reply_markup =reply_markup )
            return 'KEY'

        else:
            await update.message.reply_text('شما نمیتونید از ربات استفاده کنید')
            return ConversationHandler.END
    else:
        await update.message.reply_text('سنتون رو به عدد وارد کنید')
        return 'AGE'


async def key_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #gozine ee k entekhab shdoe?

    query = update.callback_query
    query.answer()

    if query.data=='permium':
        await query.edit_message_text(text='شما پرمیوم انتخاب کردید')
        return ConversationHandler.END
    elif query.data=='basic':
        await query.edit_message_text(text='شما ساده انتخاب کردید')
        return ConversationHandler.END

#in hatamn hamine
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")


def main():
    #step1 -- file .env besaz va ramzato beriz tosh
    #tooye jaee k file has --> tleegram_test7.py

    #touch .env

    #vim .env

    #i --> insert chizi benvisi

    #TOKEN = 'dsshgddgsgdgdsgsd'

    #:wq


    #step2 -- az ramz haye tooye .env estefade kon
    #pip install python-dotenv
    from dotenv import load_dotenv
    import os
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    #az botfather gereftimesh


    application = Application.builder().token(TOKEN).build()

    #ag kasi roye /start zad vaslesh kon b start_func()
    application.add_handler(CommandHandler('start',start_func))


    #entry_points --> ba chi shoro she? --> /dashboard
    application.add_handler(ConversationHandler(entry_points=[CommandHandler('dashboard',dashboard_func)],
                                                            states={
                                                                'NAME':[MessageHandler(filters.TEXT,name_func)],
                                                                'AGE':[MessageHandler(filters.TEXT,age_func)],
                                                                'KEY':[CallbackQueryHandler(key_func)]
                                                            },
                                                            fallbacks=[])  ) 

    application.add_error_handler(error_handler)
    application.run_polling()



if __name__ == "__main__":
    main()