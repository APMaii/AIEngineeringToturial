'''

In The Name of God

Telegram Tutorial

Created on Tue Feb 10 16:13:37 2026

@author: Ali Pilehvar Meibody



'''

'''
Moghadame

Bot bayad too  khode telegram besazi -->

@BotFather

/newbot

name --->  Fanavari English Bot

username--bot ---> fanavari_english_bot
token ---> 6363636363636363636363636363636363636363



7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI




Too mohiti k darid
pip install python-telegram-bot



ag yadeton bashe se raveshe code zani bod
1-monolothic az bal b paeen --> python ... --> run --> yek bar run mishe

2- Funcrtion based --> function haro misazid


agrar ma 4,5 ta tabe besazim vaghty run konim hichi nmishe
def welcome():
	print('salam')

def goodbye():
	print('salam')

def newton(m,a=10):
	f=m*a
	return f

def add(a,b):
	c=a+b
	print(c)
	return c



def main():
    tooye main estefade mikoni
    
if __name__ == "__main__":
    main()




pass hamechi tooye main() hast 

toosh miaym tooye maiN()

application = Application.builder().token(TOKEN).build()


az inja bebad
biroon az tabeye main() tavabe ee misazim va azashoon use mikonim
dakhele main()

chijori? --> vasleshon mikonim b zarfe application()


application.add_handler()

y fard miad bot e shoma rooye slash / chizi minevise
command

command ro yeki bayad handle kone
behssh migan command handler

handle vaghty command zadan

application.add_handler(CommandHandler(a,b))
a--> che commandi zadan
b--> b ch functioni vaslesh kone


tavabe hamishe async hast ??

farghe async va sync chie\


sync --> ye nafar seda zad hanmon lahze ejra mishe

async --> 100 nafar seda bznan , va hamaro kenare ham kenare ham 

async --> 10 ta tabe too dele hame --> ye tabe e on vasat --> gheymat bgire
b site vasle ,... --> stop (wait) await 

async  
wait --> await

hameye tabe ha dota vorodi daran
update , context 
(update: object, context: ContextTypes.DEFAULT_TYPE)
#inaro taghir bdi (ADVANCED)


'''

#import -------
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes




TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #vaghtyy trf zad start --> in matno barash bfrs
    await update.message.reply_text('salam khoosh oomadin')




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



