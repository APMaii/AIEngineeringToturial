"""
Created on Fri Feb 13 09:03:07 2026

@author: apm



"""

#------MULTIPLE Variables ----> iterables estefade mishod
a = [10,20,30,40,50,60]


#dastresi
a[1] #index 0

a[1:4]  # 1 , 2 , 3 


a[1]= 100

#methdos tabe
#list fucntion

a.append(10)

a.insert(4,20)

a.remove(20) #remove element

a.pop(1)  #remove idnex


#for ....




'''
Moshkele list --> 1D . organziing 1 d 
table --> radif, soton -
3d --->chanta tabel rooham ????




moshekle 2 --> pythonic
rooye python neveshte shode 
yek zarf zakhrie mikonid --> ram --> [name , size , type , value]

a= 10

C++, C ---> 
int a
a = 10 #rooye memory fght yek adad ,rhata tar sari tar bashe


yek ketabkhone omd -> NUmpy
numpy array <---> List azash estefade koni
1- aval inek 1d , 2d , 3d , ....
2- core , rooye C neveshte shdoe , 60x faster --> calculation

ba in ide omd vasat -->b koja resid?
3- aksare ketabkhone ha harja mohasebta dahstan --> numpy 2000 o khorde ee
4-requirements aksare library (sklearn, pandas, matplotlib,....)
5- methods methods --> calculation bayad berid samte numpy [fght array nmide]
list.append()    array.koli method dare va kare shoam ro rahat mikone

6- spoecific --> scipy , sympy oomad --> differential equations -->hale maodelate difransiel o ...

'''



'''
Junior --> khob bayad tadris bshe, hol dade bshe
midlevel --> senior [khodet bayad bri yad bgriid]

shoma bayad khodet inkaro koni
12 ta ketabkhone , 

-----TARIGHEYE YADGIRI

esme yek ketabkhone ro mitoni peyda konid?
aval boro gpt ,..
miporsi --> library, python , .... fieldi?

entekhab mishe --> NUmpy

i am basic student [level],give me lecture from ..scratch..
about numpy in 10 lectures , start from lecture1


na --> shoma yek ashnaeiate koli gerefti ba kar
vali na midoni dastan chie, na mitoni mosalati



[ASHNAEIAT]
google.com
search mikoni esmesho --> peyda mikoni sitesho
.org hast 

https://numpy.org

Install --> tarighashe --> pip numpy search bzni --> pip install numpy
contribute --> github --> beri souyrce code ,jaeesh ezafe koni (FORKE + Ezafe, pull request)
news , about , community ,....


'Documentarion'
'tutorial , get started'
quick start



ya rtoo safe aslie ya tooye documentation
raftam Documentation --->

Quick start | getting started

https://numpy.org/doc/stable/user/quickstart.html

farsi ? --> extension chrome (tarjome) , gpt , translate , word ,... --> [Khandane zaban]


quick start -> shoro khob nabashe -> overview bde befahmi chekhabare
getting started, tutorial -->L dars midan daghigh behet



'''



#------TADRISE KHODE NUMPY-----

'''
Numpy


#---ag env nadari
#sakhte environement
python -m venv FANAAVRI2021

#faaal sazie 
source FANAAVRI2021/bin/activate



hatamn tooye environmentet bash
pip install numpy


python --> toye in mohti run koni ta
numpy ro dashte bashe
'''

import numpy

print(numpy.__version__) #1.26.4

#k shoma install krdish


#bejay elist ma mikhastim , --> array -->araye hast

import numpy


a = numpy.array([10,20,30,40])
b= [10,20,30,40]



type(a) #Out[14]: numpy.ndarray n-dimentional-array --> آرایه های چند بعدی
type(b) #Out[15]: list




#yek chizie k marof shdoe , gahrardade naneveshte 

import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from pygamlab import constant as gamcons


a = np.array([10,20,30,40,50])


type(a) #Out[18]: numpy.ndarray

#yekseri attributes darad

a.ndim #Out[19]: 1 --> list -> 1 bod dare
a.size # 5
a.shape #(5,)


print(a)
#[10 20 30 40 50]


a[0] #Out[23]: 10

b = a[0]
print(b) #10

#ag y index bdam-->y adad pas mide


a[0:2]
#array([10, 20])


#change?
a[0]=100

print(a)
#[100  20  30  40  50]



#-----DIMENSIONS -----------
#import ha jashon balaye code 
import numpy as np

#-0D ---> yadad

a= np.array(0)
a.ndim
#0 bod

#asan kh kam estefade




# ---1D --> list jaygozinesh (fast,...)

#a= np.array([0])
#a.ndim  1 D

b = np.array([10,20,30,40,50,60])
b.ndim #1
b.size #6
b.shape #(6,)

b[0]
b[0:5:2]

b[0]=100



#-----2D ---> do bodi --> radif o soton darim
#baraye inkar ma bayad 
'''

st*-->soton
        st1 st2 st3 st4
radif1 10   20   30   40
radif2 50   60   70   80


col* --> columns
     col1 col2 col3 col4
row1 10   20   30   40
row2 50   60   70   80



[] yedone beraket baz koni begi intoo

harchi mzindi yek radife 
ba comma joda msihe

[radif, radif,radif ,radif]

khodee radif ha --> list -->numpy array1 bodu


****forme nahaeee
[[radif1] , [radif2]]

radif1
radif2

****forme nahaeee
[[radif1] , [radif2]]



'''
import numpy as np

#1d
a=np.array([10,20,30])



#2d
b=np.array([ [10,20,30,40] , [50,60,70,80]  ])


b.ndim # 2 --> do bodi hast
b.size #8
b.shape #(2, 4)

'''
Numpy --> ASLE --->

(radif,soton)


dar numpy, radif moheme bad soton

(2,4)
chan soton chan radif, chan radif ssoton?/
numpye?? --> radif

(radif, soton)
(2,4)

2 ta radif, 4 ta soton

10 20 30 40
50 60 70 80

'''
#b=np.array([ [10,20,30,40] , [50,60,70,80]  ])
print(b)

#dastrsi b radif --->
'''
[[10 20 30 40]
 [50 60 70 80]]

'''

b[0] # array([10, 20, 30, 40])

#radife 0


b[1] #Out[46]: array([50, 60, 70, 80])




#--->element beresam --> 70
#radife dovoma?-->indedx harf
#
'''
            soton0 soton1 soton2 soton3
radif 0 --> 10       20     30      40]
radif 1 -->50       60     70       80


adad 70 --> radife 1 , soton2 

[1,2]

[radif, soton]
'''

b[1,2] #Out[47]: 70


#40 --> radif 0 , soton 3

b[0,3] #40


b[0,3] =10000

print(b)
'''
[[   10    20    30 10000]
 [   50    60    70    80]]

'''


#------dastresi b soton
'''
            soton0 soton1 soton2 soton3
radif 0 --> 10       20     30      40]
radif 1 -->50       60     70       80

20 
60

array[radif , soton]

array[tamame radif , 1]

array[: , 1]

'''

b[:,1] #Out[51]: array([20, 60])



#---recap
b= np.array([  [10,20,30,40] , [50,60,70,80]   ])

b.ndim #2
b.size #8 
b.shape #(2,4) --> (2 ta radif, 4 ta soton)

'''
            soton0 soton1 soton2 soton3
radif 0 --> 10       20     30      40]
radif 1 -->50       60     70       80

'''

#---radif dastresi
b[0] #radife 0 --> 10 ,20,30,40
b[1] #radif 1 -- 50,60,70,80

#element dastrsi
#array[radif,soton]
#70
#radi1 , soton2
b[1,2] #Out[52]: 70
b[1,2]=1000000

#datresi b soton
#soton2
b[:,1]  #: -->tamame radif ha
#Out[53]: array([20, 60])



#---3D----

'''
table jadval
10 20 30
40 50 60


1  2  3
4  5  6


9 99 999
8 88 888

'''
#[ table , table , table]
#[n2d , n2d , n2d]
#c = np.array([])
#c = np.array([ [] , [] , []  ])

#c = np.array([ [ [10,20,30],[40,50,60]   ] , [] , []  ])

c = np.array([ [ [10,20,30],[40,50,60]   ] , 
              [  [1,2,3] ,[4,5,6] ] ,
              [ [9,99,999],[8,88,888]  ]  ])



c.ndim #3
c.size #Out[56]: 18
c.shape #(3, 2, 3)

#(kodom jadval , kodom radif, kodom soton)
#(chnata jadval , chanta radif, chanta soton)
#3 ta jadval
#har jadval 2 ta radif
'''
10 20 30
40 50 60
'''
#har radif 3 ta soton

#dastresi
#array[kodom jadval, kodom radif, kodom soton]



#masal adade 3 ro mikhay
#jadvale 1 
#radife 0 
#sotone 2

c[1,0,2] #Out[58]: 3

#c[1,0,2]  = 10000

c = np.array([[[10,20,30][40,50,60]], 
              [[1,2,3],[4,5,6]],
              [[9,99,999],[8,88,888]]])



c = np.array([[[10,20],[30,40]],[[1,2],[3,4]],[[9,99],[8,88]],[[11,11],[11,11]]])
c.shape
#Out[61]: (4, 2, 2)


#4 ta jadval 
#har jadval --> 2 ta radif 2 ta soton 2x2


#4 ta 2x2


#----4D------
#mokaab
#3 ta mokaab daram
#mokaab --> 4 ta jadval 2x2
#jadval 2 radif
#har radif



#np.nan
#None
#0



'''
FLASHBACK

numpy -->ketabkhone

array 0--> fucntion

def array():
    
    return ndarray() -->clas


a = np.array() tabe 

a --> object hast 

a--> .attributes  .methods()





ma kolan 2 no tabe darim

yeki tabe ee k besoorate joda dar numpy sakhte va defined shode

baraye estefade

import numpy as np
np.function() estefade konid
too delesh numpy array bzarid



methods --> too dele nd.array hastan
a,b,c , zarf = np.array(.......)

zarf.function() #taghiro emal mikone



2 halat
overlap -->tabe ha ham esman. 
np.add(a,b)

a.add(b)

'''

#yad gereftim nd array chie
#khob man baaldam besazamesh
#ama b ch dardam mikhore???

#shoma harnoee adad k khasi b har tartibi
#besazi
#-----------------------

#tavabe biroooni
#-------------------------
#-------ASSIGNMENTS------
#-------------------------
import numpy as np

zarf = np.array([10,20,30,40],dtype='float32')


print(zarf)
#[10. 20. 30. 40.]

#start , stop , step

a= np.arange(10)
print(a)
#[0 1 2 3 4 5 6 7 8 9]

a.ndim #liste --> 1 
a.size # 10
a.shape #(10,)



a=np.arange(1,100,2)
print(a)
'''
[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47
 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95
 97 99]

'''


a = np.arange(0,101)
print(a)
'''
[  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100]

'''

#np.arange(0,101,2)
b= np.linspace(0,101,50)
print(b)

'''
[  0.           2.06122449   4.12244898   6.18367347   8.24489796
  10.30612245  12.36734694  14.42857143  16.48979592  18.55102041
  20.6122449   22.67346939  24.73469388  26.79591837  28.85714286
  30.91836735  32.97959184  35.04081633  37.10204082  39.16326531
  41.2244898   43.28571429  45.34693878  47.40816327  49.46938776
  51.53061224  53.59183673  55.65306122  57.71428571  59.7755102
  61.83673469  63.89795918  65.95918367  68.02040816  70.08163265
  72.14285714  74.20408163  76.26530612  78.32653061  80.3877551
  82.44897959  84.51020408  86.57142857  88.63265306  90.69387755
  92.75510204  94.81632653  96.87755102  98.93877551 101.  
  
'''

b =  np.linspace(0,1,10)
print(b)
'''
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]

'''

c = np.logspace(0,10,10 )

print(c)

'''
[1.00000000e+00 1.29154967e+01 1.66810054e+02 2.15443469e+03
 2.78255940e+04 3.59381366e+05 4.64158883e+06 5.99484250e+07
 7.74263683e+08 1.00000000e+10]

'''

#-----------------
#balaee ha bayad migofti ch rangi mikjay
#ch value haee bashe, yekseri tabe hast
#value malome --> shape bedi
'''

MATRIX -->
hamon radif soton
table 
matrix
matrices

'''

#
#zarf -->
np.zeros(10)
#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

np.zeros((2,5))

'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

'''


np.empty(10)

'''
array([1.00000000e+00, 1.29154967e+01, 1.66810054e+02, 2.15443469e+03,
       2.78255940e+04, 3.59381366e+05, 4.64158883e+06, 5.99484250e+07,
       7.74263683e+08, 1.00000000e+10
       
'''

#np.empty(2,3) ghalat
#(shape)


np.empty((2,3))

'''
array([[0.00e+000, 4.94e-324, 9.88e-324],
       [4.84e-322, 4.89e-322, 4.94e-322]])

'''


np.ones((3,5))

'''
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

'''

#((shape) , full by which value?)
np.full((2,3),3.14)
'''
array([[3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14]])

'''

#i x i --> radifo soton i -->vasat vatare 1
np.eye(3)

'''
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

'''



#4 x 4 --> 4 radif,. 4 soton
#Identity matrix
np.eye(4)
'''
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])

'''


#vatar aslio midi baghie sefre 
#diagonal Matrix
#vasatia , vatar, diagonal 1 nist
#adadie k b tartibe listet
np.diag([1,2,3])

'''
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])

'''


np.diag([1,2,3,4])

'''
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])

'''

#offset --> 

np.diag([1,2,3,4],k=0) 
'''
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])

'''

np.diag([1,2,3,4],k=1) 
'''
array([[0, 1, 0, 0, 0],
       [0, 0, 2, 0, 0],
       [0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0]])

'''

np.diag([1,2,3,4],k=2)

'''
array([[0, 0, 1, 0, 0, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]])

'''
np.diag([1,2,3,4],k=-1)
'''
array([[0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 2, 0, 0, 0],
       [0, 0, 3, 0, 0],
       [0, 0, 0, 4, 0]])

'''

data = np.genfromtxt('felan.dat') #azoon data birone spyder, laptab ,... 
#numpy tahvil mide



a_array= np.diag([1,2,3,4],k=-1)
#np->az numpy
#tabeye savetxt() ro vardar
#(esm , nujmpy arrat)
np.savetxt('random_matrix.csv',a_array)



#load , save --> PANDAS ****

#NUMPY ARRAY --> YCHIZI AZ PANDAS ?? -->JALASATE AYANDE




#-----RANDOM------
#bydefault
import random


random.random() # 0.3978211326844082

random.random() #0.7111013979063225

random.randint(10, 20) #18  # 12

#YEDONE ADAD MIDE --> ZARF
#Numpy --> randomo dare --> numpy arrray 
#k sortono radifash --> random shodand


#yek adade float betyne 0 , 1 
np.random.random() #0.016036791252807436

#tooye dleet tabe --> shap ebedi

np.random.random((2,3))

#yek np array bde 2 ta radif, 3 ta soton toosho 
#az 0 ta 1 random por kon

'''
array([[0.01302821, 0.32131125, 0.11003532],
       [0.08975113, 0.08635853, 0.72005935]])

array([[0.42946242, 0.55364992, 0.9012833 ],
       [0.48428207, 0.99827751, 0.52266241]])

'''


#statistic va amar 
#normal , uniform 

'''
uniform --> y ebaze a ta b
0 ta 10
harchi adade beyne 0 ta 10 ag
shanse entkehab shdosanshon yeksan bashe (hododan)

1.32981723  4.32832876 6.31293271 yeksan bashe
migim distibution (tozi) -> uniform hast 




Normal, Gaussian --> mohem 
distribution haye natural --> to tabiat
shoma ag brid shoneye khonaton 
beriz andaze begiri 100 bar
3.2
3.23  3.25  3.28
hole mehvare y adad jam shodan -> miangin 3.2

shans -->tamarkoz dare rooye yek adad 

3 ta 4 --> 3.5 
harchi az 3.5 doortar , shanse entkehab kamtar




shoma bekhayn adad bardari mitonid
uniformly vardare random
gussian way 

'''
np.random.uniform(0,10) # 7.121615786798342

#2.849058582400794


np.random.uniform(0,10,(2,3))

'''
array([[5.71142564, 6.91424201, 0.27549855],
       [3.61827544, 5.71250762, 6.08274449]])


yek matrxi misaze 2 radif , 3 soton
toosho az adade random beyne 0 ta 10

random.uniform --> tamame adadi k mikhad entkehab jkone
beyne 0 ta 10 -->  yani shanseshon abrabar

'''

#agha man mikham random avrdare vali hole mehbvare ye adadi

#adad -->miangin  #variance -> ta che had door az 

np.random.normal(20,5)

'''
np.random.normal(20,5)
Out[108]: 17.03996522106831

np.random.normal(20,5)
Out[109]: 20.60846555217081

np.random.normal(20,5)
Out[110]: 28.32151614349159

np.random.normal(20,5)
Out[111]: 22.39762540839053

np.random.normal(20,5)
Out[112]: 23.152387236503984

np.random.normal(20,5)
Out[113]: 21.798544631560613

np.random.normal(20,5)
Out[114]: 22.672818843304896

np.random.normal(20,5)
Out[115]: 10.639519214311392

np.random.normal(20,5)
Out[116]: 25.12574957247592


'''

np.random.normal(20,5,(4,8))

'''
array([[18.72457901, 20.38532885,  8.8207475 , 22.2734512 , 23.94882124,
        17.08555028, 27.81784715, 22.2992675 ],
       [13.10241245, 19.54967568, 21.03257341, 21.99984697, 18.04291681,
        18.34083232, 17.28079448, 13.90777631],
       [30.89369978, 16.4466896 , 26.3846876 , 18.19520122, 10.21888538,
        23.22527306, 13.00632073, 21.68581695],
       [17.11307324, 15.0891899 , 24.25784749, 23.13396121, 26.44826029,
        19.37355658, 23.59845303, 14.98749006]])

'''


np.random.normal(20,0.1,(4,8))

'''
array([[19.9684866 , 20.0049521 , 19.95963739, 19.95873158, 19.9461212 ,
        20.16194395, 19.9925845 , 19.96673518],
       [19.88976979, 20.00921887, 19.99770895, 19.79710315, 19.93734728,
        20.00289253, 20.04876567, 19.99728609],
       [20.15365752, 19.97597248, 19.91933496, 19.90805175, 19.9554191 ,
        20.11212627, 19.97742443, 20.14263579],
       [19.98154933, 20.09408171, 19.92026306, 19.95304042, 19.97369694,
        19.81817277, 19.90846459, 19.93995997]])

'''


#float --> ineteger

np.random.randint(0,10)
#Out[119]: 9

np.random.randint(12,18,(2,3))
'''
array([[12, 12, 16],
       [14, 12, 12]])
'''


#----advanced on dtype
'''
PYTHON TYPE --> INT, FLOAT, COMPLEX, BOOL


DTYPE------ mokhtase numpy --> C
bool_ Boolean astored as a byte
int_   default integer type ( same as C long: normally int64 or int32)
intc    identical to C int (normally int32 or int64)
intp    integer used for indexing ( C ssize_t , int32 or int64)
int8    byte(-128 , 127)
int16   integer ( -32768 to 32767)
int 32
int64

unit8    unsigned integer (0 to 255)
unit16 
unit32
unit64

float_   shoryhand for float64
float16
float32 
float 64

complex_ shorand for complex128
complex64
complex128
'''



#------RECAP-------
#numpy array --> fast , chan D 
#fhmidm chghdr -->adad sazi konm

#np.arange , np.linespace  , np.logspace

#----valu
#np.zeros(shape) ,np.ones() , np.empty() , np.eye() , np.diag(,k)

#---random
#np.random.random(shape) 0-1 
#np.random.uniform(a ,b, shape) float beyne a,b  
#np.random.normal(mean, vaeriance,shape) #float hole mehvare mean , ba fasle variance
#np.random.randint(a,b,shape) #1 - 10 -->integer midad



np.arange(1,21)

'''
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20])

'''



#agha man manzorma ine
'''
1   .... 10
11  .... 20

2 ta radif, 5 ta soton mikham
type ham k nmigire 

arange, linespace????
'''

#khode nparray ha-- >object
#az ch clas ->ndarray --> varibale

#a

#a.ndim
#a.size

#a.reshape()

#khoroji mide

a = np.arange(1,21)

print(a)
#[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

a.reshape((2,3))
#ValueError: cannot reshape array of size 20 into shape (2,3)

b = a.reshape((2,10))

print(b)

'''
[[ 1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20]]


'''



c = a.reshape((10,2))
print(c)

'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]
 [13 14]
 [15 16]
 [17 18]
 [19 20]]

'''

#----*** c = a.reshape() 
#yani in tabehe khoroji mide , #
#taghiri emal nmikone rooye a 
#a hamone k bood

a = np.zeros(20)
print(a)
'''
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

'''


#**havaset bashe type -->20 
#(5,4)

a.reshape(5,4)

'''
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

'''



#------
#vasete haro hazf kon

a= np.arange(0,10)
b = a.reshape(2,5)



a = np.arange(0,10).reshape(2,5)
print(a)
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]


'''

word='salam '

word.upper().strip() #'SALAM'

word.upper().lower().title().strip()


word='salam '
new_word= word.upper()
new_word2= new_word.lower()
new_word3 = new_word2.title()
new_word4 = new_word3.strip()

word.upper().lower().title().strip()



a = np.arange(0,10)
b = a.reshape(2,5)
c = b.reshape(10)

a = np.arange(0,10).reshape(2,5).reshape(10)



#-------------------------------------------------------
#-------------------MAGIC FUNCTIONS-------------------
#-------------------------------------------------------
#ina tavabe mostaghele numpuy nistand mesle
#np.arrange() np.zeros() np.random.uniform()
#ina method haye yek ndarray (class) hastan k bayad
#rooye oon numpy array dot bzni --> b.()
#-----reshaping
import numpy as np
#.reshape()
grid = np.arange(1, 10).reshape((3, 3))

print(grid)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''


#.astype()
M = np.array([10,20,30,40])
M.dtype #Out[141]: dtype('int64')

M2 = M.astype(float)
print(M2)
#[10. 20. 30. 40.]

M2.dtype #dtype('float64')


print(M) #[10 20 30 40]
M.dtype #dtype('int64')

'''
a = np.array([1,2,3,4])
a.reshape((2,2))

emal nmishe
hatman niaz b yek zarf drid
ch baraye tabae khareji va mostaghel
np.arange() np.zero()

method ha
a.astpe()  a.reshap()
'''


M3 = M.astype(bool)
print(M3)
#[ True  True  True  True]


##---flatten
a = np.random.uniform(1,10,(5,2))
print(a)
'''
[[9.63260924 5.67090252]
 [7.73690271 3.86751571]
 [1.54304279 7.2368842 ]
 [3.31023339 9.34176159]
 [8.68903823 4.33071184]]

'''

b = a.flatten()

print(b)
'''
[9.63260924 5.67090252 7.73690271 3.86751571 1.54304279 7.2368842 3.31023339 9.34176159 8.68903823 4.33071184]
'''
b.ndim # 1
b.shape # (10,)


#---copy and view
import numpy as np
arr1 = np.arange(0,10)


arr2 = arr1.copy()


arr3 = arr1.view()



arr2[5]=1000
print(arr2)
#[   0    1    2    3    4 1000    6    7    8    9]

print(arr1)
#[0 1 2 3 4 5 6 7 8 9]




#----
arr3[5]=1000
print(arr3)
#[   0    1    2    3    4 1000    6    7    8    9]

print(arr1)
#[   0    1    2    3    4 1000    6    7    8    9]






#---fancy indeexing
arr=np.array([11,22,33,44,55,66,77,88,99])
row_index = [1,2,3]

#index 1 , 2, 3
arr[row_index] #array([22, 33, 44])
#arrr[ [1,2,3]]

row_mask = np.array([True,True,False,False,False,False,False,False, False])

row_mask = np.array([1,1,0,0,0,0,0,0,0])


arr[row_mask]
#array([11, 22])


#-----------
#dfone done elementet hesab krde
x = np.array([1, 2, 3, 4, 5])
#man agh az comparisonal operators estefade konm
#nabayad montazwere yedoone true false basham
#x = [1,2,3] 
#x>10 --> yanichi?

#baklke manzoram ine har elemnt dar x aya bzoorgtr az 10 ?#
#pas montazere true false bishatri hasta,m


x < 3 # less than
#Out[5]: array([ True, True, False, False, False], dtype=bool)
x > 3 # greater than
#Out[6]: array([False, False, False, True, True], dtype=bool)
x <= 3 # less than or equal
#Out[7]: array([ True, True, True, False, False], dtype=bool)
x >= 3 # greater than or equal
#Out[8]: array([False, False, True, True, True], dtype=bool)
x != 3 # not equal
#Out[9]: array([ True, True, False, True, True], dtype=bool)
x == 3 # equal
#Out[10]: array([False, False, True, False, False], dtype=bool)





#-----
#azin feature mitoni estefade koni baraye filter krdn

x = np.arange(0,10)
print(x)
#[0 1 2 3 4 5 6 7 8 9]


row_mask = x>5
print(row_mask)
#[False False False False False False  True  True  True  True]


x[row_mask ]  # array([6, 7, 8, 9])
#fghtonae k true hastan ro mide
#francy indexing
#ino mitoni brizi too zrf





x[x>5] #array([6, 7, 8, 9])

x[x==4] #array([4])

#x[x>4 or x>=3]
#x[x>4 and x>=3]




#-----#where-->it get us the index
a = np.arange(10,40)

new=np.where(a==12)
print(new) #(array([2]),) -->indexe 2

a[2] #12


new=np.where(a>30)



#tamame jahae k in shart barat True mishe ro bht indexsho pas mide

print(new)
#(array([21, 22, 23, 24, 25, 26, 27, 28, 29]),)


len(new[0]) # 9









#----counting
x = np.arange(0,10)
#where + len
np.count_nonzero(x < 6) #6
np.sum(x < 6) #6

#chanat element in sharayet barashon mojhagaheghe


#------- conditions
#.any() .all()

#sharti mizari roo kole nuympy arrsay .any() 
#hadeghal yekishon in ro ok mishe

M = np.arange(5,10)

print(M)
#[5 6 7 8 9]

M>8
#array([False, False, False, False,  True])



#.any() .all() y true mide ya false
#rooye ye chizi k koli [tru true false false]

#any --> hadeaghal yeki az in ha
#ag yedone ham true bashe beynesh 
#agar hata yeki az element haye dakhele array M ,az 8 bozorgtre
#true pas 
(M>8).any() #9 -->>8 --> True
#True



#hameye element haye M az 8 bozorg tr bashand
(M>8).all() #False


#if , else

if (M>5).any():
    pass


if (M>5).all():
    pass





#---Array arithemic
#jabri anjam midim 
#baraye har element in karo konm
#for ......
#tavabe ee  + - 
#rooye element element array kar anajm bdi

x = np.arange(4)
print("x =", x)
#x = [0 1 2 3]

new = x + 5
print(new)
#[5 6 7 8]


print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
#x / 2 = [0.  0.5 1.  1.5]


print("x // 2 =", x // 2) # floor division
#x // 2 = [0 0 1 1]

print("-x = ", -x)
#-x =  [ 0 -1 -2 -3]

print("-x =", -1 * x)
#-x = [ 0 -1 -2 -3]


print("x ** 2 = ", x ** 2)
#x ** 2 =  [0 1 4 9]


print("x % 2 = ", x % 2)
#x % 2 =  [0 1 0 1]



x = np.array([4,6,8,10,12])

#aya hamash zooj hast?

x%2 #--> numpy array baghi mandeye harkodom
#[0 0 0 0 0 ]


x%2==0 #--> True Fasle
#array([ True,  True,  True,  True,  True])

(x%2==0 ).any() # True
(x%2==0 ).all() # True




x = np.array([4,6,8,7,12])

(x%2==0).any() #True
(x%2==0).all() #False


print(x%2==0)
#[ True  True  True False  True]












arr1=np.array([10,20,30])
arr2= np.array([20,30,40])
arr3= np.add(arr1,arr2)

print(arr3) #[30 50 70]

#np.add() ---> shoam mitoni

np.add() #+
np.substract() #-
np.negative() #-
np.multiply() #*
np.divide() #/
np.floor_divide() #//
np.power() #**
np.mod() #%
np.absolute()
#or
np.abs()



#------Comparison
arr1=np.array([10,20,30])

arr1>3 # array([ True,  True,  True])
arr1>=3 
arr1<3 
arr1<=3 
arr1==3
arr1!=3



#-----
arr1=np.array([10,20,30])
arr2=np.array([10,20,40])

np.equal(arr1,arr2)  # array([ True,  True, False])


arr1=np.array([10,20,30])
arr2=np.array([100,200,1])


#aya arr 1 az arr2 kochiktr hast?
np.less(arr1,arr2) #array([ True,  True, False])



#----don e done moghayese konam beytne dota rray
np.equal() #==
np.not_equal() #!=
np.less() #<
np.less_equal() #<=
np.greater() #>
np.greater_equal() #>=



#array -->10000 element 
#hadaaf --> ahmash bayad sedghkone, hadeaghal yekish
arr1=np.array([10,20,30])
arr2=np.array([100,200,1])

np.less(arr1,arr2) #np.array az tru false mide

np.less(arr1,arr2).any() #True


#aya ahme ye arr1 az arr2 hamashoon kcohiktrn>

np.less(arr1,arr2).all() #False



 


#---Trigonometric functions
theta = np.linspace(0, np.pi, 3)

print(theta)
#[0.         1.57079633 3.14159265]



print("theta = ", theta)
#theta =  [0.         1.57079633 3.14159265]

#sinus done done elemnt haye yek array ro bgirm

print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

#vorodi ya list bedi ya np array
#tavabe nevshte shdoie 
#Inpu --> List, numpy arrray ,..
#Khoroji --> Numpy arrray 
#az tabey numpy estefade mikoni

x = [-1, 0, 1]
print("x = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))




#Exponents and logarithms
x = [1, 2, 3]
print("x =", x)
#e**
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))


#nokteye asli -->in tavabe --> baraton y nd arrauy jadid misaz
#toosh bayad bzarid x , variable
#done done anjam mide baraye har element

#array --> yek chiz nbain
#ykchizi az chiz ha (elemnt ha) bebinesh


x = [1, 2, 4, 10]
print("x =", x)
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))





#----
x = [1.3 , 2.8]
#b paeen gerd mikone
np.floor(x) #array([1., 2.])


np.ceil(x)
#array([2., 3.])



#specialized functions
'''
from scipy import special
x = [1, 5, 10]
print("gamma(x) =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2) =", special.beta(x, 2))
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x) =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))
'''











#-----------------------

x = np.arange(1,6)
print(x) #[1 2 3 4 5]


np.add.reduce(x) #15


np.multiply.reduce(x) #120


#beman done done neshonbde
#1*2 -->2   2*3 --> 6   6*4 -->24  24*5 ->120
np.multiply.accumulate(x)
#Out[124]: array([  1,   2,   6,  24, 120])




#-----STATISTICS
#random ha sohbat

#Np.random.random() beyne 0 ta 1 float --> shape

#np.random.uniform(a,b,shape) #az a ta b --> shape ro
#np.random.normal(mean,variance , shape)

#np.random.randint(a,b) #integr mida



L = np.random.random(100)
print(L)
'''
[0.80222959 0.07894942 0.42059851 0.14907542 0.92798877 0.4627912
 0.15475565 0.6618435  0.58784648 0.79115779 0.79679832 0.82835395
 0.27187584 0.94472923 0.82823702 0.05262717 0.25835695 0.23485167
 0.28794714 0.64314675 0.28543144 0.98198517 0.95435668 0.39978538
 0.64350983 0.9038329  0.87394201 0.05311214 0.44752308 0.5632728
 0.87768612 0.56330696 0.22700284 0.9595241  0.39681074 0.26616065
 0.84900794 0.09536302 0.25160383 0.35014525 0.07026135 0.53923212
 0.22258151 0.83657879 0.74637742 0.055037   0.42623499 0.18821141
 0.61706252 0.2260063  0.36686731 0.71682258 0.49024109 0.72943461
 0.39890948 0.99632125 0.23251807 0.40410719 0.97754344 0.15903533
 0.04841419 0.20072715 0.84943721 0.75394774 0.32030464 0.31632382
 0.51085874 0.86815641 0.99309322 0.63717269 0.99114754 0.64017088
 0.74736605 0.45354721 0.36277059 0.23193163 0.53842361 0.45841963
 0.14566935 0.11710003 0.37977044 0.510686   0.64120124 0.25801337
 0.09051514 0.87961482 0.41199003 0.25997485 0.25409784 0.64055371
 0.33407954 0.24135215 0.32952643 0.95307759 0.03870667 0.40867981
 0.42284081 0.71306972 0.23503463 0.04614364]


'''


#kole jamesho bgiri
#hamashon ro

#np.sum() np.min()  np.max()  tohosn array
np.sum(L) #48.76081779543432
np.min(L) #0.038706672983148116
np.max(L) #0.9963212462513072



L.sum() #48.76081779543432
L.min() #0.038706672983148116
L.max() #0.9963212462513072




#too in datana -->statiscto --> yek bodi nist

L2 = np.random.random((2,3))

print(L2)
'''
            soton0      soton1       soton2
radif0  [[0.43123905   0.11408909   0.32224427]
radif1 [0.71701833    0.80749121    0.53378818]]

'''

L2.sum() #2.925870129555811

L2.sum(axis=0) #array([1.14825738, 0.9215803 , 0.85603246])

L2.sum(axis=1) #array([0.86757241, 2.05829772])




L2.min() #0.11408908790960137 beyne 6 


L2.min(axis=0)
#array([0.43123905, 0.11408909, 0.32224427])

L2.min(axis=1) #array([0.11408909, 0.53378818])




#statistic --> np.()    array.
#inha bayad bdonid kolie , baraye 2d
#ba axis --> riz tar besjhid tooye rows and columns
#----- SUm ,....

#tavabe dg
np.var() #sum of elements
np.prod() #product of elemnts
np.std()  # compute standad deviation
np.var()  #variance
np.min()
np.max()
np.argmin() #find the index of min
np.argmax() #find the index o max
np.mean()
np.median()
np.percentile()
np.any()
np.all()


a=np.arange(0,10)

np.mean(a) # 4.5
a.mean() #4.5



#------
#np.sort()
#np.sort(x,axis=0)





#-------------------------------------------------------
#-------------Iterating over array elements------------
#-------------------------------------------------------

v = np.array([1,2,3,4])

for element in v:
    print(element)

'''
1
2
3
4

'''


#------2D

M = np.array([[1,2],[3,4]])
print(M)
'''
radif 0 --> [[1 2]
radif1 --> [3 4]]

'''

#b adad 3 ??
#kodom radif --: 1
#toye radif 1 --> sotone 0 

#1 , 2 , 3 ,4

for chiz in M:
    print(chiz)

'''
[1 2]
[3 4]

'''


for x in M:  
    print('row:',x)

'''
row: [1 2]
row: [3 4]

'''

#-----

for row in M :
    print('row:',row)
'''
row: [1 2]
row: [3 4]
'''




for row in M :
    #hala row yek np.array 1D
    for element in row:
        print(element)

'''
1
2
3
4

'''





C3 = np.array([  [[1,2,3],[4,5,6]] , 
               [[7,8,9],[10,11,12] ] ,
               [[13,14,15],[16,17,18]]  ])

C3.ndim #3
C3.shape #(3,2,3)


for chiz in C3:
    print('=========')
    print('khode chiz:',chiz)
    print('type e chiz:',type(chiz))
    print('dimension e chiz',chiz.ndim)


'''
=========
khode chiz: [[1 2 3]
 [4 5 6]]
type e chiz: <class 'numpy.ndarray'>
dimension e chiz 2

'''

for matrix in C3:
    for row in matrix:
        print(row)
        print('--')
'''
[1 2 3]
--
[4 5 6]
--
[7 8 9]
--
[10 11 12]
--
[13 14 15]
--
[16 17 18]
--

'''
for matrix in C3:
    for row in matrix:
        for element in row:
            print(element)
        
        
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

'''


#radife felan , sotone felan
M[2,1]


#kodom table, radif , kodom soton
C3[1,2,2]



#d4[kodom 3d , kodom table, kodom radif, kodom soton]


#for 3d in 4d:
    #for matrix in 2d:
        #for row in matrix:
            #for element in row:
                #print(element)
                
    
    
    
Matrix = np.random.uniform(10,20,(4,5))

print(Matrix)

'''
[[10.7101504  10.9931878  19.36326489 12.57765563 10.40385527]
 [11.30634037 18.09112736 18.75921809 19.03509636 19.2634681 ]
 [19.5841465  19.01956689 18.80846765 13.94746962 10.35346747]
 [17.65658903 12.38961262 19.73570548 11.68273099 19.60990709]]


'''

#kodomeshon balaye 15 hastan ?? bekeshameshon biron
#avalin fore --> radifo 
#dovomiin for ->elemtn mide
mylist=[]
for row in Matrix:
    for element in row:
        if element>15:
            mylist.append(element)
            


print(mylist)
'''
[19.363264891938712, 18.091127363963125, 18.759218093195543, 19.035096363034956, 19.263468102884477, 19.584146501415404, 19.019566889061757, 18.808467650353343, 17.656589025143113, 19.73570547891891, 19.609907091633232]

'''

mylist=[]
for row in Matrix:
    for element in row:
        if element>19:
            mylist.append(element)
            

if len(mylist)!=0:
    print('failed')
            
#failed





Matrix>19
'''
array([[False, False,  True, False, False],
       [False, False, False,  True,  True],
       [ True,  True, False, False, False],
       [False, False,  True, False,  True]])
'''


if (Matrix>19).any():
    print('failed')

#failed










#ITERATION--> chekhabare
#-->Python --> konde , code bznid

#On tavabe ee k numpy behet --> C++ , tonde, Code

Matrix[Matrix>15]
'''
array([19.36326489, 18.09112736, 18.75921809, 19.03509636, 19.2634681 ,
       19.5841465 , 19.01956689, 18.80846765, 17.65658903, 19.73570548,
       19.60990709])

'''



#-------------------------------------------------------
#-------------JOINING ANS SPLITTING---------------------
#-------------------------------------------------------

#hol nashid azizan
#rok --> bad inhame sal --> In tike sakhte
#etsefade ziad shayad nashe

#Nabayad hame ye tavabe ro ghefz koni
#ghavanino hefz kondi


a=np.array([10,20,30,40])
b= np.array([100,200,300,400])

print(a) #[10 20 30 40]
print(b) #[100 200 300 400]


'''
[10 20 30 40]
[100 200 300 400]




[10  100]
[20  200]
[30  300]
[40  400]

'''
#dota argumente jodan
#np.concatenate(a,b) -->eshtebah

c= np.concatenate((a,b))

print(c)
#[ 10  20  30  40 100 200 300 400]

c= np.concatenate((a,b),axis=0)
print(c)
#[ 10  20  30  40 100 200 300 400]

#c=np.concatenate((a,b),axis=1)


#reshape()

c.reshape(2,4)
'''
array([[ 10,  20,  30,  40],
       [100, 200, 300, 400]])

'''




c.reshape(4,2)
'''
array([[ 10,  20],
       [ 30,  40],
       [100, 200],
       [300, 400]])

'''



#-----------3D---------



a=np.array([10,20,30,40]).reshape(2,2)
b= np.array([100,200,300,400]).reshape(2,2)

print(a)
'''
[[10 20]
 [30 40]]

'''

print(b)

'''
[[100 200]
 [300 400]]
'''




'''
[[10 20]  [[100 200]
 [30 40]]   [300 400]]




[[10 20]
 [30 40]]
[[100 200]
 [300 400]]

'''

c = np.concatenate((a,b))
print(c)
'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]


dar toole *radif* ha inkaro anjam mide

'''

c = np.concatenate((a,b),axis=0)
print(c)

'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]
'''



c = np.concatenate((a,b),axis=1)
print(c)
'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]

'''





#-------------------------
#vstack
#vertical stack --> vertical --> amodi

x = np.array([1, 2, 3])
print(x)
#[1 2 3]

grid = np.array([[9, 8, 7], [6, 5, 4]])
print(grid)
'''
[[9 8 7]
 [6 5 4]]
'''

np.vstack([x, grid])
'''
array([[1, 2, 3],
       [9, 8, 7],
       [6, 5, 4]])

'''




#------

np.hstack((x,grid)) #errror

a=np.array([10,20,30,40]).reshape(2,2)
b= np.array([100,200,300,400]).reshape(2,2)

np.hstack((a,b))
'''
array([[ 10,  20, 100, 200],
       [ 30,  40, 300, 400]])

'''



#d --> omgh 




#-----

x = [1, 2, 3, 99, 99, 3, 2, 1]

a = np.split(x,(3,5))


print(a)
#[array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]




#-------repeat
a= np.array([[1,2],[3,4]])

np.repeat(a,3)

#array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])




#_----RESHAPE() estefade konid






#--BLOCK [[optional]]

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a)
'''
[[1 2]
 [3 4]]
'''


print(b)
'''
[[5 6]
 [7 8]]

'''
'''

[[1 2]
 [3 4]]
        [[5 6]
         [7 8]]

[[1 2]   0  0
 [3 4]]  0   0
  0  0  [[5 6]
  0  0  [7 8]]



'''

result = np.block([
    [a, np.zeros((2,2))],
    [np.zeros((2,2)), b]
])

print(result)

'''
[[1. 2. 0. 0.]
 [3. 4. 0. 0.]
 [0. 0. 5. 6.]
 [0. 0. 7. 8.]]

'''



#-----Nokteye akahr -->reshape yechizi dare --> -1

import numpy as np

a= np.arange(10,410,10)
print(a)


a.shape # (40,)




#ag daghigh begam 4 radif , 10 sotone mikham
#a.reshape(radif, soton)
#a.reshape(4,10)


#man mikham b 4 radif tabdileshkonm --> 

#size = radif x soton

#1----usage

b=a.reshape(4,-1)

b.shape #Out[218]: (4, 10)


c= a.reshape(-1,4)
c.shape #Out[220]: (10, 4)


#2-usage

#bebin kh az tavabe k mirim joltar
#strciitan --> rooye shape e np arrayi k bdsoraste
#vorodi dakheel yek tabe mikoni

#sklearn --> tavabe dae --> np array migire
#guire rooye chi?
#rooye shape array --> error --> errore 


a = np.array([1,2,3,4,5,6,7,8,9,10])
a.shape #Out[222]: (10,)
a.ndim #1


#2 bodu --> 2 bodi?
# 10 ta soton tabdil koni 1 radis

#1,2,3,4,5,6,7,8,9,10
#(1,10)



#10 ta radi 1 soton
'''
1
2
3
4
5
6
7
8
9
10

(10,1)
'''


#*****
#1 bodio --> 2 bodi tabdil mikonan


#1 done radif
a.reshape(1,-1)


#1 doone soton
a.reshape(-1,1)






#-----------------
''' Linear Algebra 
'''
#-----------------

'''

Linear_algebra.py --> Numpy, scipy , sympy ro tadris konim

Mogahdame bar ML 

Hooshe masnoee
MATRIX()
100 khat

'''



#==============
#==============
#==============

'''
Practical Notes
'''



'''

radif mohem ahs --> aval radif --> ...

np. external , inside method

tavabe -> yek nparay -->moghaye yek adad
tavabe --> dota np array moghayese koni


tavabe , .. --> 1D , 2d (3d,....)
1d -->y result
a.min() y adad mide --> [10,20,30,40]

2d --> y result  [radif, soton]
min -->kole --> toohar sootn , har radifi --> axis





Nokte --> Tamrin 

kole numpy shoam mitoni?
se barbaare inam bkhjni -> 5% numpy balad bashi


90% e usage e numpy 




tabeye concat -> besorate bydefaul -->dar rastaye **radif** ha maiayad michinad
ama dar 1D -->asan masale radifo soton nis -> 1d --> poshte ham michaboaanrsh
'''






#--------------------------TAMRIN -----------------------------


'''

Gorohe quiz , tamrin

1-  tabe haye advance python , python built in fucntion
hame bayad yekbar test shode bashe tooye yek file .py
tozih


2---> Anvae Error haro 15 ta test mikrdid


3---> class , property() , classmethod() staticmethod()



4---> Numpy_practice.py --> 
numpy chiast (gpt ham komak bgirid)
darsname benevisid
pip install ,...

np.array
#....

tabe ha ,......







#------bayad kard

github --> repo 

#--------global ------
github.com

roo domeye sabz

esm --> AI_esmeton , ai_ -->namayesh dade she

read me ro bazesh kon --> commit mikhore (git init) mikhore

[chon dg niaz nis shoma git init , git remote ,...]

rooye dokemye sab --> code

-->ye url --> copy mikoni
https://github.com/APMaii/ai_tutorials_2026.git

yani dar asl

https://github.com/{{id shoma}}/{{esme repo e shoma}}.git



#----terminal baz , git bash

(base) apm@APMs-MacBook-Pro ~ % pwd
/Users/apm


boro desktop

(base) apm@APMs-MacBook-Pro ~ % cd desktop
(base) apm@APMs-MacBook-Pro desktop % pwd
/Users/apm/desktop

az git clone https://///


(base) apm@APMs-MacBook-Pro desktop % git clone https://github.com/APMaii/ai_tutorials_2026.git
Cloning into 'ai_tutorials_2026'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.


ino miriz ejaee k bodid



hala boro into codeto besaz
ba  new file save

touch file.py ,....



badesh boro dakhelesh 
(base) apm@APMs-MacBook-Pro desktop % cd ai_tutorials_2026
(base) apm@APMs-MacBook-Pro ai_tutorials_2026 % 



vaghy  4 ta file ro sakhti
ya asan ydone file ro skahti ya harchi


git status --> file k sakhti barat miad 

(base) apm@APMs-MacBook-Pro ai_tutorials_2026 % git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean




git add python_function.py

git status --> az ghermez --> sabz motmaen sho

git commit -m 'file e python funciton'

tooye laptsbt sabt shod


git push origin 
#mire github 





#-----frda bidar mishi
file jadideto besaz karato kon

git status

ghermez 
advanced_class.py


git add advanced_class.py

git sdtatus --> ghermesz sabz
git commit -m 'file advance ra sakhte am'

git push origin main
git push
git push origin


#-----
do nfrid , 
ghabel inakra
git pull origin --> motmaen shi hamechio grfti




'''

