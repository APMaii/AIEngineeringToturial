"""
Created on Fri Jan 30 14:17:36 2026

@author: Ali Pilehvar Meibody


AI engineering

L1  ----> Github repo 






"""



'''




Programming ---> order to computer

Human (en) <-------Interface -----> Machine (0,1 binary)

Interface --> programming language (Python, C , C++)


tooye mokhafafashone , sorate trasnlation ()




Python ---> mohem tarin va por karbordtarin zaban hast


python --> vocab, grammar

oon developera k in zabano neveshtan reserved words

1----------- Python Built in Functions (narenji)
2-----------Python Keywords(banafsh)

3----------Python variables (sefid)
variable-->zarf --> moteghayer --> yek value dakhelesh zakhire mikone



'''

#3--------VARIABLE ---------
#1-Numbers

#int sahih 
ghad = 180

vazn = 80


#float --> ashari
vazn = 80.7362

#complex
mohandesi = 1j

'''

------------
| Type name |
| size value |
-------------

'''
a=10
b=30

#int a = 10

#a + b = c

#aval baayd yek ghesmat az memory khali koni 
#oon adada varedesh bshe

#***ma darmorede farghe memory , hafeze , ram , transistor, cpu, gpu
c = a + b


#------> amaliat
#() ** * / + -

c = a**10+20/4

c= ((a**10) + 20) / 4



#----moghayese
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)

#-->TRUE FALSE -->  boool

a=True
b= False

#----STR ------
#''
name = 'ali'

print(name)

#index --> 0

name[0]

#TypeError: 'str' object does not support item assignment
name[0]='b'


name='alipilehvarmeibody'

#akahrin adad excluded --> shamel nmishe
#range() []

#1 2 3
#:--->ta 
name[1:4] #'lip'
name[1:8:2]



#str functions hastan --> y kair mikone

#print()
#lower()


print(type(name)) #<class 'str'>


#class -->
name='ali'



class mystr:
    def __init__(self,value):
        self.value = value
    
    def lower(self):
        return 10
        
        
    def upper(self):
        pass
        
    def replace(self,old,new):
        pass
    
    
    def count(self,character):
        count_=0
        for char in self.value:
            if char == character:
                count_ = count_ + 1
                
        return count_
            
       
name = str('ali')


name = mystr('ali')    

name.count('a') #1







name = str('ali') 


class Bank:
    def __init__(self):
        pass
    
    def methods1(self):
        pass
    

obj1 = Bank()
obj1.methods1()



#str --> khodesh tabeh has taghir ijad nmikonan , khoroji midan
name='alipilehvarmeibody'

name.lower()

new = name.upper()


print(name) #alipilehvarmeibody


print(new)


'''

1- Taghir rooye khdo conversion

2- Adad mide

3- True Fallse

'''

name.upper()
name.lower()
name.title()
name.strip() #az chap va rast space ro hazf mikone
#zamani k yek user jolote va dare beht text mdie space chapo rashtesha zash joda bshe
name.replace('l','p')



#---aDAD
name.find('a') #--->indexe avalin a 
name.count('a') #mishmore


#true false

#is

name.islower()
name.isupper()

name.isalpha()
name.isnumeric()
name.isdigit()




#---Multipel Variables ---> baramon moheme
#list
#iterables --> iteration konid

a= list([10,20,30,40])

a=[10,20,30,40]


b=[10,10.6,True,'ali']


b[0]


b[0:2]


#str doesnt support item assignment

#list support item assignment

a[2]= 10000
print(a) #[10, 20, 10000, 40]



#function
a.insert(1,'ali')

a.append(40)


b=[10,20,30]



class mylist:
    
    def __init__(self,main):
        self.main = main
        
    def append(self,value):
        #self.main b tahehzs ezafe mikone
        pass
    
    def clear(self):
        self.main=[]
        
        #return nadare
        #Khode self.main ro taghir mide
        
        
    
    
#na jolosh zarf mizri na hichi-->khoroji ndre


#str function --> khoroji dare ama emal nmishe
#slist fucntion -->khoroji ndre ama emal mishe

a.extend(b)


#index
a.pop(0)
#value
a.remove('ali')


a.sort()

a.reverse()

a.clear() #pak nmikoen a --> a not --> a= []
del a
#print(a) #---> a is not defiend


#------.Iterables ---> multple values

#list -->ordered (index), changable, allow duplicated
#tupel --> ordered(index),,unchangable ( -->list taghiur->tuple) , allow duplciated
#set --> unordered (Index ndre),unchangable , doesnt allow duplicated



#tuple --> jaee estefade mishe --> az yja y datee safe bfrsi
#database --> 100 ta value () --> tuple --> k taghir nkonan
#y tabe dah ta kari roosh 

b=(10,20,30,40)

b[0]=1000
#TypeError: 'tuple' object does not support item assignment
#tuple===str 






#set --> duplicated bashe , nazmo --> adad majmoe ha 


c={10,20,30,40,40,40}
#error behet nmide 
print(c)
#{40, 10, 20, 30}


c[0]


#-----
#informational data , structural data

a=['ali',18,2000,'0440001199']

a[0]

a[1]

#a['name]

#dicrtionary -->

'''

list , tuple
index value
0       value0
1      
2
3



Set
value
10
20
30



dictiopnary
key    value
key1    value1
key2   value2

'''

d= {'name':'ali' ,  'sen':10 , 'pool':2000}


d['name'] #'ali'



d['name']='vahid'

#set -->nmishe tagir , indexi ndre k btoni bhsh dastrsi peyda koni


#tuple , str --> taghir pazir nistan item asignemnt ndrn

#list, dictionary --> item assignment mide

print(d)
#{'name': 'vahid', 'sen': 10, 'pool': 2000}


#key value ezafe

d['jadid']='value jadid'


print(d)
'''
{'name': 'vahid', 'sen': 10, 'pool': 2000, 'jadid': 'value jadid'}
'''



'''

DATAHAYE TOOYE DATABASE --->dictionary 
api --> application programming interface

backnd front -->data --> json -> dictionary


'''


#--------------
'''
1-Python built in functions
2-Pyuthon keywords
3-python variable <>

'''


#1----python built in fucntions
#reserved -->narenji , ....

print('salam')


#str pas mdie , conver  casting int()  float() 

a= input('salam esmet:')

#ina fght shabih sazie k fk konim gharare data az site begirim
#az user bgirim


'''
QUIZ 1 --->


github --> sakhtid
github --> git yad dadam

quiz1.py
quiz2.py


https://docs.python.org/3/library/functions.html


'''



#------------
#Pyuthon keywords
#zamani k shoam mikhay
#manteghe python in hast ke -->


#az bala b paeen miad va mikhone



'''

computer --->

--------------------------------------------------
|                                                |
|Hard  --> Memory(RAM) ---> Cache ---> CPU/GPU   |
--------------------------------------------------


HARD ---> technology cheap , konde ---> dataro zakhire kone
bargh bre , electricity --> inaro dare
write --> >> read
hamishegi oonjas --> 500 Gb   1 Tb

laptabo roshan mikoni

laptab (system  physici dare hardware) --> windows (macOS, microsoft,linux) --->softwares 

software --> dataee k niaz dare az hard -->memoruy RAM

Random access memory (RAM)--> expensive --> 2 Gb , 4 , 8, 16 

hame kara inja ram --> dataro negah mdiare -->sopratesh ziade --> kh kh kh 



cpu --> transistor (1,0 ) -->mohasbee krdn -->kar emohassbe cpu (GPU)
cpu --> core -->haste dare movazi anjam bdn --> 5 ta akr koni
gpu --> 1000 kare kochike movazi --> graphic, bazi , AI processing
cpu --> computation 

cpu/gpu --> parzadeshe

ram <----> cpu/gpu


hard <---->cpu/gpu

hard ----> ram ---> cpu/gpu
ram --> cache kb --> cpu/gpu
von neumann memari ishon


ram --> khamosh bshe mipare

a=10 , b=20 , c=40 ---> ram dare zakhire mishe --> cpu 



hardware ---> OS ---> software (spyder) --> codeto 

run  --> spyder --> firewall os --> binary --> ejra transsitor ha


software --->
az bala b paeen kaht b khat mikhone

gahi mikhayn in logic ro taghir bdid

--->keywords -->banafsh



if ---> sharti

'''

a=10 #20 #5
print('salam')

'''

if shart:
    dastoor
    dastoorat
    
    
Shart -->True false




if shart or shart2:
    ...
    
    
if shart and shart2:
    ....
    
    
    
or --> hadeaghal yeki az shart ha ag  in shart --Ya-- oon shart
and --> hatman joftesh --> sharte 1 ---VA---sharte 2 -->true bshe

'''

if a>10:
    print('salam')
    b=10
    c=b+40
    
    
'''

Shart ha 3 no

1-Just if

faghat yek if --->
rahzane --> onae k Truye shgoodan (shart)-->felan karo konan
oinae k nashodan rad mishan



        shart
     ___________
     True      False
     kare1




IF , ESLE --->dorahi
ag oonae k true shdoan -->kare1
onae k false shdoan -->kare2



        shart
     ___________
     True      False
     kare1     kare2



if lse elif --> dorahi haye to dar tooo


    shart
___________
True      False
kare1     |
         shart2
        ___________

      True      False
      kare2     kare3
         

performance


'''


#code compile beshe
#code run bshe


a=30

if a>20:
    print('salam')
    
    
if a<20 and a>10:
    print('hi')
    
if a<10:
    print('bye')



#-----
if a>20:
    print('salam')
elif a>10:
    print('hi')
else:
    print('bye')





#-------Halgeh ha

#---> While ,For

'''

for shoamrande in baze ee darim:
    dastoor ,\
        dastorati
        
'''

#for j#
#for esm
#for k


for i in  [1,2,3,4,5,6]:
    print('salam')
    
'''
i-->1 ta 6 -->salam ro ejra mikone

i=1 ---->print(salam)
i=2---->print(salan)


i=6

salam
salam
salam
salam
salam
salam
'''

#range-->

for i in  range(0,7):
    print('salam')

'''
salam
salam
salam
salam
salam
salam
salam

'''

#static for


#dynamic for

for i in range(0,7):  
    print(i)

'''
0
1
2
3
4
5
6

'''



#iteration

mylist2=['ali','vahid','hamid']

for name in mylist2:
    print(name)

'''
ali
vahid
hamid

'''


#10 ta mdoele hsohe masnoee
#20 ta score 

#mikhaym brim toosh check koni

#for --> if 


#---


mylist2=['ali','vahid','hamid']

for name in mylist2:
    if name[0]=='a':  
        print(name)



mylist2=['ali','vahid','hamid']
count=0
for name in mylist2:
    if name[0]=='a':  
        #print(name)
        count = count+1


print(count) #1




mylist2=['ali','vahid','hamid']
newlist=[]
for name in mylist2:
    if name[0]=='a':  
        #print(name)
        #count = count+1
        newlist.append(name)


print(newlist) #['ali']






'''

for i in range(start,end,step):
    dastooor
    
    
    
    
i=start
while i<end:
    dastooor
    i=i+step




'''

for i in range(0,10,1):
    print('salam')



'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
'''




i=0
while i <10:
    print('salam')
    i=i+1

'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam

'''

while True:
    print('salam....')
    answer=input('dsdddsd:')
    #kharej shodan
    #termination
    if answer=='exit':
        break


#pass --> jaye khali bzari, function , for ,...

#continiue --> mipare mire bade

#break ---> mishkone





#--------------------------
#monolothic , psudocode -->az bal abenevis bia paeen

#repeat , encapsulation, microdesign 

#tabdil konim yek code monolothic --> 
#FUNCTIONS ---->
'''

Input ----> function ----> OUtput





defintion -->misazish
call ---> azash estefade mikone



def name(arg,):
    body
    khoroji dashte bashe ndashte
    
    
    
    
'''

#nokte -->baarye yek tabe fght body moheme na vorodi na khoroji

#na khoroji na vorodi


def welcome():
    print('salam')


welcome() #salam

#khorojii  != Print


zarf = welcome()

print(zarf) #None




#---khoroji dre vorodi

def pi():
    return 3.14


zarf = pi()
print(zarf) #3.14




#vorodi dare, khoroji ndre


def jam(a,b):
    c = a+b
    print(c)


jam(10,20) #30


zarf = jam(10,20) #30

print(zarf) #None




#mohemtrin-->ham vorodi ham khoroji

def jam(a,b):
    c= a+b
    return c


zarf = jam(10,20)
    
    
'''

oon ghesmate def -->run -->chizi etefagh nmiofte
a=10
in sakhtar ro mire va zakhir emikone

call --> moheme jeraye vaghei onjas


zarf = 

mire tooye memory --> yejaro 

esm , size , ...  --> zakhrie kone

jam --> variable , def ,-->jam is not defined
ag dasht --> dota vrodoi

kamtar bedi -->miss
bishtar bdi --> 3 were given


a=10
b=20
c= 10 + 20 = 30
return 30 




zarf = ...
zarf = 30

LOCAL VARIABLE
a , b , c -->sakhte nashode bodn --> ino pak mikone 

ag az gahdim sakhte shode bodn -->

'''
    
    
    
print(z)    
#NameError: name 'z' is not defined



def jam(z,y):
    x = z + y 
    return x
    
    
#z = 10   
zarf = jam(10,20)    
print(zarf) #30


print(x) #NameError: name 'x' is not defined
print(y) #NameError: name 'y' is not defined
print(z) #NameError: name 'z' is not defined




a=10000000

b=200000000


def jam(a,b):
    c = a +b
    return c


zarf  = jam(10,20)
    
print(zarf) #30

print(a) #10000000




#globalesh koni localeto

a=10000000

b=200000000


def jam(a,b):
    global c
    c= a +b
    return c


zarf  = jam(10,20)


#ina asan bedard nemikhore --> concepte 



#-----------------
#arguments ---->
#argument



def jam(a,b):
    c = a + b
    return c

#ppositional arguments
jam(10,20)


#keywrod arguments
jam(a=10,b=20)



#-------------
#* -->harchi badesh biad --> keywordi mishe
def jam(*,a,b):
    c = a + b
    return c
jam(10,20) #in kar nmikone
jam(a=10,b=20) #In kar mikone



def jam(a,b,/):
    c = a + b
    return c
jam(a=10,b=20)
jam(10,20)



#---default

def jam(a,b):
    c = a+b
    return c


jam(10) #TypeError: jam() missing 1 required positional argument: 'b'





def jam(a,b=20):
    c = a+b
    return c


jam(10,5) #b hamon adadi k too call estefade shode

jam(10)  #pishafrz b --.erro dg nmide



#*** noketey kh mohem ine ke -->hatman default argument ha bayad bad az baghie tarif bshn


def jam(a=10,b):
    c = a+b
    return c

#SyntaxError: non-default argument follows default argument





#---->multiple input, multiple output ham dari


def zarbjam(a,b):
    c=a+b
    d=a*b
    return c,d


zarbjam(10,20)
#30 , 200


zarf = zarbjam(10,20)
print(zarf) #print(zarf)

print(type(zarf)) #<class 'tuple'>

k= zarf[0]

l = zarf[1]




#zarf = zarbjam(10,20)

k , l = zarbjam(10,20)

k,l,t = zarbjam(10,20) #ValueError: not enough values to unpack (expected 3, got 2)


#malom nis sabe nis , static arguemnts -->dynamic arguemnts


#positional dynamic arguments

#def jam(*arg)


#def jam(a,b,c,d,,.....)
#a -->
def jam(*a):
    print(a)
    print(type(a))

#(10, 20, 30, 40, 50, 60)
#<class 'tuple'>


jam(10,20,30,40,50,60)





def jam(*b):
    
    miangin = sum(b)/len(b)
    
    print(miangin)


jam(10,20,30,40,50,60,70,80,90,100) #55.0


def jam(*b):
    miangin = sum(b)/len(b)
    
    new = b[0]
    #b[1]
    
    final = miangin - new
    
    print(final)
    


jam(10,20,30,40,50,60,70) #30.0






#keywords dynamic arguments
#def name(**kwarg)

def jam(**k):
    print(k)
    print(type(k))

'''
{'a': 10, 'b': 20, 'c': 30}
<class 'dict'>
'''
    
    
    
jam(a=10,b=20,c=30)




def jam(**infomarion):   
    sen = infomarion['sen']
    ghad = infomarion['ghad']
    print(sen/ghad)
 

jam(sen = 20 , ghad = 180 , esm = 'ali',tasob = 'tasob')
    
 
#0.1111111111111111
 
    

'''
@proprty 
tozih ..............

mesal bznan 
chika mikone


@classmethod



@staticmethod



'''







'''
#-------------
REVIEW PYTHON ------> BARAYE SHORO
Python built in functions ---> link --> berid ino quiz1.py -->tak take tabe haro y test bznid

REVIEW FUNCTIONS 


REVIEW CLASSS
private variables __variable --> negahe mojadade 

decorators --> property , classmethod, staticmethod --> motale e beshe


JALASE --->
Ketabkhane ha , Github , GIT , Numpy ro baham dg shoro mikonim 

'''







