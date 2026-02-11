
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
khob ta alan fahmdiim kasi ag az /command estefade krd chijori ba add_handler(CommandHandler) miaym va
yek fucntion msiazim va ba update.message.reply_text behesh javab midim . khob ag bkhaym yeki message
bede chijori ono handle konim?

yek ghanone talaee
- kasi command dad --> command handler estefade mikonim
- kasi message dad --> message handler estefade mikonim

pas hala bayad berim message handler besazim
mesle hamishe
**yek tabe biroon misazim badesh add_handler mikonim b application**
pas biaid begim ag kasi message dad masalan biaym fght behesh javab bdim haminghd sade

shekle tabe hamonjorie daghighan
```python

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    await update.message.reply_text('مسیج دریافت شد')

```

hala mirim too main va inja addhanlder mikonim bejaye **commandhandler** messsage handler mikonim

```python
from telegram.ext import MessageHandler
from telegram.ext import filters

application.add_handler(MessageHandler(filters.TEXT,text_handler))

```
in yani ag kasi message dad, tabeye text_hadnler shoro bekar mikone k in tabe fght dar javab mige message daryaft shdo, ama ma ag bkhaym yeki yechi befrese ma fght y matne sade besh bedim k niazi b message ndrim , hamoon raveshe ghabli kafi bod, yani miomdim az **command** estefade mikardim ke. pas ma message handler misazim k messag e taraf ro begirim va bahsh kar konim
message e taraf koja mire? tooye yechizi bename ** update.message.text**

khob fek kon yek tabe misazim k ag taraf message dad salam yechi bgim khobi goft yechi javab bdim


```python
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zarf= update.message.text
    if zarf =='salam':
        #print('salam to chetori)
        await update.message.reply_text('سلام خوبی؟')

    elif zarf =='khoobi':
        await update.message.reply_text('ممنون تو خوبی؟')

    else:
        await update.message.reply_text('من نمی فهمم چی می گی')


```

ba estefade az **update.message.text** miaym va harfe user ro mirizm too zarf , bad miaym ba if elif else migim ag felan bod felan javab bde , felan bod felano javab bde. javab dadna ham k mesle ghabel bayad az **update.message.reply_text** estefade konim.


khob hamin ro ma omdim piade sazi kridm dar ![telegram_test3.py](/telegram_tutorial/telegram_test3.py)

hala ag runesh konim

```bsh
python telegram_test3.py
```
mibinim k

![messsage](/telegram_tutorial/tutorial_pictures/message.jpg)



---
## 2.5-Inlinekeyboards
khob ma ta alan balad shodim k az command handler estefade konim o message handler estefade konim . yani ag kasi ta alan bema command ferestad mesle **/start** ya inke bema **message** dad ma behesh ba **message** javab midadim ama khob aya hamishe ma mitonim message bdim? nmitonim b form haye dg javab bdim?
bale yeki az in rah ha ine ke behesh gozine neshoon bdim.

khob chijori? bayad gozine ro besazim. yani too oon tabe ee k ma handl emikonim , bejaye estefade az **update.message.reply_text()** bayad yekar konim bejaye **text** be trf gozine neshoon bde. 

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def menu_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #await update.message.reply_text('menu : menu1 , menu2 --> TEXT')
    keyboard = [
        #yek chizi k b user namayesh mdie, ba y mokhafaf
        [InlineKeyboardButton("گزینه 1", callback_data="opt1")],
        [InlineKeyboardButton("گزینه 2", callback_data="opt2")],
        #ezafe kon

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #hala to gozine haro sakhti --> bfrsi baraye ?? baraye user
    await update.message.reply_text('لطفا یک گزینه انتخاب کن',reply_markup =reply_markup )

```

tanha farghesh ine shoam yek zarf misazid bename keybord k yek **list** hast ke toosh **list** haee hast. too har **list** mitonid az class **InlinekeyboardButton** estefade konid ye aval oon chizi k mikhayd b user namayesh bede, va poshtesh y mokhafafe englisi mizarid

kole in **keyboard** k yek list k az list ha bood ro mindazid tooye **InlinekeyboardMarkup** va miriz y zarfe dg .

fght chizi k hast vaghty az **update.message.reply_text** estefade mikonid kenare textoon bayad az yek argument ya vorodie dg ee etsfeade konid bename **reply_markup** k ejaze mide .

khob hala hamchin chizio ma dairm
hala ino mitonid b soorate **message_handler** ya biad **command_handler** estefade konid.

```python
application.add_handler(CommandHandler('menu',menu_func))
```


mesale kamelsh dakhele ![telegram_test4.py](/telegram_tutorial/telegram_test4.py) mojod hast.
baraye run kafie bezanid

```bsh
python telegram_test4.py
```

va mibinid k vaghty rooye **menu** miznid choon commandhanlder has mifreste be tabeye **menu_func** va dar in tabe bejaye update.message.reply_text e khali , hamrahesh yek **markup** ferstadim , yani gozine ha. 

![menu](/telegram_tutorial/tutorial_pictures/menu.jpg)

hamontori k mibinid vaghty roo gozine ha bezanid hich javabi daryaft nmikonid . chraa???


---
## 3-Callbackquery handler
khob ta alan vorodi haee k momken bod user behemon bede , **command** bod mesle /start , /menu , /help va baghie , ya mitones kheyliu sade behemoon **message** bede va baraye hamashon miomdim az **handler** makhsoseshon estefade mikrdim mesle **commandhandler** ya **messagehandler** ama ag ma baraye taraf bejaye **text** e khali, biaym **Markup** ya gozine befresim , vaghtyy trf entkehab mikone , chi baramon ersal mishe?? 
behesh migan **callbackquery**


khob pas ma bayad yek tabe besazim k baid handle kone k vaghty k in goziine ha az tarafe user entkehab shod, ya behtre begim vaghty erssal mishe be samte python , bayad oono begirim. ama mesle gahbl ke **message** mirft tooye **update.message.text** inja ghaziash frgh mikone


```python
async def callback_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    query.answer()
    if query.data=='opt1':
        #await update.message.reply_text('you selected option 1')
        await query.edit_message_text(text='شما گزینه یک رو انتخاب کردید')
    elif query.data=='opt2':
        #await update.message.reply_text('you selected option 2')
        await query.edit_message_text(text='شما گزینه دو رو انتخاب کردید')
```
khob **update** too delesh yechizi dare be esme **callback_query** too delesh hast va oono mikeshim biron mirizim toye ye zarf b esme **query**
hamchnin vaghty miznim **query.answer()** yani montzre ta javab bde trf

khob too dele **query** ye chizi darim bname **data** in hamon chizzi has k vaghty user roo y dokme click bzne ag yadeton bashe tooye tarife dokme omdim yechize **mokhafaf** onja behine krdim


```python
[InlineKeyboardButton("گزینه 1", callback_data="opt1")],
        [InlineKeyboardButton("گزینه 2", callback_data="opt2")],
```

pas ag trf rooye gozine 1 bzne. **query.data** mishe opt1 va age taraf gozine 2 ro bzne **query.data** mishe opt2 . ba yek if o elif o in mitonim kh sade begim ag felan gozien ro ch konim.
fght inja bejay einke baraye send message b user bejaye **update.message.reply_text** miaym az chizi estefade mikonim bename **query.edit_message_text**.


khob hala in tabe k sakhtim ro miaym b appllcisaation add mikonim. inja bejaye messagehandler ya commmandhandler az yek handler e dg estefgade mikonim



```python
from telegram.ext import CallbackQueryHandler


application.add_handler(CallbackQueryHandler(callback_func))

```


baraye kamel mitonim az ![telegram_test5.py](/telegram_tutorial/telegram_test5.py)

kafie shoam run bznid
```bsh
python telegram_test5.py
```

avl fucntion menu gozine haro miare vaghty roosh bznid oon mokhgafafo mifrse b callbackquery handler
![menu](/telegram_tutorial/tutorial_pictures/gozine.jpg)


khob halaa  ma az query.edit_message estefade mikonim k gozine haro edit mizne va messasge mikone
![javab](/telegram_tutorial/tutorial_pictures/callback.jpg)



---
## CONVERSATION HANDLER
ma kh vaghta miaym az yek concept estefade mikonim bename **conversation handler** yani miaytm az chizaee k az bala yad grfitm mesle command handler o message handlero o callbackquery estefade mikonim.

yani ye bot migim koli command dare, harki har command ro zad vrede ye kanal, y dariche , ye **conversation** , yek goftogoo beshe k in **conversatyion** shamele command handler, message handler, callbackquery hast . 

baraye inkar shoma bayad yek tabe **command handler** dashte bashid va baghiu


```python
from telegram.ext import ConversationHandler
application.add_handler(ConversationHandler(entry_points=[CommandHandler('dashboard',dashboard_func)],
                                                            states={
                                                                'NAME':[MessageHandler(filters.TEXT,name_func)],
                                                                'AGE':[MessageHandler(filters.TEXT,age_func)],
                                                                'KEY':[CallbackQueryHandlerß(key_func)]
                                                            },
                                                            fallbacks=[])  ) 

```
bebinid inja b applicatin, ma add mikonim ye handler bename Conversationhandlr, toosh yechi dare bename **entry_points** k yani shjoroe ma chie, shoroe in conversation chie , ba yek command hsoro mishe masalan migim k yechi darim bename **dashboard** darim k b function dashbaord_func vasl mishe. va in tabe ha b ham dg vaslan b tgartib az tarigeh yechi bename **state**


```python
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

```
![dashboard](/telegram_tutorial/tutorial_pictures/dashboard.jpg)

in yani vaghty kasi rooye **/dashboard** mizane tabeey **dashboard_func** seda mikkhoe k toosh b taraf mige salam esmetoon ro befarmaeed , fght farghi k dare tahesh ma ychzii dari **return 'NAME'** ro barmigrdone.

**bejaye NAME , shoma harchi mitonid bezarid, adad, 0 , 1 , 2 harchi mikhayd** 
koja estefade mishe?? tooye khdoe main() ag bbinid neveshti daghigh
```python
states={
        'NAME':[MessageHandler(filters.TEXT,name_func)],
```
yani harmoghe oon tabe he return dad yani vghty NAME ro dad, in mige NAME mosavie ba felan tabe , yani ag NAME return dade shod tabeye **name_func** seda mizne . yani injori ma omdim tabeye dashboard_func ro vbasl krdim b tabetye name_func vasl krdim.

hala mirim tooye tabeye name_func


```python
async def name_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #mikham bedamesh b ye tabe dgg
    name = update.message.text
    await update.message.reply_text(f'سلام {name} خوش آمدید')
    await update.message.reply_text('سنتون چقدره')
    return 'AGE'

```
khobn hala update.message.text hamoon chizi hast k yani , bad az inke minevsie **esmeton ro begid** khob taraf harchi benvise , choon oon tabe vasle b in tabe. javabe taraf ersal mishe b in tabeye **name_func**

![name](/telegram_tutorial/tutorial_pictures/name.jpg)

kho inja update.message.text mishe hamon 'ali' va hamontor k mibinid await mizane yani
sari in soal ro miporse va 'AGE' ro barmigrdone va ag too **states** bebinid age ro vasl krde b tabeye badi


```python
'AGE':[MessageHandler(filters.TEXT,age_func)],
```

![sen](/telegram_tutorial/tutorial_pictures/age.jpg)

khob hala seni k inaj dadim mire tooye update.message.text . khob berim tabeye age_func ro benvisim

```python
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

```
yek tabeye pichide skahtim k age taraf age esh baalye 8 bashe k miad va barash keyword neshonmide , age paeen tar bashe mige shoma nemitonid az robot estefade konid va rasman az conversation kharej mishe **conversationhandler.END** yani baraye in masir dobare bayad bezane **/dashboard** ag ham kolan adad vared nakone , minevise seneton ro b adad vared konid va reutnr mikone **age** in AGE hamonie k b hamin tabe seda mizane, yani dobare in tabe montazere sene tarafe

hala ag sene trf balaye 8 bashe , hamontor k gofte shod dota gozine permium basic sakhte mishe va baraye taraf namayehs dade mishe. taraf ag rooye har gozine ee click kone, in tabe return mikone **KEY**

```python
'KEY':[CallbackQueryHandler(key_func)]
```
tabeye key_func fght motnazer vastade k behesh gozine befrestid, pas =in tabaro haminjori minevisim 


```python
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

```
besadegie tamam.


hala kolesho ma dakhele file ![telegram_test6.py](/telegram_tutorial/telegram_test6.py) darim k mitonid ba dastore zir runesh konid

```bsh
python telegram_test6.py
```



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
#Appendix B : TOKENS
Kolan yadetoon bashe k tooye code haye khdoetoon **password** , **token** va baghie chiz haye khososi ro mostaghim nazarid.
pas chikar konim?
kafie yek file i besazid bename .env daghighan hamoonjae k file e pythoneton hast
chijori?


injkori

```bsh
touch .env
```

in yek file e .env misaze va khob mitonid bazesh konim
albate havaseton bashe in file yek file e hidden hast va shoam nmitonid bebinidesh
```bsh
vim .env
```

rooye **i** miznid ta insertt baz she va bertoonid benevis masanal
```bsh
TOKEN = 'DSDSJKSHAKHSDKJDAHJKDHSA'
PASSWORD = '12345678'
```

harchi ramzo token o api o .. darid ro inaj berizid

hala bargrdid toye file e pythoneton
ghabl az in yadeton bashe hamchin ketabkhon ee bayad dashte bashid

```bsh
pip install python-dotenv
```

hala kafie oonjae k TOEKN bood biaid benevisid
```python
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

```
tabeye load_dotenv() k az ketabkhone dotnev hast, ejaze mide k dotenv biad bala
ba **os** vasl mishid b .env va khob 'token' yani b token vasl shod meghdaresho beriz tooye ye
zarf bename TOKEN. va injori kheyli safe hastid

ma daghighan haminkar ro omdim file e ![telegram_test6.py](/telegram_tutorial/telegram_test6.py) ro besoorate safe va amn neveshtim dar ![telegram_test7.py](/telegram_tutorial/telegram_test7.py)


**more advanced
haavseton bashe vaghty github mikhayd bznid
behich vaj git add .env nazadid yani hichvaght ino nazanid
```bsh
git add .env
```

yani ag inkar konid in file .env k havie passwordo token hatoon hast mire github

hata bartaye khial rahatie bishtr mitonid tooye foldere madare projedtetoon yek file besazid bename .gitignore 
in file rajebesh tozih dade mishe ama b sorate kholase , yechize k har no formati bzarid inja , dg ersal nmishe b samte github

```bsh
touch .gitignore
```

```bsh
vim .gitignore
```

rooye **i** bznid
bad bznid
```bsh
.env
*.env
```

bad dg save konid khial rahat

----
----
----
#Appendix C : Advanced Topics



----
----
----
# Appendix D : Summary

| Topic | Description | Key imports / components | Example file |
|-------|-------------|--------------------------|--------------|
| **Telegram setup** | Create bot via @BotFather, get token; name must end with `bot` | Token from BotFather | — |
| **Python setup** | Install library, use `main()` and `if __name__ == "__main__"` | `pip install python-telegram-bot` | — |
| **Application core** | Build app, add handlers, error handler, run polling | `Application.builder().token(TOKEN).build()`, `run_polling()` | — |
| **Error handler** | Always define and register to catch errors | `ContextTypes`, `application.add_error_handler()` | — |
| **Command Handler** | User sends `/command` (e.g. `/start`, `/help`) | `CommandHandler('cmd', func)`, `update.message.reply_text()` | telegram_test1.py, telegram_test2.py |
| **Message Handler** | User sends plain text (not command) | `MessageHandler(filters.TEXT, func)`, `update.message.text` | telegram_test3.py |
| **Inline Keyboards** | Show buttons instead of only text | `InlineKeyboardButton`, `InlineKeyboardMarkup`, `reply_markup` | telegram_test4.py |
| **CallbackQuery Handler** | User taps an inline button; handle by `callback_data` | `CallbackQueryHandler`, `update.callback_query`, `query.data`, `query.edit_message_text()` | telegram_test5.py |
| **Conversation Handler** | Multi-step flow: entry → states → next state or END | `ConversationHandler`, `entry_points`, `states`, `return 'STATE'`, `ConversationHandler.END` | telegram_test6.py |
| **Async pattern** | Handlers are async; use `await` for sending/editing | `async def`, `await` | Appendix A |
| **Tokens / .env** | Keep token out of code; load from `.env` | `python-dotenv`, `load_dotenv()`, `os.getenv('TOKEN')` | Appendix B |
| **.gitignore** | Never commit `.env`; add `.env` and `*.env` to `.gitignore` | — | Appendix B |