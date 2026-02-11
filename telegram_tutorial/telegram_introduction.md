
# Telegram Tutorial (Amoozeshe sakhte robot telegram)

Khob baraye sakhte robot telegram shoma bayad do ta kar konid yeki tooye khode telegram yeki tooye python

-  1- Telegram Side
-  2- Python side

---

## **1-Telegram Side**
khob shoma ebteda mirid be bote **@BotFather** va vaghty varedesh mishid dastoore **/newbot** ro mizanid
va mige ye **name** begid va minveisid va mige yek username k hatman bayad tahesh ba bot tamom she
masalan **fanavari_english_bot** badesh behetoon yek token mide k yek adad bozorg mesle
```bsh
token ---> 6363636363636363636363636363636363636363
```

va kafie bezanid rooye esme boteton yani masalan **@fanavari_english_bot** va in bot baraye shomas mitonid axesho avaz konid, description bezarid va ....

![botfather](/telegram_tutorial/tutorial_pictures/botfather.jpg)


---

## **2-Python Side**
hala in rooye kar bod, bayad bbinim oon posht chekhabare k behesh migan backend
aval bayad tooye mohiti k code mizanid ketabkhoneye telegram ro berizid k ejaze bde shoma tarahi konid

```bsh
pip install python-telegram-bot
```

ag yadetoon biad ma se no raveshe code zani dashtim
- monolothic az bal b paeen --> python ... --> run --> yek bar run mishe
- Funcrtion based --> function haro misazid
- OOP (class and object)


khob mesle **django** , **fastapi** , **telegram** ham az shoma mikhad k function based besazid
bedoonid vaghty shoma koli file python masalan darid vaghty runesh mikonid hich etfaghi nmiofte
masalan

```bsh
mkdir new_project
cd new_project
touch new_file.py
vim new_file.py
```

badesh inro ezafe konid
```python
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
```

hala ag file ro run konid yani
```bsh
python new_file.py
```
hich etefaghe khasi nemiofte. chon fght chanta function define shode hamin (tarif shode)
pas too in ravesh ha shoam niaz darid b yek tabe bename **main()** 
pass kole in ravesh , mesle kh chiza, shoma koli tabe misazid va dar enteha hamchin chizi


```python
def main():
    #tooye main estefade mikoni
    pass
    
if __name__ == "__main__":
    main()

```
yani hamechi tooye main() hast va kh sade


---
### **Badane asali main()**
khob hamontor k goftim badaneye asli in main() hast
shoma miaid va dar inja dar main() in ro mizarid
**nokte** : yadeton bashe harchi inja minevisam ro tooye tabe main() benevisid

```python
application = Application.builder().token(TOKEN).build()
```

khob application k yek zarf hast , Application ham yek class k bayad improt she va TOKEN ham tokeni k
az telegram grftid.

```python
from telegram.ext import Application
TOKEN= 'YOUR-TOKEN-HERE.....'
```

khob joda azin bydefault shoma bayad yek tabe bename error handler besazid k hamishegie

```python
from telegram import Update 
from telegram.ext import ContextTypes

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

```

va hamchnin dar main bayad hamishe error handler ro bzarid k error haro handle kone va hamchnin
runing pooling yani hamishe roo ejra bashe

```python
def main():
    application = Application.builder().token(TOKEN).build()

    #ag kasi roye /start zad vaslesh kon b start_func()
    application.add_handler(CommandHandler('start',start_func))



    application.add_error_handler(error_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
```


Azinja bebad shoma bayad dar nazar begirid in forme aslie har *BOTE TELEGRAM* i hast va khob
shoma fght bayad hey berid bala tabe besazid , va oono add konid be application

yekbar dg takid mikonam
**shoma fght bayad hey berid bala tabe besazid , va oono add konid be application**

ma khob ma hastimo koli handler.


-----
### **Handler chie?**
Handler yani , vaghty yeki mikhad biad be bot payam bede, chan ravesh dare
- command
vaghty mian mizanan rooye /start /help /harchizi b ina migan command va motefavet hast ba message

-message
vaghty message midan kh b sadegi

-callbackquery
vaghty rooye yek dokme ee click mikonan , oon click krdne dokme b esme callbackquery shenakhte mishe



Pas ma bayad baraye harkodom yani baraye **command, message, callbackquery** handler besazim va b application add konim


-----
## 1-Command Hanlder

khob baraye skahte in , shoma hamantor k gfot shode yek tabe misazid

```python
from telegram import Update 
from telegram.ext import ContextTypes

async def esme_tabe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام به ربات فناوری مهندسی اینگلیسی خوش آمدید .')

```
khob in yani yek tabe misazid k bayad **async** bashe . va khob hamishe toosh jolosh minevsiid update = update va ... --> in yek **template** hast hamishe
tooye dele tabe har dastoori k gharare baraye user ersal she ghablesh **await** mide

**update.message.reply_text** yek tabe hast k yek vorodi migire ke **text* hast va vaghty mdiid hamon
ersal mishe.
khob in tabe be khodie khod b dard nmikhore va kari nmikone , bayad biaym begim agha ino b **application** vasl konim


```python
def main():
    application = Application.builder().token(TOKEN).build()

    #ag kasi roye /start zad vaslesh kon b start_func()
    #****
    application.add_handler(CommandHandler('start',start_func))



    application.add_error_handler(error_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
```
inja daghighan darim migim harki rooye **start** zad vaslesh kon b tabeye **start_func**
application.add_handler(CommandHandler(a,b))
a--> che commandi zadan
b--> b ch functioni vaslesh kone


khob pas harki rooye start bezane barash in payam mire, kole code kamel dakhele ![telegram_test1.py](/telegram_tutorial/telegram_test1.py) mojood hast.


hala ag brim va runesh konim kafie ba python runesh konim code ro
```python
python telegram_test1.py
```
age berim test konim mibinim rooye **command start** ag bezanim mibinim hamoon matne ersal mishe

![botfather](/telegram_tutorial/tutorial_pictures/start.jpg)



---
#### commandhandler haye dg
hamchenin ma harcheghadr bekhaym mitoonim besazim. masalan mikhaym yek command /help besazim
daghighan bayad aval **yek tabe** be hamoon esm besazim , dakhelesh az reply_text stefade konim k
va dar application add_handler konim

in daghighan yani yek tabe darim help_func() ag seda bokhore **update.message.reply_text** mikone , yani message mifrese baraye user chizi k dakhele tabe hast 
```python
async def help_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
    سلام به بخش کمک بات خوش امدید
    دستورات موجود:

    استارت : /start
    کمک : /help
    """
    await update.message.reply_text(text)
```

khob key in tabe seda mikhore? ma mirim tooye main() va migim k 

migim k bbin too **applciation** vaghty kasi zad roye **/help** bayad tabeye **help_func** seda bokhore k dakhele tabe gofte shode ch matni ersal she
```python
application.add_handler(CommandHandler('help',help_func))
```


code kamel dakhele ![telegram_test2.py](/telegram_tutorial/telegram_test2.py) mojod hast.

shoma kafie in ro run konid
```bsh
python telegram_test2.py
```

va mibinid k ag command /help ro bznid hamonchizi k tarif krdid ersal msihe yani tabeye help_func seda khorde
![help](/telegram_tutorial/tutorial_pictures/help.jpg)


---
## 2-Message Handler
khob ta alan fahmdiim kasi






----
----
----
# Appendix A : Async Def
neeed to be completed

tavabe hamishe async hast ??
farghe async va sync chie\
sync --> ye nafar seda zad hanmon lahze ejra mishe
async --> 100 nafar seda bznan , va hamaro kenare ham kenare ham 
async --> 10 ta tabe too dele hame --> ye tabe e on vasat --> gheymat bgire
b site vasle ,... --> stop (wait) await 
async  
wait --> await


----
----
----
#Appendix B : Advanced Topics
