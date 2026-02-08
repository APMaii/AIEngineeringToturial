"""
In The name of god
Created on Fri Feb  6 16:18:52 2026
@author: Ali Pilehvar Meibody

Aval ye negah be AI_CLI.py bendazid ke bebinid Bash chie , Cli chie
chijoori mishe bedone GUI , harkari bekhaym ro ba CLI bokonim.
emrooz mikhaym darmorede in se ta topic harf bznim
1-GIT
2-GITHUB
3-GITLAB
baham motefavet hast
"""

#=======================================================
#=======================================================
'''
			             1-GIT	 
'''
'''
wifi ghate ..... local (machine) computer laptob ro fght darid
FOLDER DARI
.py 
.txt
.md 
haroz dari taghir midi , bad az yemah migi ey kash
man ychi dashtam k 1-aval migof ch zamani , kodom fiel skahyte shode
ch zamani tahghid dade shod , kojahash taghir dade shode
ki taghiur dade (team) , ey kaah noti bod -taghiri
control konam folder , files
version control = control versioning
1-Nazm
2-Harmogeh khasi mitoni b har step bargardi
3-befahmi ki taghir dad, chi taghir dade ahode (bugg)
4-tozihi kash bood (description)

age tooye AI_CLI.py yadetoon biad ma yekserii CLI tool dashtim ke
default boodan mesle vim (k mizasht edit bezanim )
hala yekseri darim bayad download konim --> yeki azina git hast

--> TOOL (abzar) ---> git
ejaze mide shoma control bversioning
control koni folder , fil hato

hadaf -->
folder sakhti, file sakhti
1-bege ki hasti va 
2-ch file ch zamani dari misazi k taghir midi
3-paye har taghirt tozih bnvis 
4-hameye ina jam bshan kenare ham
5- betoone inaro bargardi (step back)

Linus Trovalds --> ABAR ENSAN
3 rooz --> GIT Misaze
'''


'''
------> MOSHKEL CHIE???
man koli file daram , directory (folder) va hey misazam , edit mizanam , hazf mikonam

File ha sakhte mishe
file ha edit mishe
file ha hazf mishe
mikham har kari k krdm sabt bshe --> sabteshon konm
-->1- nazm daram
-->2- midonm key chikar krdm
--->3- hamashon zakhrian , harmoghe khastam b se rooz pish
---> 4.......

ye nafarim , yechizi , y toooli , abzari --> nezarat kone
rooye kole laptab?? na
ye foldero neshon mikonm -> aghaye x ino moraghebesh bash (nexzarat kon)
abzar --> git 
Linus Trovalds
-->systemam ---> bASH --> AI_CLI.py  cd pwd topuch ,.... | vel kon
abzari --> git --> dare laptabam? na

--------- INSTALL GIT---------
WINDOWS --> https://git-scm.com  (default option) Git bash(terminal) --> SHELL (siah)  | abzare git
macos --> terminal (bash) --> brew install git
Linux --> Terminus,.,..(bash) ---> sudo apt install git

---------Bad az install Git---------
windows, macos, linux --> SHELL --> git mishnase 

bad az inke install krdid, Shell ro baz mikonid
MAC , LINUX --> Terminal
windows --> GIT BASH

yek safe siahe --> in safe siah hamoon SHELL hast k dakhele AI_CLI.py goftim k chie .


baraye inke motmaen beshim k git ro darim bayad in ro bznim
git --version  

error nadad --> rahat nasb shdoe



Git -> niaz dare bedoen sahebe laptab kie , author (nevisande kie)


#harchi k doos dari
git config --global user.name 'Ali Pilehvar'
git config --global user.email 'ali@gmail.com'

#behtre baraye compatibility --> hamon emaili bashe k github bahash hesab baz krdi


bekhay bbini configat chie
git config --global --list



Hala fek kon ma yek folder misazim 
mkdir my_project
cd my_porject


masalan vaghty terminal baz mikoni hamchin chizi mibini
(base) apm@APMs-MacBook-Pro 
yani tooye (base) hasti na hich environemnti 
apm esmete o rooye laptobet hast

mijkhaym brim desktop kafie benvisim
(base) apm@APMs-MacBook-Pro cd desktop

bad mibini k rafte tooye desktop -->
(base) apm@APMs-MacBook-Pro desktop % 
#in yani tooye desktop hast 

-------------------------------------------
#yek folder misazim 
(base) apm@APMs-MacBook-Pro desktop % mkdir ai_engineering_test

#badesh varedesh mishim 
(base) apm@APMs-MacBook-Pro desktop % cd ai_engineering_test
(base) apm@APMs-MacBook-Pro ai_engineering_test % 
-------------------------------------------

bad az macbook-pro neveshte esme file ro yani alan injaeem.



in fodler va harchi tooshe, zire nazare git nist.
git mesle yek nazer hast va tahte nazar migire file haye dakhele yek fodlero
ama ghabl az inke dar nazar begire bayad behesh begim k boro
felan folder ro tahte nazar bgir
khob ba cd my_project raftim tooye folderemon va bad command zir ro miznim
git init 


mige manam hastam --> oon foldereto tahte nazar gharare mide

-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git init
Initialized empty Git repository in /Users/apm/Desktop/ai_engineering_test/.git/
-------------------------------------------



kole Git yek kari bayad bokonid .
alan ----> add staging  ----> commit final


Yani chi? yani fil skahti, pak krdi, chizi ezafe krid bayad
hamashon ro sabt koni zir nazare git va begi agha man felan roz
felan karo krdm va dalilesho bnvisi 
vase inkar. shoma taghirateto midi , mibarish tooye 'stage' --> yek marhale
ghabl az taeed nahaeie, badesh mibarish taeed nahaee k esmesh hast
commit.




baraye inke bbini chia tooye 'alan' vojod dare , stage , unstage
az dastoore --> git status --> estefade mikoni
(mibinm too 'alan' , 'stage')

-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
-------------------------------------------



Choon folderemon khalie in dare bema mige hichi 
too branchemon nis, hichi commit nashode




Khob ma miaym ba dastoore 
touch readme.md
touch salam.txt

dota file e khali misazim.



hala ag get sttus bezanim bbinim chekhaabr
-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	matn.txt
	readme.md

nothing added to commit but untracked files present (use "git add" to track)
-------------------------------------------
in yani dota file skahte ama track nashdoe, yani 
yadet biad ino -->
alan ---> stage --> commit
khob yani file matn.txt , readme.md tooye 'alan' hastan
bayad bebarim tooye stage

ba dastoore git add in karo mikonim

-------------------------------------------
#matn.txt --> endakhtam tooye staging (ytek marhale ghabl az sabte nahaee)
(base) apm@APMs-MacBook-Pro ai_engineering_test % git add matn.txt
-------------------------------------------


hala badesh status migirim bebinim chekhaabre




-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   matn.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	readme.md
-------------------------------------------

mifahmim k readme.md tooye 'alan' hastan va stage nashode
ama 'matn.txt' tooye stage hast.


hala k matn.txt tooye stage hast , bayad bbrimesh commit nahaee 
injas k tozih minevisi

-------------------------------------------
git commit -m 'toziheto inja benevsi'
-------------------------------------------


hala age status begirim mibinim file e matn.txt dg nist (yani commit shod tamom shod)

hala brim file readme.md k tooye 'alan' hast ro 'stage' badesh 'commit' konim


#tooye staging
git add readme.md

#inkar commit mikone
git commit -m 'toziheto inja benevsi'




#-----HALA BERIM TAGHIR BEDIM BEBINIM CHEKAHABRE
yademon bashe ma kojaem? tooye foldere AI_engineering_test hastim

(base) apm@APMs-MacBook-Pro ai_engineering_test % ls
matn.txt	readme.md


hala fek kon asan dasti mirim yek file .py python misazim
kgob untracked hast yani tooye amrhale 'alan' hast

-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	myfile.py
-------------------------------------------

dobare bayad bbrimesh 'stage' badesh 'commit' konim
git add myfile.py
git commit -m 'man yek file python sakhtam'




hala fek kon bazesh mikonim file myfile.py va mirim yek function
jadid misazim toosh be esme welcome() hala age status begirim mibinim
k bale taghir krde


-------------------------------------------
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   myfile.py

no changes added to commit (use "git add" and/or "git commit -a")
-------------------------------------------

har taghir ,sakht --> sabt bshe (tozih) -->commit koni

--> add staging --> commit (description)

git status --> git add --> git commit -m 'tozih'







Kholase ee az kole kari k krdim -->
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   myfile.py

(base) apm@APMs-MacBook-Pro ai_engineering_test % git commit -m 'man yek file python sakhtam'
[main 83c49ed] man yek file python sakhtam
 1 file changed, 10 insertions(+)
 create mode 100644 myfile.py
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   myfile.py

no changes added to commit (use "git add" and/or "git commit -a")
(base) apm@APMs-MacBook-Pro ai_engineering_test % git add myfile.py
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   myfile.py

(base) apm@APMs-MacBook-Pro ai_engineering_test % git commit -m 'function welcome ra sakhte am'
[main 2a77dc2] function welcome ra sakhte am
 1 file changed, 3 insertions(+)
(base) apm@APMs-MacBook-Pro ai_engineering_test % git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   myfile.py

no changes added to commit (use "git add" and/or "git commit -a")
(base) apm@APMs-MacBook-Pro ai_engineering_test % git add myfile.py
(base) apm@APMs-MacBook-Pro ai_engineering_test % git commit -m 'tabeye goodbye nevshte shod'
[main d83401e] tabeye goodbye nevshte shod
 1 file changed, 6 insertions(+), 1 deletion(-)
(base) apm@APMs-MacBook-Pro ai_engineering_test % 






baraye bargardoondane yek file az satge too halate adi

git restore --staged esme_file




gahan bejaye inke chant achant bznim mitonim az dot (.) estefade konim


bejaye

git add new1.py
git add new2.py

mitonim bnvisim
git add . 
#in hamaro 



#restore
git restore --staged new1.py
git restore --staged new2.py


git restore --staged . 




'''


'''

#---
git log

tamame commit hato miare

#5 ta loge akahr
git log -5



git log --author="yourname"



git log app.py



#git diff

#git 



'''
#===========================================
#===========================================
#2- Git Hub--------
#===========================================
#===========================================


'''
git ---> linus trovalds
github --> microsoft


github --> hub baraye git haa



to mitoni manage koni ba abzare git --> dakhele laptabeto

man mikham barnamam besoorate msohakahs (foldar)
beyne hamebashe

man , dostam , felani ,.....

center mikhaym --> source of true

hub 
git hub --> hubi hast baraye git haye shoma


account darim 
vaghtyy miri repo new mizni , 

'''



'''



OPTION1 -------------
yek folder tooye laptabet sakhti, hala mikhagy vaslesh koni b github


ma ta alan yek chizi too local sakhtim

(base) apm@APMs-MacBook-Pro fanavari2026 % ls        
myprogram.py	new2.py		newprogram.py	newwwwwww.py



miri dkahele github mishi , ye repo misazi (github)



git branch -M main

git remote add origin https://github.com/APMaii/fanavari2026.git




Usernam  --> esmi dari 
Password --> ? ERROR


-->khob goosh bde

[dakhele telegram ferestade shod] ---> Token


passsword  --> token 


anjam mide 

**in yekbar hast 


git config --global credential.helper manager

or

git config --global credential.helper store 




koli commit kardam??? --> locale khodam 


####git push origin    [git harchi commit kardam ro origin()]
git push -u origin main
OPTION2------------
SHoma yek folder repo too github hast , mikjhay bgirish , hala mikhay vasl shi b oon




************88
======RAHANMAYE DEVELOPER HA======
harchi uypdate hast az github miad roo local (laptabet)
git pull origin  



miri code mizni
git status -->mibini
git add
git commit


commit? --> local (laptab)
10 ta ciommit, 100 ta commit
shab k shod karet k tamoom shod

git pull origin (harchi hast biad)
git push origin main
mire too github




MESAL---
(base) apm@APMs-MacBook-Pro fanavari2026 % git pull origin
Already up to date.
(base) apm@APMs-MacBook-Pro fanavari2026 % touch alipm.py
(base) apm@APMs-MacBook-Pro fanavari2026 % vim alipm.py
(base) apm@APMs-MacBook-Pro fanavari2026 % touch alipm2.py
(base) apm@APMs-MacBook-Pro fanavari2026 % touch alipm3.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	alipm.py
	alipm2.py
	alipm3.py
	newwwwwww.py

nothing added to commit but untracked files present (use "git add" to track)
(base) apm@APMs-MacBook-Pro fanavari2026 % git add alipm.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git commit -m 'man file salam ro sakhtam'
[main 519039a] man file salam ro sakhtam
 1 file changed, 3 insertions(+)
 create mode 100644 alipm.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	alipm2.py
	alipm3.py
	newwwwwww.py

nothing added to commit but untracked files present (use "git add" to track)
(base) apm@APMs-MacBook-Pro fanavari2026 % git add alipm2.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git add alipm3.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   alipm2.py
	new file:   alipm3.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	newwwwwww.py

(base) apm@APMs-MacBook-Pro fanavari2026 % git commit -m 'file haye 2,3 sakhte shod'
[main 8359be9] file haye 2,3 sakhte shod
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 alipm2.py
 create mode 100644 alipm3.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git add newwwwwww.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git commit -m 'news ra skahte am'
[main 3f38ffa] news ra skahte am
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 newwwwwww.py
(base) apm@APMs-MacBook-Pro fanavari2026 % git pull origin 
Already up to date.
(base) apm@APMs-MacBook-Pro fanavari2026 % git push origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 10 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 809 bytes | 809.00 KiB/s, done.
Total 8 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/APMaii/fanavari2026.git
   8970035..3f38ffa  main -> main







----OPTION2-------
zamani hast k code hast , mikhaysh biarish too lcoalet
(zamani k code sherkate) khode githube

git clone https://github.com/APMaii/AIEngineeringToturial.git

public bashe mitoni download koni 

private bashe 
user passs 


na git init mikhjay (khorde) -->inite 


(base) apm@APMs-MacBook-Pro AIEngineeringToturial % git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


(base) apm@APMs-MacBook-Pro AIEngineeringToturial % touch test2.py
(base) apm@APMs-MacBook-Pro AIEngineeringToturial % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	test2.py

nothing added to commit but untracked files present (use "git add" to track)
(base) apm@APMs-MacBook-Pro AIEngineeringToturial % git add test2.py 
(base) apm@APMs-MacBook-Pro AIEngineeringToturial % git commit -m 'teste 2'
[main 96b85da] teste 2
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test2.py
(base) apm@APMs-MacBook-Pro AIEngineeringToturial % git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 10 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 281 bytes | 281.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object
To https://github.com/APMaii/AIEngineeringToturial.git
   c958dec..96b85da  main -> main






'''



#--3-GITLAB--------




'''
Aval rajebe khode git o ina…….
Badesh rajebe github chi bod chi nabood 
git clone https://github.com/OWNER/REPO.git
Vaghty password mikhad 0- token based migiri va hamchning

Store plain text
git config --global credential.helper store 

git config --global credential.helper manager


#------
Badesh k skahtim tamom
1-	Aval dari bad mikhay vasl koni
Remote

2-	Darish asan hamono migiri push pull mikoni Rahat




git branch

git branch feature-login


git checkout feature-login
OR 
git switch feature-login
git push -u origin feature-login



git push –all

git merge feature-x





'''




