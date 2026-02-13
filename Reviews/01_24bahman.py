"""
Created on Fri Feb 13 07:47:29 2026

@author: Ali Pilehvar Meibody


----- PYTHON REVIEW -------
1- python built in function
2- Keywords (if, else, for, while, def , class)
3- Variables (numbers, str, iterables)

----Python Advanced topics on class (OOP)----



------SIDE -----------
AI_CLI.py 
b shoma ejaze mide bejaye GUI , Bash estefade konid ta
ba systemetoon sohbat konid
dar sade tarin halat b shoma komak mikone , yek folder bsazid (mkdir)
varedesh bshid (cd) , liste file haotno bbinid (ls) , yek fil besazid
har formati (.txt .md .py .cpp .json ,...) ba (vim , nano) [touch khali misakht]

taghir bdid --> vim
jabeja konid --> mv
file ro bebinid --> cat
copy konid --> cp
hazf konid --> rm mizadid

tools va abzar hast --> CLI TOOL --> komak mikrd 
vim , nano 
networking --> ping ,....
yekish --> git hast --> modiriat

[[yadeton bashe vared github bshid update konid darsname]]



AI_GIT.md
tadris shode --> git ? yek abzare ejaze mide shoma toye yek folder
modiriat konid , hamechio sabt konid
---> ejaze mdie shoma source codde ro az github vardari biayd tooye localeton 
branch bsazid -->shoro konid roosh kar krdn , vaghty tamom shod push konid
CTO , az github easy --> server

Option1 ------ az aval khdoet besazi folder
mkdir project
cd project
git init -->yekbar baraye hamsihe
miri file o ... karato --> CLI , ya mamoli [hameye inaro chon git init zdi moraghebeshe]
badan 
git status --> chia tooye alan , stage
git add file ---> tooye sataging [harchgh bkahy git add readme.md || git add file.py || ....]
git commit -m 'tozihat' -->sabt mishe
hameye ina ta inja --> tooye laptabet

miri rpeo misazi tooye github --> linkesho vrdmidari 
git remote origin ....   [vasl mikone khdoeto b oon ja]
git push origin --> hamechio az laptabet befrresi b oonja


hardafe kar mikoni
git pull origin (update mikone)
karato mikoni
git status
git add file || git addd ...
git commit -m 'tozihat'
git push origin (mifresti besamte github)



Option2 ------ REPO SKAHTE SHOD (Tleegram bot)
git clone https://// ---> folder misze
miri tosh [na git init , .....]
karato mikoni , felan file -->dasti
git pull origin (update)
git status
git add file change dadi | git add file ezafe
git commit -m 'tozihat'

git push origin (-->mifrste b samte github)




#-----Telegram_tutorial/
dakhele in folder kamel goftim chijori robote telegram besazim 
messsagehandler , commandhandler, callbackquery handler ,..... conversationhandler
--> topic dg monde -> bayad code zdn shoro bshe

[QUIZ ---> ta hafteye dg --> yek robot besazid -->harchi mikhad bashe]
1- b hich onvan dar 2 roze avale porozhaton az hoshe masnooe estefade nkonid [fght darsname]
2- enhance konid (ghavi trsh konid) --> gpt estefaxe konid
b khode man payam bdid , dakheel goroh payam bdid



badesh y jaalse mizarim --> oon bot english_bot.py takmil mikonim
--> github mizaramesh --> collaborate mifrsm

pwd  -->kojaeed
git clone https://githuhb.com/adrese oon telegram bot source code 
cd telegram_fanavari
git branch
* main -->yedone bsihtar nsi va main hast
git branch esmet 
masalan--> git branch ali-pilehvar
## az main -->hamechio mirize tooye shakhe 
git switch ali-pilehvar 


***hamishe mikhay bri too folderet
git branch 
branch haro miare ooni k * zade yani tooshi
git switch khodet


karato mikoni , feature ezafe konid , harkasi yechizi gofte mishe
rooye oon code kar koni , kole code tooye branchet dri
miri roosh shoro mikojni, file python do ta file kar mikoni

#---rozane
git switch branch
git status
#har file taghir dade 
git add 
git commit -m 'tozih'


git push origin branchet
git push origin ali-pilehvar
[github]

**ta gahble in
git push origiin --> git push origin main 



karet tamom shod --> mergesh mikonm



"""



#--------------------------------
#--------Python review
#--------Python Class
#--------Python Library

#bekham tavabe calcualtor ro begiram va use konam
#chijori behesh dastresi peyda konm??


#file haye .py --> 1-yek ja hastan
#AI.py --> user/apm/desktop/
#calcualtor.py -->user/apm/dekstop/fan/

'''

hamishe yeki yejaee hast
yejaee ma oon file haro run mikonim




CMD , bash , terminal [SHELL]--> 
miri [cd] hamonjae k hasan python ...file.py -->hamonja k hast
hamonja ham run mishe



IDE -->spyder o ....
file yeja hast 
run yeja dg --> [oon bala samte rast mibinish]

/Users/apm

man ag bkham b yek file i dastresi peyda konm inja

open()
file -->address
import krdn

bayad in ghazie havasemon bashe
'''


#tabey add ro az calculator vardaram
#kh moheme k spyder kojas? /user/apm 

#calcualtor /user/apm/desktop/fan


#IDE <---> system amel gahro ghati msihe

#from .desktop.fan.calcualtor import jam

#rahat tar ine ke beri oon bala samte rast taghir bdi 
#jaye run ro
from calculator import jam




#_--normal

#def jam(a,b)


#jam(a,b)




#------ 3 rah hast
#1-----
import calculator
#kole file ro miari inja

#vase dastresi b tavabe hash
calculator.jam(10,20) #Out[6]: 30


#2-------
from calculator import jam

jam(10,20)


from calcualtor import jam_zarb_tafrigh

jam_zarb_tafrigh(10,20)


jam_zarb_tafrigh()

jam_zarb_tafrigh()


jam_zarb_tafrigh()

jam_zarb_tafrigh()


#3--------
from calculator import jam_zarb_tafrigh as jzt

jzt(10,20,2,4) #Out[9]: 56



#----SPYDER KAR MIKONI

#-----FILE APPLICATION KAR MIKONI
#NIAZ DARI AZ YEK FILE B OON YEKI FILE ET IMPORT KONI
#VA HAMSHON ZIR MAJMOE YE HAM BERAN VA RUN SHAN

#django , .....

#tooye folderi k hasti --> .
#ag bkhay biay y folder aghab tar ..
#ag mikhay bri tooye folderi .esme_folder


#------
#PEDAR-----
        #myfolder
             #pesar
             #dokhtar
        #BROTHER
        
        #brother.py


#agar toye file myfolder chizi hast .py 

#from . import oon chizo

#from .pesar import oon chizo

#from ..brother import ....

#mohem nsi az koja run mishe 
#az desktop? az user and ...

#pedar filie k havie file myfolder hast
#m

#. hamoon khdoesh
#.esm -->fodlere tooye in fodlr
#.. biay brioon


#from felan import * -->hamechizo 
#jam()


#-----file importing------
#----ketabkhone??? hamone vali y khobi dare

#baraye nasbe yek ketabkhone ---> PIP  
#pip --> ham download mikone, install --> baes msihe
#tooye yek ghesmati az computere shoma
#zakhrie mikonatesh

#install -->yek kari mikoni harja esmesho bznid 
#peyda mikone folderaro



#snn/dose ta foldeerr / .py -->chayta function


#bayad bdonid foldere snn kojast
#import .....


#pip install snn

#snn globalabrta nasb mikone

#harja bodi from snn -->az hamoon foldere


'''

Ketabkhone

madules dare --> kole folder
tooye foldr koli foldere dg
tooye har foldr koli ,.py (script)

gotye har script , variable|functipn|class



az madar (ketabkhone) --> . --> . 
madule -->maduel -->file b fuile

brsim oon tabe ro bekeshim biroon

'''

#from sklearn.neural_network import MLPRegressor

'''

skleanr
|---------neural_network
|------------------MLPregressor() -->classs

'''

#from PyGamLab.structures.GAM_architectures import Graphene

'''
PyGamlab
|--------structures
          |------------GAM_Architectures
                          |---------------graphene.py
                                              |--class Graphene()
                                              
'''



#---------------------------------------
'''
ketabkhone ha vaghty nasb mishe 
version dare

_ . _ . _

adad chapie mohem trin adade-->version yan in
3 . . 
2 . .

yekodom version 3 , version 2
airpod 2 , 3 zamin ta asemon frgheshe
iphone 8 , x(10)



3.2
3.4 

feature --> 3.4 uyekseri feature dare k 3.2 nadare |oon featr=u kh kahs bahse hsoam donabelsh



3.4.1
3.4.2

bug fixing
3.4.2. -->yek buggi fix shode (rare ,nadeer hast k shoma asan on bugo)
recoommend mikonan agha akhariaro brizid


stabel version--> featur haye aslio dare
--> pip install mizani -->stabekl version ro barat nasb mikone

pip install pygamlab==1.7.0
pip install numpy==1.2.1


pip install numpy -->akahriaro nemide --> sytabel version
akahriaa

pip install numpy==
pip install numpy --upgrade

'''


'''
vaghyy mirizi 
ahr ketabkhone yek file dare bename
requirements.txt --> toosh yekseri ketabkhon

pip install oon ketabkhgone

aval mire tooye requirmeents --> oonaro  update mikone --> hadimi bekahd, hamon versioni k hastan
badesh ketabkhoen shomaro install mikone


moshkjeli peyda mishe --> sklearn -->  numpy==1.8.1 --> hosh masnoee
django ---> numpy == 1.1.1


laptab -->yedonas -->numpy == 1.1.1  | sklearn error
ya belax

mohemtarinaee k baham kar mikonan --> sklearn, numpy, pandas , django ,..
dota proozhe kh motwfavet

sale pish y proozhe zadi --> oonmoghe ooon chiza bode ketabkhone ag update koni 
yek tabe e toye 100 ta file --> oon hazf bshe, argument avaz bshe


---> MOHIT BESAZID DOOSTANE MAN

laptabo-->envrioenment taghsim mikonid



conda -->

GUI --> bazesh mikone --> environements --> new environment --> misazi [spyder,...]

CLI --> conda activate  --> env , vared bshid




conda , .... mohti besaazi


python -m venv esme_

python -m venv FANAVARI2021
in misaze mohito 


harmoghe har codi bekham ejra konm , ***PIP INSTALL

source FANAVARI2021/bin/activate



#kole laptabet

#mohit misazi
(base) apm@APMs-MacBook-Pro fan % python -m venv FANAVARI
(base) apm@APMs-MacBook-Pro fan % 

(base) apm@APMs-MacBook-Pro fan % ls
FANAVARI	__pycache__	calculator.py


(base) apm@APMs-MacBook-Pro FANAVARI % ls
bin		include		lib		pyvenv.cfg



#mohiteto faal mikonid
(base) apm@APMs-MacBook-Pro fan % pwd
/Users/apm/desktop/fan



(base) apm@APMs-MacBook-Pro fan % source FANAVARI/bin/activate 
(FANAVARI) (base) apm@APMs-MacBook-Pro fan % 



pip instal ,...





yek proozhe dari --> okeye
yek porozhe jadid -->
khoddet dari kar mikoni -=->
kole ketabkhone hato update ikoni

hame karam onjas
behesh dast nmiznm -->fgth baraye karam varedesh mishm

python ...py

ghablesh vared mohit shi




'''





'''

Mohit besazi --> AI26

(base) apm@APMs-MacBook-Pro ~ % pwd
/Users/apm


#yekbar -->bare aval-_>sakhgteshe
python -m venv AI26




#----
source AI26/bin/activate


pip install



1-- Numpy -->calcualtion

2--Scipy , Sympy --> calculation

3- Matplotlib --> rasm
    3.5. Seaborn --> jadid tari hast baraye rasm
    
4- Pandas --> data cleaning

5- Statistics , scipy --> amare

6- Sklearn --> machine learning

7- pytorch, tensorflow ---> deep learning

8 - sqlite , mysql --> database
 
9- fastapi ---> sohbat ikonm

10 - transformer --> huggging_face -->mdoel haro vared
(groq , ....) --> NLP modesl

11 - Opencv --> compuer vision --> binaee machine



****rule -->< yek darsname azina dahste bashim
*** rule2 --> inaro hey update konim baham --> hey miss shod bezarim
***rule 3 --> documentation bekhonim (farda y ketbakhone yad bgiri?)
*** rule4 --> haamro nabayd hefz konim --> mophemtrinar--> az estefade

'''













