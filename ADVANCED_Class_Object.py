
"""

In God  we trust

ADVANCED_Class_Object.py


Created on Fri Feb  6 16:13:37 2026

@author: Ali Pilehvar Meibody




------AI Engineering--------
------L2--------


#---------------------------
Telegram --> MATALEB --> Github profile --> Linkesh profile 
--> collaboration ---> GITHUB REPOSITORY dashte bashim
--> yechizie ke Ai_Fanavari_2026

.py -->
Topic -->
01_Python_reviw.py
02_class_advanced.py
02_numpy.py
03_pandas.py



-->Guidline --> local (laptob)
gpt , documentation, source --> 

#============== Topic section

#------------ subsection



#------ REPO SHAKLHSI MISAZID --> AI_Engineering_Tutorial or Notes
Quiz , tamrin , felan lectyre --> kholasasho 
harchizi doos dahstid
COllaborate @APMaii







#----------------- ZABAN ENGLISI TOO TELEGRAM ---------
Jalase Extra --> TELEGRAM BOT --> yad mdiam chijori ye teolegram bot besazid

hadafe asli --> telegram bot --> bache ha bain sabte nam konan --> profile bsazan 
esm , password


harki har hafte molzame ke --> 5 ta kaalme englisi mortabet ba zabane barname nevisi 
varede telgram bot 

--> [input]  [output] [randomzie]  [question,]

[input]----> 5 ta mifresi (agar tekrari bashe, tekrari) 5 tat tmaom shod mige daskhosh
[output] --> fiel exel, pdf ,...--> az tamame kalamtei k jamavari shode behet mide 

Admincore --> har hafte chan nafar karo krdn -->



hadafe dovom --> 



server ---> hazine dare , linux bazi, GUI , appo , nginx , .....

telegram bot --> codi function hato --> bastari mese bot 
GUI (graphical user interface )
Robot 
Test unit hesab --> IDEA ---> testesh kon-->hal mide --> yechizi misazi
REAL misazi





#-----------------------------------------------------

***L1 ---> Review on all python related topics
variables, functions, class 


**L2 ----> 

"""

#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================

#local hastan --> nemitoni az in fucntion b oon fucntion bri

#class object oriented ---> OOP -->mohemtain ghesmate programming

#c++ ---> c ----> OOP support class object

#az yekchizi class --> too delesh yekseri adad , yekseri method

'''


hoshe masnooe, machine learning --> model ha --> az ye ravehsi mian
rabete haro besorate amari yad migiran

riaziat, pichidas, kh kh pichidas ,....

mano shoma vghti mikhay estefade konim

Modele hoshe masnooee --> tabe nis -->class

model = MODEL(()))
    
    
model.tabe1()

model.train()

model.optimzie9)
    
model.predict()

model.accuracy()



'''


#def bank(vorodi)




#class --> vorodi haro --> __init__
class BANK:
    #BANK(vorodi chi bdi)
    def __init__(self,name,sen):
        pass
    
    

#object misazi az yek class

#object chia dare ? 1-Varibales 2- methods (function)

obj1 = BANK('ali',18)


obj1.name #AttributeError: 'BANK' object has no attribute 'name'


#kole class --> SELF ---> khodash --> harchi k gharare interfac bshe
#moshtarek besh ebeyne tabe
#gahrare beyen objecti k misazi , tabe ha
#tak take in datsan 0--> self hast in haro mesle yek reshte beha vasl mikone


class BANK:
    def __init__(self,name,age):
        self.name = name
        self.age = age



obj1 = BANK('ali',18)


obj1.name #Out[116]: 'ali'

obj1.age #Out[117]: 18





class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen):
        
        self.name = nam
        self.age = sen

BANK('ali',18)
obj1 = BANK(nam='ali',sen=18)

#man too self sakhtam
obj1.name #Out[120]: 'ali'

obj1.age #Out[121]: 18

obj1.sen #AttributeError: 'BANK' object has no attribute 'sen'

#1-----Attributes , Variables --> moteghayed ha

#obj.esm



#2-----Methods ,, fucntions

class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen):
        
        self.name = nam
        self.age = sen
        
        
    def welcome(self):
        print('salam')


obj1 = BANK(nam='ali',sen=18)


obj1.welcome() #salam





class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen):
        
        self.name = nam
        self.age = sen
        
        
    def welcome(self):
        print(f'salam {self.name}')
        
        

obj1 = BANK(nam='ali',sen=18)
obj2 = BANK(nam='vahid',sen=18)


obj1.welcome() #salam ali
obj2.welcome() #salam vahid



obj1.name # 'ali'


obj1.name = 'reza'


obj1.name # 'reza'





#---------------------------------------------
#internal variable -->dakheli



class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen,initial_balance):
        
        self.name = nam
        self.age = sen
        self.balance = initial_balance
        self.ATM_fee= 100
        
        
    def welcome(self):
        print(f'salam {self.name}')
        
    def show_balance(self):
        print(self.balance)
        
        
    def ATM(self,amount):
        self.balance = self.balance - amount - self.ATM_fee
        
        
a1=BANK('ali',18,2000)

a1.ATM(200)
         
a1.show_balance() #1700

a1.ATM_fee =0

a1.ATM(200)

a1.show_balance()  #1500

#usage 

#programming --> program



#protected ---> variable haro 

#protected variable



class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen,initial_balance):
        
        self.name = nam
        self.age = sen
        self.balance = initial_balance
        self._ATM_fee= 100
        
        
    def welcome(self):
        print(f'salam {self.name}')
        
    def show_balance(self):
        print(self.balance)
        
        
    def ATM(self,amount):
        self.balance = self.balance - amount - self._ATM_fee
        
        
        
a1=BANK('ali',18,2000)
#a1._ATM_fee =0
a1.ATM(200)
a1.show_balance() #1800

#for ... kari konm 

#shansi _ATm taghir konan
#gheyre ghabele taghir konam

#--> shansi -->for , while 





class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen,initial_balance):
        
        self.name = nam
        self.age = sen
        self.balance = initial_balance
        self.__ATM_FEE= 100
        
        
    def welcome(self):
        print(f'salam {self.name}')
        
    def show_balance(self):
        print(self.balance)
        
        
    def ATM(self,amount):
        self.balance = self.balance - amount - self.__ATM_fee
        
        
        
a1=BANK('ali',18,2000) 
a1.__ATM_fee #AttributeError: 'BANK' object has no attribute '__ATM_fee'
a1._BANK__ATM_fee


#-------azizan --> in ghesmato khodeton -->
'''
bejay ekhodnan khodemon logic mantegho yad bgirim






'''




'''
Decorator

@property

@classmethod

@staticmethod


CHATGPT ,....



'''


class BANK:
    #BANK(nam,sen) --> nam , sen
    def __init__(self,nam,sen,initial_balance):
        
        self.name = nam
        self.age = sen
        self.balance = initial_balance
        self.__ATM_FEE= 100
        
    @property
    def welcome(self):
        print(f'salam {self.name}')
        
    def show_balance(self):
        print(self.balance)
        
        
    def ATM(self,amount):
        self.balance = self.balance - amount - self.__ATM_fee
        






'''

Code 3 no
1-monolothic -->yekparche az bala b paeen
--> bot -> har roozs saate 12 gehyamto ....

2- Function based --> kh az application, website, backedn
djnago, fastapi --> function based hastan
encapsulation anjam bdid



'''

#--------FUNCTIONS---------------

def add(a,b):
    c = a + b
    return c



#------
#3--> cLASS haro darim --> object besazi
'''
library ha , tools ha --> professiona;
aksaran az class sakhte shdoe
k class yechize mother hast k koli method (function)
to delesh


'''




class BANK:
    #object = class()
    #ham mige ch vorodi hae bde
    #ham in tabe aasan seda mikhore
    #init-->initial --> avalie (shoro) start
    
    def __init__(self,name,age,initial_balance):
        
        #attributes , vairables 
        
        #obj1=BANK('ali',20,20000)
        #obj1.name
        self.name = name
        self.age = age
        self.balance = initial_balance
        
        #------varibakle hae beshe k user vared
        self.transactionals=[]
        
        
        
    #methods --> functions tabe hastan
    #obj1.welcome()
    
    def welcome(self):
        print(f'salam  {self.name} khosh amadid')
        
        
    #obj1.show_balance()
    def show_balance(self):
        
        print(f'Mojodie shoma hast {self.balance}')
        
        
    #obj1.deposit(10000)
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactionals.append(f'+{amount}')
        
    #obj1.ATM(2000)
    def ATM(self,amount):
        
        if amount < self.balance:
            self.balance = self.balance - amount
            self.transactionals.append(f'-{amount}')

        else:
            print('mojodi kafi nistr')
            
            
    def show_transactions(self):
        
        for trans in self.transactionals:
            
            if trans[0]=='+':
                print('deposited : ',trans)
            else:
                print('withdraw : ',trans)
        
        
        
    
obj1= BANK('ali',20,2000)
                 
obj1.name #]: 'ali'
obj1.age #Out[4]: 20

obj1.transactionals #: []


obj1.welcome()
#salam  ali khosh amadid



obj1.show_balance()
#Mojodie shoma hast 2000

obj1.deposit(5000)



obj1.transactionals
#Out[11]: ['+5000']


obj1.ATM(20000)
#mojodi kafi nistr

obj1.ATM(1000)

obj1.transactionals # ['+5000', '-1000']
obj1.ATM(500)

obj1.deposit(2000)

obj1.deposit(3000)

obj1.ATM(200)

obj1.transactionals
# ['+5000', '-1000', '-500', '+2000', '+3000', '-200']



obj1.show_transactions()
'''
deposited :  +5000
withdraw :  -1000
withdraw :  -500
deposited :  +2000
deposited :  +3000
withdraw :  -200

'''

obj2= BANK('vahid',20,2000)
obj2.welcome()
#salam  vahid khosh amadid


#====================
#====================
#-----DB------
#====================
#====================


class BANK:
    #object = class()
    #ham mige ch vorodi hae bde
    #ham in tabe aasan seda mikhore
    #init-->initial --> avalie (shoro) start
    
    def __init__(self,name,age,initial_balance):
        
        #attributes , vairables 
        
        #obj1=BANK('ali',20,20000)
        #obj1.name
        self.name = name
        self.age = age
        self.balance = initial_balance
        
        #------varibakle hae beshe k user vared
        self.transactionals=[]
        
        self.deposition_fee= 500
        
        
        
        
        #database --> table [customers]
        #name , ag , .....balance
        
        
        
    #methods --> functions tabe hastan
    #obj1.welcome()
    
    def welcome(self):
        print(f'salam  {self.name} khosh amadid')
        
        
    #obj1.show_balance()
    def show_balance(self):
        #databse --> balance 
        
        print(f'Mojodie shoma hast {self.balance}')
        
        
    #obj1.deposit(10000)
    def deposit(self,amount):
        
        if self.balance > self.deposition_fee :

            self.balance = self.balance + amount - self.deposition_fee
            
            
            #pool --> table custoemr --> balance + amount --> zakhire
        
        
            self.transactionals.append(f'+{amount}')
        
            #tabel transaction --> tarikh, kodom shobe , ... ezafe
        
        
            #databse --> balance --> afzayesh
            
        else:
            print('mojodi nadarid')
            
        
    #obj1.ATM(2000)
    def ATM(self,amount):
        
        if amount < self.balance:
            self.balance = self.balance - amount
            self.transactionals.append(f'-{amount}')

        else:
            print('mojodi kafi nistr')
            
            
    def show_transactions(self):
        
        for trans in self.transactionals:
            
            if trans[0]=='+':
                print('deposited : ',trans)
            else:
                print('withdraw : ',trans)
        
      
        
      
#plutus_bank.com 

'''
------------
user : 
kar meli:
pole avali :
    
    
    create account
-----------------
FRONTEND --> Html, javascript , css


javascript

create_account_button.button(-->create_account_function)


def create_account_function :
    url = plutus_bank.com/create_account
    get url 
    


'''


'''
@fastapi.get('/create_account')
def create_account(name,age,kart_meli,initial_balance):
    
    #db --> databse table customers
    
    print('sakhte shod')
    pass

'''






class normal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._real = 0
        
        
obj1 = normal('ali',20)   
        
obj1.name       #Out[20]: 'ali'
obj1.name  = 'mohsen'
obj1.age #Out[21]: 20

obj1._real #Out[22]: 0
obj1._real = 1



#_real --> in private variabel 
#neshoonas ---> k bdonim in variable daroonie 
#vase karaye dakhel sakhte
#Birone class 





class user:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        
        
user1 = user('ali',20)

user1.name # 'ali'

user1.age #AttributeError: 'user' object has no attribute 'age'

#narikhtim to self.age

user1._age #20

user1._age = 40




class user:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        
        
    @property
    def age(self):
        return self._age
        
user1 = user('ali',20)

user1.name # 'ali'


user1.age #20


#age(self) --> objec.method()
 
user1.age= 40 #AttributeError: can't set attribute 'age'

user1._age= 40

#darooni bodane

class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
        
  
obj1= BANK('ali',4000)


#name
#shjow_balance
#deposition

#use --> estefade koni
#khodet --> aydet maid inas


#_balance??/





#taraf betone b balance dastrsi peyda kone
#ama natoone taghir bde

#_ --> sign



class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
        
    def _calculate(self):
        pass
        
        
    def balance(self):
        return self._balance
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
    

obj1= BANK('ali',4000)

obj1.balance() #4000


#property, attribute , variable




class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
obj1= BANK('ali',4000)

obj1.balance #Out[45]: 4000
obj1.balance=4000 #AttributeError: can't set attribute 'balance'



#-----
#mishe taghir dad vali 




class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,value):
        if value < 0 :
            raise ValueError('balance Cannot be negative')
        self._balance = value
        
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
    
obj1= BANK('ali',4000)

obj1.balance #Out[49]: 4000

obj1.balance = 2000


obj1.balance #Out[51]: 2000


obj1.balance = -1000
#ValueError: balance Cannot be negative




'''
TASK1 ---> shoma byad hadegahal 12 ta error ro list konid va estefadashi bnvisid

ValueError


Begard, gpt , ...

'''
 





#-=-----PROPERTY DECORATORS

#utilities --> ezafi , komak konanade
#supplementary
#coplementary

#tabe haye ezade

#UTILS 
#appendix


#-----STATIC DECORATORS
class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,value):
        if value < 0 :
            raise ValueError('balance Cannot be negative')
        self._balance = value
        
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
    
    def add(self,a,b):
        return a + b


#az brion az add() estefade konde
#majbore obejct besaze

obj1= BANK('ali',4000)

obj1.add(10,20) #Out[55]: 30


#agha bedone skahtane object bazi az
#tavabe ghabele run shdoan bashe


#staticmethod hastand

class BANK:
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,value):
        if value < 0 :
            raise ValueError('balance Cannot be negative')
        self._balance = value
        
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
    
    @staticmethod
    def add(a,b):
        #if a<50
        #raise error ....
        
        return a + b


BANK.add(10,20)  #30



#CLASS (mother) --> obj1 obj2 obj3
#seld --> obj1 

#har obj ye self
#obj1 self1
#obj2 self2
#obj3 self3



class BANK:
    
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,value):
        if value < 0 :
            raise ValueError('balance Cannot be negative')
        self._balance = value
        
        
        
    def show_balance(self):
        print(f'{self._balance}')
        
        
    def deposition(self,amount):
        self._balance = amount + self._balance
  
    
    @staticmethod
    def add(a,b):
        #if a<50
        #raise error ....
        
        return a + b


#beyne hame objects haye man share bashe


#---------

class BANK:
    
    count = 0
    
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        
        
        
obj1 = BANK('ali',2000)     

obj1.count #0




obj2 = BANK('vahid',4000)     

obj2.count #0



#cls ---> madar -->beyen ham emoshatarek



#self -->har obj
class BANK:
    #variable --> counting
    count = 0
    
    def __init__(self,name,initial_balance):
        self.name = name
        self._balance = initial_balance
        BANK.count += 1
        
        
    @classmethod
    def how_many(cls):
        return cls.count
        
        
        
BANK.how_many() #Out[68]: 0

obj1 = BANK('ali',2000)     
   
BANK.how_many()

        
obj2 = BANK('vahid',2000)     
BANK.how_many()





'''

@property 

@staticmethod

@classmethod






'''

#===============================================
# getattr, setattr, hasattr, delattr
#===============================================
'''
Khob mikhaym darmorede getattr , setattr , hasattr , delattr hgarf bznim

bebinid vaghty shoma yek class daird kheyli sade mitonid
ba seda zadane khdoe object va roosh dot beznaid va b attribute dastresi poeyda konid 
masalan

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Ali', 25)

'''

age name ya age ro bekhayd khetli sade

p.age
p.name
p.city

ama vaghty miayd tooye neveshtane application nabayad
risk konid choon momkene moshkel ijad she vaghty mikhayd 
az ye obejct chizi bekeshid , momkene esmehs ghalat bashe
khdoesh ghalat absh e, ya nadashte bashe

pas yeseri tabeye dakheli dare khode python k bema komak mikone

'''


# ----- hasattr(object, name) -----
'''
avalish hasattr hast k mitone check kone oon obecte shoma
aya oon attribute ro dare ya na
age dashte bashe True , age na False mizane

ama yadeton bashe in tabe yek tabeye dakhelie k narenji mishe

arguemnte aval object , argumente dovom str migrie
khob injorie :

'''
# True if object has that attribute (or says it has it), else False.
hasattr(p, 'name')   # True
hasattr(p, 'city')   # True (we set it)
hasattr(p, 'salary') # False


'''

pas ghabl az inke bezanid p.name bayad check konid

'''

if p.name:
    print(f'{p.name} is present')
else:
    print('is not present')


# ----- getattr(object, name [, default]) -----
'''
hala mitoni dbejaye inke hardafe check konid
mitonid bejaye khode p.name az ye tabe estefade kondi bename
getattr k miayd aval migid kodom objct , che attributi

masalan
bejaye 
p.name

mizanid getattr(p,'name')

'''
# Get attribute by string name. If missing and default given, return default; else AttributeError.
getattr(p, 'name')      # 'Ali'
getattr(p, 'age')       # 25


'''
Havaseton bashe ag nadashte bashe , bazam error mide in
ama mishe yek kar krd
mishe b onvane argumente sevome behesh begid age nadasht
besoorate default chi bzare jash (ham error nmikhorid 
ham dar soorat enabodanesh mitoonid bejash default bezarid)
'''


getattr(p, 'city', 'Tehran')   # 'Tehran' (no .city, so default used)





# ----- setattr(object, name, value) -----
'''
hamchenin bejaye inke biayn value gozari konid oon attribute ro 
bejaye inke benevisid

p.city = 'Tehran'

mitonid biayd az tabete setattr estefade kone

'''
# Set attribute by string name. Same as: obj.name = value
setattr(p, 'city', 'Tehran')
setattr(p, 'age', 26)
# now p.city is 'Tehran', p.age is 26



# ----- delattr(object, name) -----
'''
hamchnin mitondi dlete konid yek attribute ro be sadegi
'''

# Delete attribute by name. Same as: del obj.name. Raises AttributeError if missing.
delattr(p, 'city')
# hasattr(p, 'city')  # False now

# ----- Why use them? -----
# When the attribute name is in a variable (e.g. from config, loop, or user input):
attr_name = 'age'
getattr(p, attr_name)   # 25
setattr(p, attr_name, 30)


#hata mitonid inkar ro ham konid
# Example: call different methods by name
method_name = 'capitalize'
getattr('hello', method_name)()   # 'Hello'





