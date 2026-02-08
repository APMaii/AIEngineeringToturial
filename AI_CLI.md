

# Command Line Interface (CLI)

In The Name of GOD
Created on Fri Feb  6 20:19:28 2026
**author:** Ali Pilehvar Meibody


----
##  GUI vs CLI

- **GUI** :Graphical User Interface [Rabete karbari geraphici]  -->Yani shekl dare mitoni bebini . You click buttons, folders, menus (Explorer, Finder).

- **CLI** --> Command Line Interface [Rabete karbari dastoori ]  --> Yani code bayad bzni (dastoor) You type commands to tell the computer what to do. *CLI --> Faster, Powerful*



----
## What is SHELL?

SHELL yek programm (barname) hast k mikhone command (dastoorateto)
read your command, Understand it , excutes it.
ma chand no SHELL darim , k baziash roye MacOS , Linux , Windows , .... hast

Example of SHELLS:
- bash 
- zsh
- fish 
- powershell
- CMD 


---
## Bash : Bourne Again Shell
yek shel default has k rooye linux hast. rooye
old default MacOS.  ,kheyli marooofe
Rooye Mac , Linux hast . 
Baraye windows --> bayad shoma Git Bash ro brizi ya WSL (Windows Subsystem for Linux) ro brizi 


Pas Yadet bashe, harmoghe shoma Terminal, ya har Shelli ro baz mikoni mesle bash --> Bash yek mohiti barat ijad mikone k to toosh COMMAND (dastoor)et ro bezani 
va khob SHELL mikhonatesh va ejrash mikone.
 B ch dard mikhore? --> Bejaye inke dasti kar koni rooye laptobet
dari miri zire WINDOWSET yani code mizni va karato mikoni

hala yek morori az code haye marooof

Harja hashtag didi jozvi az code nist balke tozih hast


-----  
-----
-----
-----

## **Dastoorate BASH**


#### Check Where you are

```bsh
pwd 
```


#### Liste chizaee k darid
```bsh
ls
```


#### Change directories
```bsh
cd folder_name  # move into folder
cd ..           # move up one folder
cd ~            # go to home
cd /            # go to root
```


#### Creates folders and files
```bsh
mkdir my_project      # make folder
touch file.txt        # make empty file
```
bejaye file.txt har no file e bekhay mitoni besazi .py .w .everything



####View file contents
```bsh
cat file.txt
```



#### Quite/exit Terminal
```bsh
exit
```



#### Copy files
```bsh
cp source_file destination_file    # Copy file
```
source_file-->oon file hast k darish
destination_file--> oon jaee k mikhay copy koni



#### Rename / Move 
```bsh
mv old_name.txt new_name.txt
mv file.txt folder/       # move file into folder
```
avali renamed mikone, dovomi move mikoni



#### Delete File
```bsh
rm file.txt
```


#### Delete Folder
```bsh
rm -r folder_name
```




#### File permission ( ADVANCED) need to be completed0----
```bsh
ls -l
```
------change permission------
```
chmod +x script.sh   # make file executable
chmod 644 file.txt    # set read/write permissions
```

-----
-----

PAS HAMONTOR KE MIDONID , ma kh dastoorat darim 
aksare chiz haee k didim ta laan dastoorat bash boodan ,
ama ma yekseri tool (YA CLI tool) darim k be ma komak mikonan
bazi az inha bydefault rooye laptobemon hastan va khob
mitonim azash estefasde konim

baziashonam mitonim download konim , koli CLI tool dar jahan vojod dare baraye hezxaran karborde motefavet


## General Classification
#=======================================================
#=======================================================
'''
Yek daste bandie khoob dashte bashim az dastoorat va tool ha

| Category        | Commands                    | Description |
|-----------------|-----------------------------|-------------|
| Navigation      | pwd, cd, ls                 | Check current directory, change directory, list directory |
| File Management | touch, mkdir, cp, mv, rm    | Create file, create directory, copy file, move file, delete file |
| Viewing Files   | cat, less, more             | View file content |
| Searching Text  | grep, find                  | Search for text in files |
| File Info       | file, wc, stat, du, df      | Get file information |
| System info     | whoami, uname, date, uptime | Get system information |
| Permission      | chmod, chown, chgrp         | Change file permissions |
| Compression     | tar, gzip, gunzip, zip, unzip | Compress and decompress files |
| Networking      | ping, curl, wget, ssh       | Ping a server, download files from the web, secure shell |
| Text editing    | nano, vi, vim               | Edit text files |
| Environment     | echo, export, env, alias    | Manage environment variables |

'''

----
----
----

## NAVIGATION --> pwd, cd , ls 



## File Management 


## Viewing Files


## Searching Text
* ? [] [! ]  EXAMPLES ...
SEARCH TEXT INSIDE FILES


## File Info


## System info

## permission

## compression


## Environemnt



----

## Text editing

review --> az jaee k midonid ma az jaee k hastim mitonim ba 'cd' harja
bekhaym berim , badesh mitonim ba 'mkdir' folder besazim
ba 'touch' mitonim file besazim va ba 'cat' mitonim file ro bebinim.

ama agar bekhaym taghir bedim niaz darim b yek abzari be name text editing, ma koli abzar haye mokhtalef darim hata abzar haye kh kh pichide ama dota az
maroof tairn haro inja migm k 
----
### **VIM**
Vim (Vi Improved) yek text editore ghavi hast rooye Unix/Linux system. and khob ma normal mode ta koli mdoe haye mokhtalef. 

kafie fek kon file e darim bename myfile.txt ya harchi .everything py harchi k hast

vaghty ino miznim
```bsh
vim myfile.txt
```

kole matnesh baz mishe baraye ma
harkari bekhaym bokonim hamashon dookme dare
```bsh
Vared kardane text --> Press i -->shoro b type kon
Esc --> barmigarde b normal mode
save file --> :w    [hatman do noghte ro bayad bznid]
quite --> :q
save and quit --> :wq
undo --> u
redo --> ctrl + r
cut --> x
copy --> y
paste --> p
search --> /pattern --> press n for next, N for previous
```

Khob ba in 'vim' dakheel shel har file ro shoma mitonid edit bezanid,

----
### **Nano**
ama hamchenann yek chize dg ham hast bename Nano k asoon tare
va baraye shoro ason tare.
```bsh
nano myfile.txt
Edit directly --> hamon lahze mitonid taghri bdid
Save file --> ctrl + o
quite --> ctrl + x
search --> ctrl + w
cut text --> ctrl + k
copy text --> ctrl + c
paste text --> ctrl + v
```

Ma hamchenin abzar haye kh kh pishrafte tar darim mesle
'Emacs , Micro , Joe , sed , Ex' va hamashon injorian
masanalan
micro file.txt

ama in abzar ha b soorate bydefault rooye shelle ma nistand
bayad nasbeshon konim
'

---
#### networking


#### ping
ma yek tool darim bename ping va shoma kafi ebenvisid
```bsh
ping google.com
``` 
ya har saite dg behetoon test mikone k aya HOST ghabele dastrese ya na
check connectivoty hast dar asl



#### lsof
```bsh
lsof -i 
```
in neshoon mide hame process haye rooye networke laptabetoon
```bsh
lsof -i :80 
```
--> in neshoon mide process haye rooye port 80 e laptabetoon



####Curl
in abzar baraye fetch data heyli khobe k bznid bgirid 

```bsh
curl http://example.com
```

masalan yek site hast k moshakahsate bitcoin ro mdie injori-->
```bsh
curl "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
javabi k migirid ine :

{"bitcoin":{"usd":68054}}%   
```


#### wget
in abzar baraye downlod file khobe , vaghty mikhayd yek seri abzar ro 
downlod konid bva ..

curl va wget besoorate bydefault rooye system ha hastand.




-----
-----
-----
-----
-----

# **CLI TOOLS**

ma yeseri dastoorate shell --> pwd , ls , cd , mv , cp , rm , touch, cat ,

abzarate mohem (tool) by default --> vim , nano, ping , curl , wget

1 milliard abzar dar jahan vojod dare
1000 abzare maroof --> berizimeshon

Non Default and Advanced CLI TOOLS

## ripgrep (rg)
Faster and smarter alternative to grep


##  jq-
For parsing JSON files.

## httpie
User-friendly HTTP client, easier than curl.
##  nmap
Advanced network scanning.

## htop
Interactive process viewer (better than top).


##  glances
Real-time system monitoring for CPU, RAM, disk, and network.


##  parallel
Run commands in parallel for faster batch processing.



## conda
nvironment and package manager (Python, R, and other languages).


## docker
Containerization tool. Run isolated applications or services with all dependencies.



## git
**in AI_GIT.md file shoma mitonid git ro bebinid**


## Poetry
Python dependency and project management tool (like Conda but lighter for Python-only projects)


## AWS CLI / Azure CLI / gcloud
Manage cloud resources directly from the terminal.



## Make / Task / Just-
Automation of repetitive tasks or pipelines


## Hugging Face CLI
# Login to Hugging Face
```bsh
huggingface-cli login
```

# Download a model
```bsh
transformers-cli download bert-base-uncased
```
# Push a model
```bsh
transformers-cli upload ./my_model --repo_id username/my_model
```




-----

## Command chaining

```bsh
mkdir test && cd test     # only cd if mkdir succeeds
echo "Hello" || echo "Failed"  # run second only if first fails
echo "Line 1"; echo "Line 2"   # always run both
```


-----

## Bash Scripting
