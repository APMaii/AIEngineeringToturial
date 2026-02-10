'''

ta zamani k minevisi python file 

ta zaman k laptabet roshane , ro rune , bot runee 
[TEST]


[PRODUCTION] YESAL

--> SERVER --> Rooye server run konim


Farspack,.... --> 1 G RAM , 2 G ram --> Linux (ubuntu , debian)
kharj az keshavr --> Linode , 

kharid k mikonid (ejare mikonid) ---> IP , password

vared shid --> Terminal 

barname downlaod konid --> Terminus , Putty , ....
az laptabe khdoeton  b server vasl shid

ip , password 

miri too terminus --> Ip , passwordeton mizani vavasl mishi behesh




mirim ip ro miznim , label esm mziarim , useer : root , password : ... vasl mishim
ye safe siahe --> server hamine

kojaeeM/
root@localhost:~# pwd
/root
root@localhost:~# cd /
root@localhost:/# pwd
/
root@localhost:/# ls
bin   dev  home  lib32  libx32      media  opt   root  sbin  srv  tmp  var
boot  etc  lib   lib64  lost+found  mnt    proc  run   snap  sys  usr
root@localhost:/# cd root
root@localhost:~# ls




tamame dastorate --> sudo 
#----ino run konm
aval bayad udpate konid


sudo apt update



mkdir telegram_bot
cd telegram_bot

#ino instal mikone ejaze mide man yek mohit besaazam
apt install python3.10-venv



#
python3 -m venv TEL


root@localhost:~/telegram_bot# ls
TEL
root@localhost:~/telegram_bot# source TEL/bin/activate
(TEL) root@localhost:~/telegram_bot# 

#------

(TEL) root@localhost:~/telegram_bot# touch bot.py
(TEL) root@localhost:~/telegram_bot# vim bot.py
(TEL) root@localhost:~/telegram_bot# ls
bot.py  TEL
(TEL) root@localhost:~/telegram_bot# vim .env
(TEL) root@localhost:~/telegram_bot# ls
bot.py  TEL
(TEL) root@localhost:~/telegram_bot# cat .env
TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
(TEL) root@localhost:~/telegram_bot# python bot.py
Traceback (most recent call last):
  File "/root/telegram_bot/bot.py", line 1, in <module>
    from telegram.ext import Application
ModuleNotFoundError: No module named 'telegram'
(TEL) root@localhost:~/telegram_bot# pip install python-telegram-bot
(TEL) root@localhost:~/telegram_bot# pip install python-dotenv
#-----


agar az serveer baiyd biron mese laptabeton --: inam baste msihe



tmux --> yek abzare

sudo apt install tmux



'''
