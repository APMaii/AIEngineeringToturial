"""
In The Name Of God

Created on Fri Jun  5 11:24:09 2026

@author: Ali Pilehvar Meibody

Look at this file after AI_Pandas.py




-------------------------
Bad az inke Pandas ro yad grftim
hala mibinim vagehan koja az pandas estefade mikonim?


Dar asl ghabl az inke varede Machine learning (deep learning)
AI beshim, vase harkari har computation



Data analysis, Data cleaning , Feature engineering --> ML WORKFLOW



Data tamiz bashe 

"""

#fileton --> sotone az dade
#azmayeshgah , (tajrobi , engineering)
#file --> download, website , .. data collect jam

#data --> chijori jam koni, source daran, API , database zakhire
#-------> scrap (gheyre ghanonoi)


#.csv --> read_csv
#.xls .xlsx ---> read_excell

#Datat tooye computeret ---> Pandas DataFrame

#data_15khordad.xlsx




import pandas as pd

data = pd.read_excel('/Users/apm/Desktop/data_15khordad.xlsx')


data.head()

'''
   dama feshar  estehkam
0  40.0     1'     400.0
1  50.0     2'     500.0
2  60.0     3'     600.0
3  70.0     4'     700.0
4  80.0     5'       NaN

'''

data.head(6)
'''
   dama feshar  estehkam
0  40.0     1'     400.0
1  50.0     2'     500.0
2  60.0     3'     600.0
3  70.0     4'     700.0
4  80.0     5'       NaN
5  90.0     6'     900.0

'''


data.tail()
'''
     dama feshar  estehkam
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8     NaN     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''


data.tail(6)
'''
     dama feshar  estehkam
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8     NaN     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''




data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      10 non-null     float64
 1   feshar    11 non-null     object 
 2   estehkam  10 non-null     float64
dtypes: float64(2), object(1)
memory usage: 392.0+ bytes



In yek file hast , zarfe data --> dataframe az pandas
11 ta radif dare k az 0 ta 10 index khorde
3 ta soton dare

har soton gofte  , typesh , non-null

null-->khali 

'''


data.describe()
'''
soton haee k Numbers()

             dama    estehkam
count   10.000000    10.00000
mean    87.000000   870.00000
std     35.605867   305.68684
min     40.000000   400.00000
25%     62.500000   625.00000
50%     85.000000   950.00000
75%    100.000000  1075.00000
max    160.000000  1300.00000

'''

#soton jensiat , mard mard mard zan 
#chanta chanta zan

data.value_count()



#----- .describe() .value_count() rooye soton hambzni

data['dama'].describe()

'''
count     10.000000
mean      87.000000
std       35.605867
min       40.000000
25%       62.500000
50%       85.000000
75%      100.000000
max      160.000000
Name: dama, dtype: float64

'''

data['dama'].max() #160.0
data['dama'].min()
data['dama'].mean()
data['dama'].sum() #870.0
'''
soton .function()  -->roo kole baray eghar soton

.mean()   average
.sum()   total sum
.count()
.min()
.max()
.median() 
.std()     standard eviation







Che etefaghi miofte k data momkene salem nabashe
4 ta etefagh drim k age etfagh biofte yani
data niaz dare be cleaning

1-Tashkhis bdim
2-Hale konim mozo (data ro clean konim)


'''


#----------4 ta moshkele data
#-----1- Empty celll
#-----2-wrong format
#----3-logical
#----4-Duplicated


print(data)

#inja data kame ama ag ziad bashe vase didnsh vase hmain
#az head() tail() estefade mikone

#==========================
'''  1- Empty cell  '''
#==========================
#yeki az adad ha k 
#Nan Not a number
#y frd excel misakhte , havasesh khali bode
#ya dashte moshkele ata , save dashte hard moshkele narm afzar 
#vaghty dashte -->comapitble ono khali nshon mdie

#source enssan, computer --> man dar data yekchizi drm NaN not a number 
#kahli --> empty cell

#number mifahme adasd mifhme -->khali bokhore rrror mikhore kole porozhat


#1-Taskhis bdm ino


data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      10 non-null     float64
 1   feshar    11 non-null     object 
 2   estehkam  10 non-null     float64
dtypes: float64(2), object(1)
memory usage: 392.0+ bytes


11 ta radif dari  -->bayad hame sotonat 11 ta non-null

sotone dama --> 10 non-null  --> 1 null
feshar okeye
estehkam --> 10 non-null --> 1 null

2 ta empty cell

'''

print(data)

'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'       NaN
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8     NaN     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''



#yek raveshe dg
data.isnull()
'''
     dama  feshar  estehkam
0   False   False     False
1   False   False     False
2   False   False     False
3   False   False     False
4   False   False      True
5   False   False     False
6   False   False     False
7   False   False     False
8    True   False     False
9   False   False     False
10  False   False     False


zmaani k data kamw mishe did (to khdoet print)
'''

data.isnull().sum()
'''
dama        1
feshar      0
estehkam    1
dtype: int64

'''

#daghigh bbini kojan in nulla
#recommended nist
data.isnull().sort_values(by='dama',ascending=False)
'''
     dama  feshar  estehkam
8    True   False     False
0   False   False     False
1   False   False     False
2   False   False     False
3   False   False     False
4   False   False      True
5   False   False     False
6   False   False     False
7   False   False     False
9   False   False     False
10  False   False     False

'''




'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'       NaN
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8     NaN     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''


#droos konim moshkelo??
#avalish ine bgi

#data.drop(column , index) specific 

#drop n a number

data.dropna()  #data.dropna(inplace=True)
'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''
data['dama'].dropna()
'''
0      40.0
1      50.0
2      60.0
3      70.0
4      80.0
5      90.0
6     100.0
7     120.0
9     160.0
10    100.0
Name: dama, dtype: float64

'''

#hazinash --> loste data , loste information

#age data b andaze kafi dari --> dropna()

#ag datat kame hasase, vase hardonash ahzine shdo va ...



#fillna()

print(data)

'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'       NaN
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8     NaN     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''

data.fillna(10) #inplace=True
'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'      10.0
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8    10.0     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''

#adad bdm

dama_mean = data['dama'].mean()
print(dama_mean) #87.0

data.fillna(dama_mean) #inplace=True
'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'      87.0
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8    87.0     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''


#ordinal --> tartibi

#harja k didi 

data.fillna(method='ffill') #az ghabli
'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'     700.0
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8   120.0     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''



data.fillna(method='bfill')
'''
     dama feshar  estehkam
0    40.0     1'     400.0
1    50.0     2'     500.0
2    60.0     3'     600.0
3    70.0     4'     700.0
4    80.0     5'     900.0
5    90.0     6'     900.0
6   100.0     7'    1000.0
7   120.0     8'    1100.0
8   160.0     9'    1200.0
9   160.0    10'    1300.0
10  100.0     7'    1000.0

'''




#==========================
'''  2- Wrong format  '''
#==========================

#time -> str 
#adad --> str
#float --> .. 

data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      10 non-null     float64
 1   feshar    11 non-null     object 
 2   estehkam  10 non-null     float64
dtypes: float64(2), object(1)
memory usage: 392.0+ bytes


dama flaot, estehkam flat

feshar --> object ?????
'''

yekdane=data['feshar'].loc[0]

print(type(yekdane)) #<class 'str'>

print(data['feshar'].loc[0]) #1'



#source --> alan ina str zakhrie shod
print(data)

data.head()
data.tail()


#str --> numeric()

data['feshar'] = pd.to_numeric(data['feshar'])

#1'   '1'

data['feshar'] = data['feshar'].astype(int)
data['feshar'] = data['feshar'].astype(float)

#----- str --> date time
data['time'] = pd.to_datetime(data['time'])








#--------- Advanced -->
value = "salam ' "
print(value) #salam '

value.replace("'","") # 'salam  '



data['feshar'] = data['feshar'].apply(lambda x : x.replace("'",""))


data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      10 non-null     float64
 1   feshar    11 non-null     object 
 2   estehkam  10 non-null     float64
dtypes: float64(2), object(1)
memory usage: 392.0+ bytes

'''

data['feshar'] = pd.to_numeric(data['feshar'])


data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      10 non-null     float64
 1   feshar    11 non-null     int64  
 2   estehkam  10 non-null     float64
dtypes: float64(2), int64(1)
memory usage: 392.0 bytes

'''




#==========================
'''  3- Logical '''
#==========================
data.describe()

'''
             dama     feshar    estehkam
count   10.000000  11.000000    10.00000
mean    87.000000   5.636364   870.00000
std     35.605867   2.907670   305.68684
min     40.000000   1.000000   400.00000
25%     62.500000   3.500000   625.00000
50%     85.000000   6.000000   950.00000
75%    100.000000   7.500000  1075.00000
max    160.000000  10.000000  1300.00000



.apply() too sootoon
filtering

'''

data[data['dama']<=100]
'''
     dama  feshar  estehkam
0    40.0       1     400.0
1    50.0       2     500.0
2    60.0       3     600.0
3    70.0       4     700.0
4    80.0       5       NaN
5    90.0       6     900.0
6   100.0       7    1000.0
10  100.0       7    1000.0

'''


data = data[data['dama']<=100]

print(data)

'''
     dama  feshar  estehkam
0    40.0       1     400.0
1    50.0       2     500.0
2    60.0       3     600.0
3    70.0       4     700.0
4    80.0       5       NaN
5    90.0       6     900.0
6   100.0       7    1000.0
10  100.0       7    1000.0

'''




#===================================
'''  4- duplciated (tekrari) '''
#===================================

#ejaze dari k tekrari bashe data yana?
#kole radif manzore

#ejazash hast --> beza bashe 


data.drop_duplicates(inplace=True)

print(data)
'''
    dama  feshar  estehkam
0   40.0       1     400.0
1   50.0       2     500.0
2   60.0       3     600.0
3   70.0       4     700.0
4   80.0       5       NaN
5   90.0       6     900.0
6  100.0       7    1000.0

'''


#specific 
#data.drop_duplicates(subset=['dama'],inplace=True)

#ID , SHOMARE MELI , ...




data.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 7 entries, 0 to 6
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      7 non-null      float64
 1   feshar    7 non-null      int64  
 2   estehkam  6 non-null      float64
dtypes: float64(2), int64(1)
memory usage: 224.0 bytes

'''



data.fillna(method='ffill',inplace=True)


data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   dama      7 non-null      float64
 1   feshar    7 non-null      int64  
 2   estehkam  7 non-null      float64
dtypes: float64(2), int64(1)
memory usage: 296.0 bytes
'''



data.reset_index(drop=True,inplace=True)

data.head()
'''
   dama  feshar  estehkam
0  40.0       1     400.0
1  50.0       2     500.0
2  60.0       3     600.0
3  70.0       4     700.0
4  80.0       5     700.0

'''

data.tail()

'''
    dama  feshar  estehkam
2   60.0       3     600.0
3   70.0       4     700.0
4   80.0       5     700.0
5   90.0       6     900.0
6  100.0       7    1000.0

'''




data.to_excel('/Users/apm/Desktop/cleaned_data_15khordad.xlsx')



after_day_data= pd.read_excel('/Users/apm/Desktop/cleaned_data_15khordad.xlsx')

 
after_day_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Unnamed: 0  7 non-null      int64
 1   dama        7 non-null      int64
 2   feshar      7 non-null      int64
 3   estehkam    7 non-null      int64
dtypes: int64(4)
memory usage: 352.0 bytes

'''


#esame ye majeera --> scaling, statistic ,feature engineering , ..--> Machine learning



