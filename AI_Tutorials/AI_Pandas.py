"""
In  The Name of GOD


Created on Fri Jun  5 08:54:07 2026
Jome 15 Khordad mah 1405



@author: Ali Pilehvar Meibody


Numpy,scipy, sympy , Matplotlib 

Pandas --> 1 Step before Machine learning

Pandas ---> Data (excell, ...) --> clean, filter, feature engineering ,...
--> Machine learning, Deep learning (AI)


pip install pandas --> Nasb mishe (mohiti k dashtid)

import pandas as pd


"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


#iterables--> zarf --> multiple value dakhelesh
#list, set , tuple , dictionary
#------List-------------

a = [10,20,30,40,50]

a[0] #-->10
a[1] #-->20
a[0:2] #--> [10,20]

a[0] = 400  # a= [400,20,30,40,50]

#list functions
a.append(400)
a.insert(3,3238)
a.remove(20)
a.pop(3)
a.clear()  # []
del a    #delete a ro 



#Python (speed slow ) , Multi dimentional
#------Numpy-----------
import numpy as np
#array --> araye --> list ,....

#0 d
a = np.array(0)
a.ndim #0
a.shape #()

#1d -->[list]
b= np.array([10,20,30,40])
print(b) #[10 20 30 40]
b.ndim #1
b.shape #(4,)
b.size #4

b[0] #10
b[0:2] #array([10,20])

b[0] = 300
print(b) #[300,20,30,40]

#defintiin --> np.arange() np.random() np....
#add , kam 
#join , split , ........


#2d --> [radif, soton]
#numpy --> radif arjahiat darad
c= np.array([ [10,20,30] , [40,50,60]  ])
print(c)
'''
[[10 20 30]
 [40 50 60]]
'''
c.ndim #2
c.size #6
c.shape #(2,3)    2ta radif, 3 ta sotoon

c[0] # array([10, 20, 30])  radife 0
c[1] # array([40, 50, 60])

#b adade 30 --> aval bgm kodom radif, kodom soton
#radife 0 , sotone 2
c[0,2] #30



#sotone 2 
c[0,2] #30
c[1,2] #60

c[:,2] #array([30, 60])

#numpy function haye khodesho dare , reshape()
#random.uniform() .gaussian() , shape --> (radif,soton)


'''
case      Temperature   Pressure   Estehkam
1              20         1           30
2              30         2           45
3              40         3           50
          
'''
import numpy as np

d = np.array([ [1,20,1,30] ,[2,30,2,45] , [3,40,3,50]   ])

print(d)
'''
[[ 1 20  1 30]
 [ 2 30  2 45]
 [ 3 40  3 50]]

'''

d[0] #Out[28]: array([ 1, 20,  1, 30])

d[0,1] #20
#d[0,'temperature']






#--------
l1= list([10,20,30])
n1 = np.array([10,20,30])
d1 = pd.Series([10,20,30])


print(l1) #[10, 20, 30]
print(n1) #[10 20 30]
print(d1)
#0    10
#1    20
#2    30
#dtype: int64


print(type(l1)) #<class 'list'>
print(type(n1)) #<class 'numpy.ndarray'>
print(type(d1)) #<class 'pandas.core.series.Series'>


l1.append(100)
print(l1) #[10, 20, 30, 100]

n1.append(100) #AttributeError: 'numpy.ndarray' object has no attribute 'append'
n1.ndim #1
l1.ndim #AttributeError: 'list' object has no attribute 'ndim'

'''
1D
List  --> easy , loop bzane
np Array -->  Fast (speed) ,calculation 
pd series --> kar ba data  , sotone yek excell

'''



#Numpy --> numpy.array()
#Pandas ---> pandas.Series() pandas.DataFrame()


#A serie --> 1d array (list) , ye soton tooye yek jadval mimone

import pandas as pd

#*****
#tabe haye pandas case sensetive -->Aval --> Bozorg

s1 = pd.Series([30,40,50])


print(s1)
'''
0    30
1    40
2    50
dtype: int64

'''


s1 + [10,20,30]
#khoroji mide mitoni zkahire koni
'''
0    40
1    60
2    80
dtype: int64

'''


print(s1)
'''
0    30
1    40
2    50
dtype: int64

'''
s1 + 100

'''
0    130
1    140
2    150
dtype: int64
'''

s1 <35
'''
0     True
1    False
2    False
dtype: bool

'''
#+ , / , .... -->tamme element ha



#numpy arrat --> series
import numpy as np
a = np.array([30,40,50])


import pandas as pd
s2= pd.Series(a)

print(a) #[30 40 50]
print(s2)
'''
0    30
1    40
2    50
dtype: int64

'''




#dictionary ro tabdil koni
d1= {'bob' : 50 , 'ali' : 80 , 'vahid':90 , 'reza':100}

print(type(d1)) #<class 'dict'>


s3 = pd.Series(d1)

print(s3)
'''
bob       50
ali       80
vahid     90
reza     100
dtype: int64

'''


#----------------

s4 = pd.Series([50,80,90,100])
print(s4)
'''
0     50
1     80
2     90
3    100
dtype: int64

'''


s5 = pd.Series([50,80,90,100],index=['bob','ali','vahid','reza'])
print(s5)
'''
bob       50
ali       80
vahid     90
reza     100
dtype: int64

'''

s5[0] # 50
s5['bob'] # 50


#mokhtase pandas --> injori access mikonan

#.loc[]     .loc() XXXXX
#.iloc[]

#loc[]  , iloc[] -->i -->indexe location

#ba loc, iloc mitonam dastesi dahste basham
s5.loc['bob'] #50
s5.iloc[0] #50



s5.loc[0] #KeyError: 0
s5.iloc['bob'] #TypeError: Cannot index by location index with a non-integer key


s5.keys() #Index(['bob', 'ali', 'vahid', 'reza'], dtype='object')


s2.abs() #ghadre motlagh
s2.add()  #add mikoni y adad
s2.div() #divide
s2.divide() #divide
s2.divmod() #divide integer (gerd mikone)
s2.multiply() #zarb
s2.mul() #zarb
s2.pow() #b tavan

s2.pop() #remove
s2.clip()  #thresholding


s2.all() #shart --> baraye hame True --> True
s2.any()  #hsart --> baraye hadeaghal yeki az element trye -->true
s2.max() #max
s2.min() #min
s2.argmax() #indexe elementi max
s2.argmin() #indexe elementi min
s2.astype() #dtype taghir bedi , as type 
s2.view() # copy deep
s2.copy() #copy deep
s2.keys()  #kilid vazhe haro 
s2.items() #index , value --> for i,j in ...

s2.apply() 
s2.filter()
s2.isin()
s2.isna()
s2.isnull()
s2.fillna()
s2.drop()
s2.drop_duplicates()
s2.dropna()
s2.ffill()
s2.bfill()






#pandas.Series() ---> 1D kh kh kh kam estefade mikonim
#1d -> list, numpy ,


#Jadvale dade haro betonim biaym represent kone
#2D

#Pandas --> Series() , DataFrame() 

#2D 

n2 = np.array([[10,20,30],[40,50,60]])
print(n2)
'''
[[10 20 30]
 [40 50 60]]

'''

n2.ndim # 2
n2.size #6
n2.shape #(2, 3)
n2[0] # array([10, 20, 30])
n2[0,2] #30
n2[:,2] #array([30, 60])



print(type(n2)) #<class 'numpy.ndarray'>

#----> DataFrame estefade konm
'''
[[10 20 30]
 [40 50 60]]

Bsorate pandas
'''
#df -->dataframe

import pandas as pd

df1 = pd.DataFrame([[10,20,30],[40,50,60]])


print(df1)

'''
    0   1   2
0  10  20  30
1  40  50  60

'''

print(type(df1)) #'pandas.core.frame.DataFrame'>



df2 = pd.DataFrame([[10,20,30],[40,50,60]],columns=['dama','feshar','estehkam'])


print(df2)

'''
   dama  feshar  estehkam
0    10      20        30
1    40      50        60

'''


df3 = pd.DataFrame([[10,20,30],[40,50,60]],index=['case1','case2'])
print(df3)

'''
        0   1   2
case1  10  20  30
case2  40  50  60

'''


df4 = pd.DataFrame([[10,20,30],[40,50,60]],index=['case1','case2'],columns=['dama','feshar','estehkam'])

df4 = pd.DataFrame(data=[[10,20,30],[40,50,60]],index=['case1','case2'],columns=['dama','feshar','estehkam'])

print(df4)
'''
       dama  feshar  estehkam
case1    10      20        30
case2    40      50        60

'''

'''
XXXXXXXXXX PANDAS XXXXXXXXXXXXX

1D --> Series()    Series(, index=[]) 



2D --> DataFrame()   (data=,index=[],columns=[])
na index,na column (adad) label ndrn --> df1
fght columns label dare ---> df2
fght index label dare -->df3
ham index, column joftesh label dare --> df4



standardtrin halat --> index ( adad bashe) column --> label dashte bashe
excdel sotona y esmi drn vali radifa adadan

'''

import pandas as pd

#df = pd.DataFrame(data=[[],[]],columns= , )
df = pd.DataFrame([[25,1,500],[28,2,600],[30,3,700]],columns=['dama','feshar','esthekam'])


print(df)
'''
   dama  feshar  esthekam
0    25       1       500
1    28       2       600
2    30       3       700

'''

#*********
#soton avale 

df.columns #Index(['dama', 'feshar', 'esthekam'], dtype='object')



df['dama']

'''
0    25
1    28
2    30
Name: dama, dtype: int64

'''

zarf1= df['dama']
print(zarf1)
'''
0    25
1    28
2    30
Name: dama, dtype: int64

'''

print(type(zarf1)) #<class 'pandas.core.series.Series'>



df['feshar']
'''
0    1
1    2
2    3
Name: feshar, dtype: int64

'''

#loc , iloc radif

df.loc[0]
'''
dama         25
feshar        1
esthekam    500
Name: 0, dtype: int64

'''

df.iloc[0]

'''
dama         25
feshar        1
esthekam    500
Name: 0, dtype: int64

'''

#series --> loc , iloc
df['esthekam']


#kodom soton, kodom radif
df['esthekam'].loc[0] #500
df['esthekam'].iloc[0] #500

df['dama'].loc[1] #28

df['dama'].loc[1]  = 28.5


print(df)
'''
   dama  feshar  esthekam
0  25.0       1       500
1  28.5       2       600
2  30.0       3       700

'''



#------------Function haye pandas--------

df = pd.DataFrame([[25,1,500],[28,2,600],[30,3,700],
                   [35,4,800],[40,5,900],[45,6,1000],
                   [50,7,1100],[55,8,1200],[60,9,1300]],columns=['dama','feshar','estehkam'])

print(df)
'''
   dama  feshar  estehkam
0    25       1       500
1    28       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300

'''

df['feshar']
'''
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
Name: feshar, dtype: int64

'''

df['estehkam'].loc[5] #1000
df['estehkam'].iloc[5]



#----------Moghayese---------------
df['estehkam'] >600
#baraye tamame radif ha in shart ro check mikone
'''
0    False
1    False
2     True
3     True
4     True
5     True
6     True
7     True
8     True
Name: estehkam, dtype: bool

'''

#comparison --> > >= < <= == !=  --> True false element mide



#----------Filtering---------------

filtering_list=[True,False,True,False,False,False,False,False,False]

df[filtering_list]
'''
   dama  feshar  estehkam
0    25       1       500
2    30       3       700

fght oon radifae k tru hastan ro pas mide

khodam baim dasti liste tru false bnvsim
mage comaprison --> True falsi
'''


#---------
#df['estehkam']>600---> listi True false
#df [filtering ] -->filter

df[df['estehkam']>600]

'''
   dama  feshar  estehkam
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300

'''


#hazf nmikone, khoroji mide

print(df)
'''
   dama  feshar  estehkam
0    25       1       500
1    28       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300

'''




df_high_strength = df[df['estehkam']>1100]

print(df_high_strength)
'''
   dama  feshar  estehkam
7    55       8      1200
8    60       9      1300

'''


df_low_temperature = df[df['dama']<30]

print(df_low_temperature)
'''
   dama  feshar  estehkam
0    25       1       500
1    28       2       600

'''


specific_df = df[df['dama']==25]

print(specific_df)
'''
   dama  feshar  estehkam
0    25       1       500
'''



new_df = pd.DataFrame([[25,1,500],[25,2,600],[30,3,700],
                   [35,4,800],[40,5,900],[45,6,1000],
                   [50,7,1100],[55,8,1200],[60,9,1300]],columns=['dama','feshar','estehkam'])

print(new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300

'''


specific_new_df = new_df[new_df['dama']==25]


print(specific_new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600

'''

very_specific_new_df = new_df[ (new_df['dama']==25) & (new_df['estehkam']>550)  ]

print(very_specific_new_df)
'''
   dama  feshar  estehkam
1    25       2       600

'''



new_df[new_df['dama'].isin([25,30])]
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700

'''


#--------Adding new column

print(new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300

'''

#adad , list 
new_df['jadid'] = 0 

print(new_df)
'''
   dama  feshar  estehkam  jadid
0    25       1       500      0
1    25       2       600      0
2    30       3       700      0
3    35       4       800      0
4    40       5       900      0
5    45       6      1000      0
6    50       7      1100      0
7    55       8      1200      0
8    60       9      1300      0

'''

#+ - * ,...
new_df['jadid'] = new_df['dama'] +100
print(new_df)
'''
   dama  feshar  estehkam  jadid
0    25       1       500    125
1    25       2       600    125
2    30       3       700    130
3    35       4       800    135
4    40       5       900    140
5    45       6      1000    145
6    50       7      1100    150
7    55       8      1200    155
8    60       9      1300    160

'''

df['dama'].apply(lambda x: 'high temp' if x>30 else 'low temp' )
'''
0     low temp
1     low temp
2     low temp
3    high temp
4    high temp
5    high temp
6    high temp
7    high temp
8    high temp
Name: dama, dtype: object

'''
#chizi taghir nmikone
 
 
 
new_df['category'] = df['dama'].apply(lambda x: 'high temp' if x>30 else 'low temp' )

print(new_df)

'''
   dama  feshar  estehkam  jadid   category
0    25       1       500    125   low temp
1    25       2       600    125   low temp
2    30       3       700    130   low temp
3    35       4       800    135  high temp
4    40       5       900    140  high temp
5    45       6      1000    145  high temp
6    50       7      1100    150  high temp
7    55       8      1200    155  high temp
8    60       9      1300    160  high temp

'''

new_df.loc[new_df['dama']>30,'category 2'] = 'high temp'
new_df.loc[new_df['dama']<=30,'category 2'] = 'low temp'

print(new_df)

'''
   dama  feshar  estehkam  jadid   category category 2
0    25       1       500    125   low temp   low temp
1    25       2       600    125   low temp   low temp
2    30       3       700    130   low temp   low temp
3    35       4       800    135  high temp  high temp
4    40       5       900    140  high temp  high temp
5    45       6      1000    145  high temp  high temp
6    50       7      1100    150  high temp  high temp
7    55       8      1200    155  high temp  high temp
8    60       9      1300    160  high temp  high temp

'''

#.pop  del 
#.drop

new_df.drop(columns='jadid')
'''
   dama  feshar  estehkam   category category 2
0    25       1       500   low temp   low temp
1    25       2       600   low temp   low temp
2    30       3       700   low temp   low temp
3    35       4       800  high temp  high temp
4    40       5       900  high temp  high temp
5    45       6      1000  high temp  high temp
6    50       7      1100  high temp  high temp
7    55       8      1200  high temp  high temp
8    60       9      1300  high temp  high temp

'''

print(new_df)
'''
   dama  feshar  estehkam  jadid   category category 2
0    25       1       500    125   low temp   low temp
1    25       2       600    125   low temp   low temp
2    30       3       700    130   low temp   low temp
3    35       4       800    135  high temp  high temp
4    40       5       900    140  high temp  high temp
5    45       6      1000    145  high temp  high temp
6    50       7      1100    150  high temp  high temp
7    55       8      1200    155  high temp  high temp
8    60       9      1300    160  high temp  high temp

'''

#str khoroji midadan, emal nmishodn

#list khoroji nmdiadan, emal mishodan



#-----Strategy --> DF roosh taghiur emal koni , df das nakjorde

#df=......


#df1 = df.drop()  df.apply() df.()... _.emal nmishan
#df2

#df das nakhridas --> sad ta df 


#strategy -->
#df =.....
#rooye khode dfetemal she
#inpace = False --> default --> anjam nmidam (emal nmikonm)
#Truye koni rooye 

#khoroji nmide, zarf nemikham

new_df.drop(columns='jadid',inplace=True)


print(new_df)
'''
   dama  feshar  estehkam   category category 2
0    25       1       500   low temp   low temp
1    25       2       600   low temp   low temp
2    30       3       700   low temp   low temp
3    35       4       800  high temp  high temp
4    40       5       900  high temp  high temp
5    45       6      1000  high temp  high temp
6    50       7      1100  high temp  high temp
7    55       8      1200  high temp  high temp
8    60       9      1300  high temp  high temp

'''


new_df.drop(columns='category 2',inplace=True)

print(new_df)

'''
   dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
3    35       4       800  high temp
4    40       5       900  high temp
5    45       6      1000  high temp
6    50       7      1100  high temp
7    55       8      1200  high temp
8    60       9      1300  high temp

'''

#new_df

#new_df.drop(index=...)  #

#new_df.drop(index=8)

new_df.drop(index=8,inplace=True)

print(new_df)
'''
   dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
3    35       4       800  high temp
4    40       5       900  high temp
5    45       6      1000  high temp
6    50       7      1100  high temp
7    55       8      1200  high temp

'''

#''  Nan np.nan ,....

#shodanie , ama maghool nis


new_df.drop(index=3,inplace=True)


print(new_df)

'''
   dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
4    40       5       900  high temp
5    45       6      1000  high temp
6    50       7      1100  high temp
7    55       8      1200  high temp

'''

#reset_index estefade kon

#new_df.reset_index()



new_df.reset_index(inplace=True)

print(new_df)
'''
   index  dama  feshar  estehkam   category
0      0    25       1       500   low temp
1      1    25       2       600   low temp
2      2    30       3       700   low temp
3      4    40       5       900  high temp
4      5    45       6      1000  high temp
5      6    50       7      1100  high temp
6      7    55       8      1200  high temp


besoorate default in tabe ham reset mikone index va ham
ye backup az indexe ghabli bht mide


dar aksare mavaghe shoma hamijnam nmikhay
argument drop --> True
'''


#tahe kare dg reset shod hgamechi
new_df.reset_index(drop=True,inplace=True)
print(new_df)

'''
  dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
3    40       5       900  high temp
4    45       6      1000  high temp
5    50       7      1100  high temp
6    55       8      1200  high temp

'''

#sort_index() sort_values() ,..... 

#khodeton dast bekar bayad beshid
#Chatbot --> khode ino bdid chi ja oftad

#bgo practical 5 lecture 



new_df = pd.DataFrame([[25,1,500],[25,2,200],[30,3,100],
                   [35,4,800],[40,5,900],[45,6,50],
                   [50,7,1100],[55,8,60],[60,9,1300]],columns=['dama','feshar','estehkam'])

print(new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       200
2    30       3       100
3    35       4       800
4    40       5       900
5    45       6        50
6    50       7      1100
7    55       8        60
8    60       9      1300

'''



#bar asase yek sotonet sort koni

new_df.sort_values(by='estehkam',inplace=True)

print(new_df)
'''
   dama  feshar  estehkam
5    45       6        50
7    55       8        60
2    30       3       100
1    25       2       200
0    25       1       500
3    35       4       800
4    40       5       900
6    50       7      1100
8    60       9      1300

'''
#default -> azx kochik b bozorg

new_df.sort_values(by='estehkam',ascending=False,inplace=True)
print(new_df)
'''
   dama  feshar  estehkam
8    60       9      1300
6    50       7      1100
4    40       5       900
3    35       4       800
0    25       1       500
1    25       2       200
2    30       3       100
7    55       8        60
5    45       6        50

'''

new_df.reset_index(drop=True,inplace=True)

print(new_df)

'''
   dama  feshar  estehkam
0    60       9      1300
1    50       7      1100
2    40       5       900
3    35       4       800
4    25       1       500
5    25       2       200
6    30       3       100
7    55       8        60
8    45       6        50

'''

new_df['rank'] = new_df['estehkam'].rank()


print(new_df)

'''
   dama  feshar  estehkam  rank
0    60       9      1300   9.0
1    50       7      1100   8.0
2    40       5       900   7.0
3    35       4       800   6.0
4    25       1       500   5.0
5    25       2       200   4.0
6    30       3       100   3.0
7    55       8        60   2.0
8    45       6        50   1.0

'''

new_df['rank'] = new_df['estehkam'].rank(ascending=False)


new_df

'''
   dama  feshar  estehkam  rank
0    60       9      1300   1.0
1    50       7      1100   2.0
2    40       5       900   3.0
3    35       4       800   4.0
4    25       1       500   5.0
5    25       2       200   6.0
6    30       3       100   7.0
7    55       8        60   8.0
8    45       6        50   9.0
'''




new_df.mean()
'''
dama         40.555556
feshar        5.000000
estehkam    556.666667
rank          5.000000
dtype: float64

'''



new_df['dama'].mean() #40.55555555555556
new_df['dama'].median() #40.0



s2 = new_df['dama']

print(type(s2))
#<class 'pandas.core.series.Series'>


s2.abs() #ghadre motlagh
s2.add()  #add mikoni y adad
s2.div() #divide
s2.divide() #divide
s2.divmod() #divide integer (gerd mikone)
s2.multiply() #zarb
s2.mul() #zarb
s2.pow() #b tavan

s2.pop() #remove
s2.clip()  #thresholding


s2.all() #shart --> baraye hame True --> True
s2.any()  #hsart --> baraye hadeaghal yeki az element trye -->true
s2.max() #max #50
s2.min() #min #30








#--------PLOT------------


import matplotlib.pyplot as plt

x=new_df['dama']
y= new_df['estehkam']

plt.scatter(x,y)
plt.title('Strenght vs temeprature ')
plt.ylabel('Strnegth (MG)')
plt.xlabel('Temp C')
plt.grid()
plt.show()





#--------

#line -> plt.plot()
new_df.plot(kind='line',x='dama',y=['estehkam'])
plt.show()



new_df.plot(kind='scatter',x='dama',y=['estehkam'])
plt.grid()
plt.show()




#===================================================
#===================================================
#===================================================
#===================================================
#===================================================
'''

Pandas man khodam misakhtam --> dasti

numpy --> pandas
dictionary --> pandas
dasti mineveshti 


vagheiate jahan ine ke , yek data dari 
in data ro mikhay biari too 

400 radif, 5 ta soton 


dasti biaram bala benevis

import konm



format
.png .jpfg --> ax
.mp4 .mov  -->film
.gif -->gife
.exe --> file ejra execute 
.txt --> text
.docs .doc .docx --> word

 
dade haye jadvali
.csv      ----- > CSV
.xls .xlsx  -----> Excell




'''

import pandas as pd

#halate manual (dasti) dasti dari Pandas DataFrame misazi
#dataframe --> vzihegi haye pandas estefasd koni -->filtering, .....

df = pd.DataFrame()


#dade ()
#dade at .excel  .xslx 

#roye file e excel , click mikone (get info), property --> directory 
#copy -> paste / esmesh ba format .

df = pd.read_excel('C://user//apm//desktop/...../esme_data.xls')



df = pd.read_csv('......./ name dade .csv')



#ta alan karridm-->dasti msiakhtim --> dataframe --> df --> karamono mikrdi

#excel,csv --> read_.. --> dataframe --> hame ye onkara

#df.columns --> sotona
#df['dama'].loc[]



#------ch alan ch manual ch upload .. karet tamom
#IDE (spyder )---> RAM 
#bbndish , gaht koni, khamosh bshge --> kole datahey tooye spyder
#zarf, variable (RAM) --> volatile 

#hARD ->non volatile 

#hame karato krdi

df.to_csv('addresss')

df.to_excel('addresss')

#zakhir mikone

'''

@fastapi.get('information')
def processor(name,sen):
    name , sen 
    
    import pandas as pd
    
    pd.DataFrame(..)
    
    df ......
    
    
    #ORM
    #sqlite.insert('Temeprature',df['dama'])
    #df['dama']


'''








