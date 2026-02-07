
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


