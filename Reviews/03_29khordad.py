'''
In The Name of GOD


Ali Pilehvar Meibody


29 Khordad 1405


'''

#===============================================
#===============================================
#===============================================
'''

Numpy

'''
#===============================================
#===============================================
#===============================================

'''
1- Calculation (fast) --> Ketabkhone ee hast k rooye C++ hast
2- Arraye haro beshnasi --> (dobodi ,...)
3- Ketabkhone ast ,--> ketabkhone ro yad begirim 
4- Hichvaght lazem nist tamame tavabe o ,... yad begirid , balke bayad
manteghesh ro baraye kjhdoeton daste bandi konid


daste bandi
Ref : Man
Ref : Khodetoon
Ref : GPT  (Discusssion)

'''

#-------- Array ro besazim
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


#attributes  (method) --> () 
#moshakahse hast , kari nmikoje
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype) # type of the array
print(a.itemsize) # size of the array
print(a.nbytes) # size of the array in bytes




#dastresi ham kh moheme (indexing)
#a[radif,soton]
print(a[0,0])
print(a[0,1])
print(a[0,2])
print(a[0,3])
print(a[0,4])


#methods----------------------

#1- Generators 
#arange,linspace, logspace -> shape ndre -> 1 bodi misaze

a = np.arange(0,10,2) #start,end , step

b = np.linspace(0,10,5) #start,end , number of elements
print(b)


c = np.logspace(0,10,5,base=2) #start,end , number of elements, base
print(d)


#shape midim
#zeros --> start, end , step ,--:> zero mikone . shape  . one --> yek mikonm
d = np.zeros(5)
d = np.ones((2,3)) #2 ta rafi, 3 ta soton
d = np.empty(5)


#----> full man barat full mikonm y matrix ro az y adad . oon adadaro bhsh bdi , shape bhsh

d = np.full(5,(2,3)) #2 ta radif, 3 ta soton az 5 full bashe


#random ..... ,.....



#2- Calculation (riazi)

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

c=  a.add(b)  #--> add mikone y arraye a va b

#mosalasati ,.,.......
a.mean() #miangin
a.sum() #jam
a.max() #max
a.min() #min
a.std() #standart deviasion
a.var() #variance
a.median() #median
a.mode() #mode
a.range() #range
a.percentile() #percentile
a.quantile() #quantile
a.corr() #correlation




#3- Functionals

a = np.array([1, 2, 3, 4, 5])

b = a.hsplit(2) #2 ta soton mikone
b = a.vsplit(2) #2 ta rafi mikone
b = a.split(2) #2 ta soton mikone
b = a.split(2,axis=1) #2 ta soton mikone
b = a.split(2,axis=0) #2 ta rafi mikone
b = a.split(2,axis=1) #2 ta soton mikone

#radifi, sotoni joda , beham bechasboon



#===============================================
#===============================================
#===============================================
'''

Matplotlib

'''
#===============================================
#===============================================
#===============================================
'''


Baraye rasm estefade mishe


ma chand no plot darim



structure asli chie???



'''


#AZ 3 BAKHSH TASHKIL SHODE

#0 ----> datato amade mikone , numpy array, list, pandas ,....... 
#x , y 
#x 


x= np.array([1, 2, 3, 4, 5])
y= np.array([6, 7, 8, 9, 10])

import matplotlib.pyplot as plt

#1------ Plot ro mikhay rasm koni
''''
plot() --> rasme khat
scatter() --> ramse data point
pie() --> ramse pie chart
bar() --> ramse bar chart
hist() --> ramse histogram
'''
#dahele plot() , scatter() , pie() , bar() , hist() --> configuration inja mizanim
#mesle kheyli chiza --> ba details stadris shode

plt.plot(x,y,color='red',linewidth=2,markersize=10,marker='o',label='Line Plot')



#2-----> bahse settinge kolie axe bia biron
#baraye hame msohtarake .....
plt.title('Title of the plot') #font , ...
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.grid(True) #grid mikone
plt.legend()
#bejaye ina koli chiz haye dg ham darim

plt.ylim(0,10) #y axis range
plt.xlim(0,10) #x axis range
plt.xticks(np.arange(0,10,1)) #x axis ticks
plt.yticks(np.arange(0,10,1)) #y axis ticks
plt.xticks(rotation=45) #x axis ticks rotation
plt.yticks(rotation=45) #y axis ticks rotation
plt.xticks(fontsize=10) #x axis ticks font size
plt.yticks(fontsize=10) #y axis ticks font size
plt.xticks(fontweight='bold') #x axis ticks font weight
plt.yticks(fontweight='bold') #y axis ticks font weight






#3----> Show() ya save mikhay koni
plt.show()


#plt.savefig('plot.png') #save mikone
#plt.savefig('User/apm/desktop/myplot_29khordad.png')



#===============================================
#===============================================
#===============================================
'''

Pandas

'''
#===============================================
#===============================================
#===============================================
'''
Numpy alculation, radifo soton esmi chizi ndrn


Anginze sazandeye pandas
Pandas --> data --> column label ,mese jadval
excell, ... --> label daan -> varede python


koli tavabe ee dare wzafe krde --> data analysis, data cleaning, data manipulation




'''
# 2 part dare


#PART1 --> Pandas General 
import pandas as pd #mokhafafe

#--->dataro chijori mishe sakht?
#DataFrame  --> D , F bzoiorg
#DataFrame  --> az Series() sakhte shode


#dasti besazi , numpy ,--> , column label, radif ha ro label
#a = pd.DataFrame([[radif1],[radif2],[radif3]],columns=['soton1','soton2','soton3']) #DataFrame mikone


#import koni 
b = pd.read_csv('path/to/file.csv') #csv file import kone
b = pd.read_excel('path/to/file.xlsx') #excel file import kone
b = pd.read_json('path/to/file.json') #json file import kone
b = pd.read_html('path/to/file.html') #html file import kone
b = pd.read_clipboard() #clipboard import kone



#yechizi daram bname dataframe

a.head() #5 ta radif print kone
a.tail() #5 ta radif print kone
a.info() #info print kone
a.describe() #describe print kone
a.columns() #columns print kone

#access --> Soton, bad radif
a['soton1'] #soton1 print kone
a['soton2']


#radif
#a.loc() --> a.loc[]
a.loc[0] #radif 0 print kone
a.loc[0:2] #radif 0 ta 2 print kone

a.loc['test1']
a.iloc[1]  # i --> index



#yek element

a['soton1'].loc['test1']
a['soton1'].iloc[1]




#---> Gozaresh haye amari
#method haye dexribe tosifi 

a.describe()


a['soton1'].max()
a['soton1'].min()
a['soton1'].mean()
a['soton1'].median()
a['soton1'].mode()
a['soton1'].std()
a['soton1'].var()
a['soton1'].skew()
a['soton1'].kurt()
a['soton1'].corr()

#har soton bekeshi biron har chix amari


a.sum() #-->summo too kole radifo sotona migire
a.sum(axis=1) #-->summo too kole sotona migire
a.sum(axis=0) #-->summo too kole radifo migire


a.max() #max too kole radifo sotona migire
a.max(axis=1) #max too kole sotona migire
a.max(axis=0) #max too kole radifo migire

a.min() #min too kole radifo sotona migire
a.min(axis=1) #min too kole sotona migire
a.min(axis=0) #min too kole radifo migire





#filteration 

a[a['soton1'] > 5] #soton1 bozorgtar az 5 print kone

#apply



#methods --> 
a.apply(lambda x: x*2) #x*2 kone

a.drop(columns=['soton1']) #soton1 drop kone
a.drop(index=[0]) #radif 0 drop kone
a.drop(columns=['soton1'], index=[0]) #soton1 drop kone, radif 0 drop kone


#****** --> Tavabeye pandas --> behet khoroji mide , magar inke 
#yek argument dare bename inplace --> True koni hamonja emal mikone




#PART2 --> Pandas Data Cleaning

'''
data.info()

1- Empty cell 
.dropna()
.fillna()

2. wrong format
.astype()

3.Wrong logic
for .. , filter, apply ,....

4.duplciated
.drop_duplicates()



.reset_index(drop=True,inplace=True)


data amadas




#save


data.to_csv('path/to/file.csv') #csv file save kone
data.to_excel('path/to/file.xlsx') #excel file save kone
data.to_json('path/to/file.json') #json file save kone
data.to_html('path/to/file.html') #html file save kone

'''



#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================


''''

Che konim ???




1- Dostani k fght numpy residan
dar in hafte ta jaye momken khdoeshon ro beresonan (ama ejbari nist)
Olaviate aval ba pandas hast (makhsosan data cleaning)

olaviat --> Pandas [kafie]
ag vaghyt krdi --> statistic, linear algebra, matplotlibg --> hafte haye bad




2- dostani k 2 ta ketabkhone ro khondan (ag pandas jozvesh nist)
In ye hafte ro pandas ro bekhonan

Hatman focus in hafte --> Pandas
ag residan --> video statistic ro bbinan [fght gozari] vaght hast 




3- dostani k 3 ta ketabkhone ro khondan 
emroz barashon reveiw shod, reveiw dg konn
Statistics --> jalaseye ghabl 

Statistic -> besorat herfe eee negah konan va yad bgiran











Dar kol --> har 3 goroh --> Statistics -> videosh ro bbinan 3 saat bihstr [did behet mide]



4- statistic ,,...... jolotarin --> Review --> Jabr --> Jabre pishrafte







Jalase ye Ayanade ---> ch shoma residid ya naresidid --> yek jalaaseye jhadidi

yek ketabkhane ye jadide
2 jaalse -->  SK LEARN   

jalase 1 --> sklearn 
jalse 2 --> sklearn + pandas

3 hafte baraye pandas vaght hast 





'''





