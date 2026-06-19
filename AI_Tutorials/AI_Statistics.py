
"""
In The Name of God 

Created on Fri Jun 12 08:58:21 2026

@author: Ali Pilehvar Meibody


AI_Statistics.py

"""


#==========================================
#==========================================
#==========================================

'''
 =========== Review of Pandas ================


List --> Multiple variables store (save) -->  a= [el1,el2,el3,..]   a[index]  a.append()

Fast, calculation , C++ baxckend
Numpy array --> np.array([1,2,3,4]) , np.array([[cl1,cl2,cl3],[row2]])


Label dashte bashim, data anajm bdim

import pandas as pd

a=pd.Series([1,2,3,4])
a.loc[] #label
a.iloc[] #index

a.min() a.max() ,.......


2D like table
a=pd.DataFrame([[cl1,cl2,cl3,..],[row2],[row3]],columns=[label_column,...] , index=)

a['esme_soton']

a.loc[]
a.iloc[]


a[esme sotoon]


a[esme soton].loc[]
a[esme soton].iloc[]



a>100 --> pandas --> [true false,]

filterin_list=[]
a[filktering list]


a[a>100]

b = a[a['feshar']>100]

a['new_column'] = 

a.drop(....)

inplace = False zarf mizashti jolo (default)
Inpalce = True --> emal mishod

Ta inja bood ai_pandas.py
Badesh ai_pre_processing.py


df = pd.read_excel(address.xls  .xlsx )
data = 

pd.read_csv(address.csv)

kole datato be Dataframe tabdil mikone

data.columns
data.head(6) 6 radife aval
data.tail(6)  6 radife akhar
data.info() --> non nulll, type ,...
data.describe() amare mean, max , min soton
data.value_count()

data.mean()  data['dama'].mean() .max() .min() 

4 no khata darim k ghabvl az anjame harka rbayad clean beshe

1---------Empty cell (NaN)
data.info() --> chan radif drim , too ahr sootn chnata non-null drim
non-null < radifa 

data.isnull().sum()

data.dropna(inplace=True)  hazf mikone

data.fillna(adad,inplace=True)  adad= data['feshar'].mean()
data.fillna(method='ffill') # az ghabli
data.fillna(method='bfill') # az badi avrdare


2-------------wrong type
data.info() --> joloye har soton

data[column] = pd.to_numeric(data['column'])
pd.to_datetime()

data[colujmn] = data[column].astype(int)  .astype(str)  .astype(float)


3--------logical
data[data[feshar]<100]

data[data[dama]>0]
.apply()

4-----duplciated (tekrari)

data.drop_duplicates(inplace=True)



4 ta khata ro peyda krdi va raf krdi, index habeham rikhte bashe

data.set_index(drop=True,inplace=True)


data.to_excel('.......esm')
data.to_csv('.......User/apm/desktop/cleand_data.csv')



'''


#==========================================
#==========================================
#==========================================

'''
we trust in god, others must bring data

========= AI Statistics =================

Study of data , be ma komak mikone ke betoonim dade haro analyze konim va dark konim

1- Descriptive statitics (amare tosifi) - summurize data (min , max , count , mode , median , standard deviation)

2- inferential statistics (amare estenbaty) - making prediction from data 


import numpy as np
import pandas as pd
import scipy.stats as stats


'''

import numpy as np
import pandas as pd
import scipy.stats as stats

a = np.arange(1,401) #1 to 400

len(a)

b = a.reshape(100,4)

b[0:4,:]

'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])

'''

data = pd.DataFrame(b,columns=['feshar','dama','time','estehkam'])

data.columns #Out[9]: Index(['feshar', 'dama', 'time', 'estehkam'], dtype='object')

data.head()
'''
   feshar  dama  time  estehkam
0       1     2     3         4
1       5     6     7         8
2       9    10    11        12
3      13    14    15        16
4      17    18    19        20

'''


data.tail()
'''
    feshar  dama  time  estehkam
95     381   382   383       384
96     385   386   387       388
97     389   390   391       392
98     393   394   395       396
99     397   398   399       400

'''


#Descriptive statitics


data.describe()

'''
           feshar        dama        time    estehkam
count  100.000000  100.000000  100.000000  100.000000
mean   199.000000  200.000000  201.000000  202.000000
std    116.045968  116.045968  116.045968  116.045968
min      1.000000    2.000000    3.000000    4.000000
25%    100.000000  101.000000  102.000000  103.000000
50%    199.000000  200.000000  201.000000  202.000000
75%    298.000000  299.000000  300.000000  301.000000
max    397.000000  398.000000  399.000000  400.000000

'''

np.mean(data) #200.5

#mianging
np.mean(data['feshar']) # 199.0

#[1 , 4 , 5 , 6 , 7]
#median
np.median(data['feshar']) #199.0

#bishtarin tekrar ro shode
stats.mode(data['feshar']) #ModeResult(mode=1, count=1)

#range
max(data['feshar']) #397
min(data['feshar']) #1

data_range = max(data['feshar']) - min(data['feshar'])

print(data_range) #396


#az 1 ta 397
#mean --> 199


#dataham az mianginam cheghadr parakandan .
#[200, 201 , 202, 198 , 197 ]

#[1 , 2, 3, 4


#variance , standard deviation

#Variance = Standard deviation **2


variance_value = np.var(data['feshar'], ddof=1)

print(variance_value) #13466.666666666666

generated_good_focused_data = np.random.normal(199,5,(100,))

print(generated_good_focused_data)

np.var(generated_good_focused_data,ddof=1) #25.646069656108594



#-------

np.std(data['feshar'],ddof=1) # 116.04596790352807


#116.04596790352807 *  116.04596790352807 = 13466.666666666666
#Variance = std **2


import matplotlib.pyplot as plt

plt.hist(data['feshar'],bins=100 , color='blue')
plt.title('histogram of dsata')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show()



plt.hist(generated_good_focused_data,bins=100 , color='blue')
plt.title('histogram of dsata')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show()



#=========================
#Probability - Ehtemalat

'''

cheghadr ehtemal dare yek event (etefagh) bioftad , 0 (impossible) to 1 (certain)

Experiment --> endakhtane tas
sample space (s) --> possible outcompe {1,2,3,4,5,6}
event (e) --> made nazar , {1}  , {2,4,6} ,{1,5,6} , {1,6}
probability of eveent --> P(e)

P(e) : Favorable outcomes / all events

'''


#tozi darim -> distributions darim tood ata
#k mige chghd hardata ee frequency (tekrar shode)


#----Uniform distribution ---------
#data ee darim, k hame tedadeshon dar yek dade yeksane
#randoms elct koni, ehtemale inke harkodom ro vardari 1 

data = np.random.uniform(5,40,size=(100,))


plt.hist(data,bins=20)
plt.title('uniform distributions')
plt.xlabel('data')
plt.ylabel('frequency (probability)')
plt.show()




data = np.random.uniform(5,40,size=(1000,))


plt.hist(data,bins=20)
plt.title('uniform distributions')
plt.xlabel('data')
plt.ylabel('frequency (probability)')
plt.show()




data = np.random.uniform(5,40,size=(100000,))


plt.hist(data,bins=20)
plt.title('uniform distributions')
plt.xlabel('data')
plt.ylabel('frequency (probability)')
plt.show()

#Tass --> Uniform
# agar yek tas , 1,2,3,4,5,6 yek ehtemal , khordgi, ideal

#1 ta 6 --> 1000000 bendazam

data = np.random.uniform(1,6,size=(10000,))


plt.hist(data,bins=6)
plt.title('uniform distributions')
plt.xlabel('data')
plt.ylabel('frequency (probability)')
plt.show()








#-----Normal (Gaussian) distribution -----
#Tabi ei bishtar shabihan

#aksare etefagh ha gaussian, normal hastan
#data ee dari az afrade jame e , az ghad

#ye ghadi miangin 175 afard hole mehvare 175 parakand mishan
#akasaran t oo focus dore 175 176 , 177 , 174

#189 , 2 metr . 150 bashan

#50% JAME ee dar hole mehvare 175

mu = 175  #miangin
sigma = 15 

normal_data = np.random.normal(mu,sigma,10000)

plt.hist(normal_data,bins=30)
plt.title('normal distribution')
plt.xlabel('value')
plt.ylabel('density')
plt.show()





#binominal distribution----------------
n, p = 10, 0.5  # 10 trials, 50% success chance
binom_data = np.random.binomial(n, p, 1000)

# Plot binomial distribution
plt.hist(binom_data, bins=10, edgecolor='black', density=True)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()




#poisson distribution----------------
#kh nader, pishbinie zelzele, ...
lambda_ = 2  # Average 2 events per time period
poisson_data = np.random.poisson(lambda_, 10000)

# Plot Poisson distribution
plt.hist(poisson_data, bins=15, edgecolor='black', density=True)
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.show()


'''
Normal --> Aksare data ha normal hastand

2 --> Test ( Z-test, t-test , Anova) --> Data Normal bashe

3---> Machine learning --> Datat Normal bashe

'''




#--------------------------------
#-------Normality Test------------
#--------------------------------


#----visual ------

import numpy as np
import matplotlib.pyplot as plt

# Generate normal data
data = np.random.normal(50, 10, 1000)

# Plot histogram
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()



#bell shape (zangoole) ---> Normal




#Box Plot --------------------------
#symmetric (motegharen)
plt.boxplot(data, vert=False)
plt.title("Box Plot")
plt.show()



#Q-Q plot--------------------------
import scipy.stats as stats
import matplotlib.pyplot as plt
# Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()






#KDE plot--------------------------
import seaborn as sns

sns.kdeplot(data, shade=True, color="blue")
plt.title("KDE Plot")
plt.show()




#----> Adad --> adadi mide bar asase oon tasmim migiiri 


#----Shapiro-wilk test
from scipy.stats import shapiro
data = np.random.normal(50, 10, 1000)

stat, p = shapiro(data)
print(f"Shapiro-Wilk Test: Statistic={stat}, p-value={p}")

'''


H0 : data is normal
H1 : data is not normal
    
    
--> shapir_state (T,Z,...) --> p 

p<0.05 --> reject H0 --> reject normal --> normal nist
p>0.05 --> fail to reject H0 --> normale



'''

#p_value=0.7820693254710884


#p_value > 0.05 ? --> Fail to reject H0 -->fail reject normal bodan
#--> bepaziram --> normal hast. visual nagoftm , ba adad daram migm



data2 = np.random.uniform(1, 100, 1000)

from scipy.stats import shapiro
state , p_value = shapiro(data2)


print(p_value)
#8.214666204034599e-16
#8 * 10*-16


#if p_value <0.05 --> reject H0 (normality data) normal nist
#if p_value >0.05 --> fail to rejhect --> nromale

if p_value<0.05:
    print('normal nist')
else:
    print('normal hast')

#normal nist





#-----anderson darling
from scipy.stats import anderson

result = anderson(data)
print(f"Anderson-Darling Test Statistic: {result.statistic}")
#Anderson-Darling Test Statistic: 0.2524234094341864


for i in range(len(result.critical_values)):
    sig_level = result.significance_level[i]
    crit_val = result.critical_values[i] #p_value
    if result.statistic < crit_val:
        print(f"Accept normality at {sig_level}% level")
    else:
        print(f"Reject normality at {sig_level}% level")


'''
Accept normality at 15.0% level
Accept normality at 10.0% level
Accept normality at 5.0% level
Accept normality at 2.5% level
Accept normality at 1.0% level
'''




from scipy.stats import anderson

result = anderson(data2)
print(f"Anderson-Darling Test Statistic: {result.statistic}")
#Anderson-Darling Test Statistic: 0.2524234094341864


for i in range(len(result.critical_values)):
    sig_level = result.significance_level[i]
    crit_val = result.critical_values[i] #p_value
    if result.statistic < crit_val:
        print(f"Accept normality at {sig_level}% level")
    else:
        print(f"Reject normality at {sig_level}% level")

'''
Anderson-Darling Test Statistic: 9.781214910060385
Reject normality at 15.0% level
Reject normality at 10.0% level
Reject normality at 5.0% level
Reject normality at 2.5% level
Reject normality at 1.0% level

'''



#1---> farze khetli az test ha inke data baaydnormal bashe
#2-->age nabod chi?








#======================================
#----WHAT CAN WE DO IF TEH DATA IS NOT NORMALL????
#======================================
#Agar normal nabood ---------------------

#To log ---> LOgnormal 
import numpy as np
data_log = np.log(data)  # Apply log transformation
#data_log



#-------Square Root Transformation-------
data_sqrt = np.sqrt(data)
#Test normality --> bejaye data , data_sqrt , data_log


#-------Yeo-Johnson Transformation-------
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
data_yeo = pt.fit_transform(data.reshape(-1, 1))






#=========================================
'''
Quality control in material engineering

Quality control , amari --> 7,8 Ta test hadeagahal --> 50,60 teste amar tarif mikonan

Z-test , T-test , F-test , one-smaple Z-test , two-sample z-test , one-sample  t -test
anderson-darkling test, Bartlett’s Test c, Welch’s t-test 





------Hypothesis Testing----------
1 farz , farze batelesho dar nazar migi

H0 : Null hypothesis : No effect / diffeerence

H1` : Alternative hypothesis : There is effect/difference


Population --> class python 50 nafar
sample ->  AI class ( 10 nafar)


Mesal --> agha in goroh miangine seni 27

H0 : Mean_group = 27
H1 : Mean_group != 27


gorohe python , gorohe AI.

miangine ghadi python < miangine gahdi toye gorohe AI

H0 : Mean_python_height < Mean_Ai_height

H1 : Mean_python_height > Mean_Ai_height




dakhelesh , probability , mohasebta , chnbar tekrar mishe
criteria , T , Z , F ,.... --> P

alpha --> hade 0.05 , 0.10 , 0.15 
Shekrat taen mikone, yek ostadi  , yek company , khodet , standarde jahani 0.05 hade astane


P < 0.05 --> Reject Null hypothesis (H0)
P > 0.05 --> fail to reject null hypothesis (H0)

**0.05 manzoram alpha hast




Kholase ---> ma koli test darim , dar tamame in test haye amari
ma yek H0 darim k migim null hypothesis in hamon farzi hast k mikhahim
besanjimesh (no difference/no effect) , mirim testemon ro migirim
test yekseri calculation amari anajm mide k dar nahayt T , Z , F criteria
vali hamon tabdil mishe b yechizi bename P. 

Nesbat b alphaye taen shode (0.05)

agar p < 0.05 --> reject Null hypothesis --> farzi ro k dashti rad mishe
agar p > 0.05 --> fail to reject null hypothesi --> nemitoni rad koni, bepazirish



'''



'''
Darmorede miangine yek goroh ya dogoroh farzi koni Z test , t test
Miangin sakhte shode ast

farz --> Miangin = ....

1 sample --> 1 sample Z test , 1 sample t test
2 sample --> class A , class B  2 sample z test , 2 sample t test


Z test --> data hat bishtar az 30 ta bashe hadegahal, standard deviation class ro bdoni
T test --> data hat kamtar az 30 ta bashe , standard deviation unknown bashe


'''

#=========================================
'''        1- One sample Z test       '''
#=========================================

'''
Man yek sample daram (data) az ghade afrade yek class, nomrashon, vazneshon ,,....
estehkame yekseri nemonye material ,,......


Yek farzi mikoni [miangin nazar midi]


CLass A --> miangine class python 50 nafarim --> miangine class pyhton 50 nfrim
man migam miangine senish  26 hast


Hypothesis 

H0 Null hypothtesis --> Python_class_mean_age = 26
H1 Alternative hypothesis --> Python_class_mean_age != 26


P





Pish farz
Normality: The population follows a normal distribution.
Independence: Observations must be independent.
Known Population Variance 
Random Sampling: The sample must be randomly selected.
datat bayad bishtar az 30 ta nemone


'''

from statsmodels.stats.weightstats import ztest

#kole kelase ghabli
#az kole kelas ngrftm , sample grftm
#Miangiensho migrftm 
#*** man az kole class ngrftm ,
#yek sample az class grftm va mokham ba yek sample
#rajebe kole population ( jamiat) 


#sampel --> nemone ee k man daram
#population --> kole jame e k morede analysis ghrar mdiaham

sample_data = [23 , 27 , 30 , 35 , 46 , 16 , 22 , 30 ]


#
hypothesis_population_mean = 26

z_stat, p_value = ztest(sample_data, value=hypothesis_population_mean)

#z_stat --> criteria dakheli khode test hesab mikoni
#p_value mohem hast


print('p_value: ',p_value)
#p_value:  0.41624721334861114

alpha = 0.05

if p<alpha:
    print('null hypothesis is rejected')
else:
    print('fail to reject null  hypothesis')
    
    

#fail to reject null  hypothesis


#p --> 0.41  > 0.05 --> nemitonam farze 0 ro rad konam
#farze sefr chie?

#bar asase fght 8 nafar, rajebe kole class nazar dddm
#k ina seneshon miangin 26 e

#in farz rad nmitone beshe






#=========================================
'''        2- Two sample Z test       '''
#=========================================

'''

dota class dari , ghadashon 

500 nafar, 500 nafar --> jame ast (kole population)

30 nfr , 30 nfr   --> sample
170        174






ghade indota jame e shabihe ham hast ya nist mosavi hast 



H0 null hypothesis : mean_group_A = mean_group_B
h1 altenratibve hypothesis :mean_group_A != mean_group_B 


'''

sample1 = np.random.normal(170, 5, 30)
sample2 = np.random.normal(174, 5, 30)

z_stat, p_value = ztest(sample1, sample2)
print("Z-Statistic:", z_stat) # -3.2879442325938664
print("P-Value:", p_value) #0.0010092182860184493

alpha = 0.05
if p_value<alpha:
    print('null hypothesis is rejected')
else:
    print('fail to reject null  hypothesis')
    

#null hypothesis is rejected
# miangine ghadie in do goroh baham barabar nis


#bar asase sample, rajebe kole jamiat nazar midam --> Inference stenbat




#=========================================
'''        3- one sample T test       '''
#=========================================
#datahamon kamtar az 30 bashe, unknown standard deviation
from scipy.stats import ttest_1samp
sample = [22, 23, 19, 21, 25, 30, 24, 22, 27, 26]
t_stat, p_value = ttest_1samp(sample, 24)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

'''
T-Statistic: -0.09842680723871938
P-Value: 0.9237507005577772

'''



#=========================================
'''        4- Two sample T test       '''
#=========================================
from scipy.stats import ttest_ind

group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)

t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

'''
T-Statistic: -0.405853612224562
P-Value: 0.687126513753912

'''



#farze ---> Normal bashe
#shapiro-wilk
#anderson darling



#=========================================
'''        5- F test (variance comaprison)     '''
#=========================================
'''
ta alan shoma miangine dota population moghayese mikardi

az alan be bad mikhay parakandegishi  noghayese oni

Sample , sample 

H0 ---> Var1 = Var2
H1 --> VAR1 != VAR2



F = sigma1**2 / sigma2**2 --> distribution, rooye ,....
F --> P_value

if p_value <0.05 --> reject nul -> variance motefaveta



F test --> pishfarz
normal bashe data


'''

from scipy.stats import f

group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)

var1 = np.var(group1,ddof=1)
var2 = np.var(group2,ddof=1)


F_stat = var1 / var2
p_value = 1 - f.cdf(F_stat, len(group1)-1, len(group2)-1)

print('f-statictiscs : ',F_stat)
print('p-value :',p_value)


'''
f-statictiscs :  1.4953974780815125
p-value : 0.19415667914948775


p _value > 0.05 --> reject null  --> varianc deha barabaran
'''







#=========================================
'''     6-  Eqaulity of varianbces    '''
#=========================================
'''

Levene’s Test (Less sensitive to non-normality)


H0 --> V1 = V2
H1 --> V1 !=V2



P < 0.05 --> rejct null  (V1!=V2)
P>....
'''


from scipy.stats import levene

group1 = np.random.normal(50, 10, 100)  # Mean=50, Std=10, n=100
group2 = np.random.normal(55, 15, 100)  # Mean=55, Std=15, n=100

stat, p_value = levene(group1, group2)
print(f"Levene’s Test: Statistic={stat}, P-Value={p_value}")

'''
Levene’s Test: Statistic=17.795925732339168, 
P-Value=3.7410815898496045e-0

'''
alpha = 0.05
if p_value<alpha:
    print('variance barabar nist')
else:
    print('variance barabar hast')

#variance barabar nist




#=========================================
'''     7-  Not parametric tEST   '''
#=========================================
'''
Z test 1 sample, 2 sample
T test 1 smaple , 2 sample
F test ,... 

asssume qwe have normal data
if we donot have normal data we must go for
non-parametric tests -->
examples--> (mohem nis)



'''
#Bartlett’s Test
#Welch’s t-test 

#on-parametric test (Wilcoxon signed-rank test) --> Z test normal
#non-parametric test (Mann-Whitney U test) --> 2 sampel z test non aprmaetric
#i sample t test normal nabashe-> (Wilcoxon signed-rank test)
#2 sample test nromal nabashe --> Use Mann-Whitney U test or Permutation test


#=========================================
'''    8-  Correlation test    '''
#=========================================
'''

Kh baraton moheme k bedonid aya
sotoni ba sotoni mortabet hast? correlation dare?


feshar ziad she, estehkam ham mortabet hast ??? 



Correlation test 




pishfarz

Linearity: The relationship must be linear (Check using a scatter plot).
Normality: Both variables should be normally distributed (Check using Shapiro-Wilk test).
Homoscedasticity: The variance of  Y should be similar across all X values (Check using Levene’s test).
Independence: Observations must be independent of each other.




'''
#data = pd.DataFrame(b,columns=['feshar','dama','time','estehkam'])


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate data
np.random.seed(42)
x = np.random.normal(50, 10, 100)  # Normally distributed X
y = 2*x + np.random.normal(0, 5, 100)  # Linear relationship with noise




#1------> linearity
plt.scatter(x, y)
plt.title("Scatter Plot (Check Linearity)")
plt.show()



#2--checdk normality

plt.hist(y,bins=20)
plt.show()

plt.hist(x,bins=20)
plt.show()

from scipy.stats import shapiro



shapiro(x).pvalue #0.6551676754215167 > 0.05 --> Fail to reject H0 --> Normal

shapiro(y).pvalue #0.9501836786075823



#3--
residuals = y - (2*x)
print("Levene’s test for Homoscedasticity:", stats.levene(x, residuals).pvalue)
'''
residuals).pvalue)
Levene’s test for Homoscedasticity: 1.3084338260012296e-07

'''




#test correlation----
#pearson --> yteste khatie correlation
'''

Correlaitonb test 
No differenc,e ok 


H0 : no relationship between two variable [correlaitoni vojod nadarad]
H1 : vojod nadarad



'''
r, p_value = stats.pearsonr(x, y)
print(f"Pearson correlation: {r}, p-value: {p_value}")

#Pearson correlation: 0.9654943669720487, p-value: 4.538186359602331e-59


if p_value <0.05:
    print('reject null hypothesis')
    print('rejct kon  no relationship between  ')
    print('there is relationship')
    print('there is correlation')
else:
    print('no correlation')



'''
reject null hypothesis
rejct kon  no relationship between  
there is relationship
there is correlation



x , y --> correlaiton vojod darad
'''

#r

# beyne +1 , -1 

#aslano abada manfi mosbatesh manie khasi nadaran

#harchi b gahdre motlaghe 1 --> +1 , -1 in correlaiton ghavi tare
#harchib 0 nazdik tr bashe badtare


#0.9654943669720487 ---> 1








import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#data = pd.DataFrame(b,columns=['feshar','dama','time','estehkam'])
data = pd.DataFrame(np.random.rand(100, 5), columns=[f'Var{i+1}' for i in range(5)])

# Compute Pearson correlation matrix
corr_matrix = data.corr(method='pearson')
# Print correlation matrix
print(corr_matrix)

'''
          Var1      Var2      Var3      Var4      Var5
Var1  1.000000 -0.186608  0.207927 -0.095359 -0.011769
Var2 -0.186608  1.000000  0.013542  0.137047 -0.091873
Var3  0.207927  0.013542  1.000000  0.006958  0.018743
Var4 -0.095359  0.137047  0.006958  1.000000 -0.067341
Var5 -0.011769 -0.091873  0.018743 -0.067341  1.000000

'''

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.colormaps()
plt.title("Pearson Correlation Heatmap")
plt.show()



#--pearson -> Linear y = x**2 --> corrrelation 
#y = 2*x  , 3*x x ,....

spearman_corr = data.corr(method='spearman')

plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Spearman Correlation Heatmap (Non-Linear)")
plt.show()






#----Pairwise Scatter Plots (Non-Linear Check)----
sns.pairplot(data)
plt.show()




#=========================================
'''    9 - Analaysis of Variance    '''
#=========================================
'''
Z test , T test --> vazne yek jame aro  estenbat


1 sample Z test , t Test
H0 : mean_vazn = 40  



moghayese konim dotaro

2 sample Z tst, t Test
H0 : mean_vazn_groupA = Mean_vazn_group_B



Agar bishtar az 2 ta goroh bodn chi?

3 ,4,... ta goroh bodn , aya vazne hameye iun s goroh barbare?

variance hashon ro baham moghayese konim 
Analysis of Varance --> ---ANOVA  one-way--

vazn , gahd , ....

ANOVA one-way

H0 Null hypothesis : mu1 = mu2 = mu3  
h1 alternative : mu1!=    mu2!=  mu3!=



F = Variance betweeen groups / Variance within group

30 nafar --> 



F kh bala bashe --> fasele ye beyne goroh ha ziade --> miangina barabar nist --> P_ value < 0.05
F kh kochik bashe --> hamposhani, goroh ha rohame miangina --> p > 0.05 --> fail to reject nul --> miangin ha barabr hast






farziat --->
1-tamame gorih ha bayad normal bashe --> shapiro(grouop1), hapiro ,,
2-hamgenie variance --> levene
3-esteghlale dade ha --> pearson begiri  [mohem nist]




'''

#-----One-Way ANOVA------
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data for 3 groups
np.random.seed(42)
group1 = np.random.normal(50, 10, 30) #vaznesho 50 
group2 = np.random.normal(55, 10, 30) #vazneshon 55
group3 = np.random.normal(60, 10, 30) #vazneshon 60


'''
Anova on-way
H0 Vazne har 3 goroh barbare mu1=mu2=mu3
H1 --> Mu!=mu2!=mu3

'''


df = pd.DataFrame({
    "value": np.concatenate([group1, group2, group3]),
    "group": ["G1"]*30 + ["G2"]*30 + ["G3"]*30
})

sns.boxplot(data=df, x="group", y="value")
plt.show()





import scipy.stats as stats


f_stat , p_value = stats.f_oneway(group1,group2,group3)

print(f"F-statistic: {f_stat:.3f}")
print(f"P-value: {p_value:.3f}")


'''
F-statistic: 12.210
P-value: 0.000

p<0.05 --> rejct Null hypothesis , hame barabaran -> 

hame barabar nistan

miangine vazni barabar nist



1---> ravseh conclusion --> miangine vaznie se gorohg barbar nist
2---> in se goroh motefavetan , amele (factor) vazn baese tafavvot in se goroh hast




ag ye drsad satisfy -> pishfarz
non-parametric anova one-way

stat, p = stats.kruskal(group1, group2, group3)
print(f"Kruskal-Wallis Test: p-value = {p:.3f}")


'''



#---> 1-way ? --> 1 -factor

#vazn , ghad , ...

'''
Giah darim roshd daran mikonan 

3 goroh giah darim 

ina one-way birim motegfavet

bekhatere koodeshon (organic, chemcial)
noe noor dehi (low, medium , high)


2 factor darim 


2-way ANOVA


'''


import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

import matplotlib.pyplot as plt

# Sample Data
np.random.seed(42)
df = pd.DataFrame({
    'Fertilizer': np.repeat(['Organic', 'Chemical'], 15),
    'Sunlight': np.tile(['Low', 'Medium', 'High'], 10),
    'Growth': np.random.normal(20, 5, 30) + 
              (np.repeat([2, 5], 15)) +  # Fertilizer effect
              (np.tile([1, 3, 6], 10))   # Sunlight effect
})


df.head()

'''
  Fertilizer Sunlight     Growth
0    Organic      Low  25.483571
1    Organic   Medium  24.308678
2    Organic     High  31.238443
3    Organic      Low  30.615149
4    Organic   Medium  23.829233

'''


#1-WAY --> ROSHDE ina barbaar hast ya na

#2-way --> factor 
from statsmodels.formula.api import ols
import statsmodels.api as sm
model = ols('Growth ~ C(Fertilizer) + C(Sunlight) + C(Fertilizer):C(Sunlight)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Show ANOVA Table
print(anova_table)


'''
                               sum_sq    df         F    PR(>F)
C(Fertilizer)                7.727385   1.0  0.453412  0.507152
C(Sunlight)                 70.483107   2.0  2.067833  0.148405
C(Fertilizer):C(Sunlight)   73.283022   2.0  2.149977  0.138390
Residual                   409.025866  24.0       NaN       NaN





factore fer(koood) ---> F variance beyne goro , --> P 0.50  -> 0.05 --> Bale reject nmitonm konm null
null > ---> miangine growth baraye 3 ta gorohe mokhatfe kood --> barabaran  mu1=mu2=...

Koood tasiri dar growth nadarad



Sunlight --> F bishtari --> 0.148405 > 0.05  --> 
ba shavahede amari k darim , nemitavanim farze motefavet nabodn ra rad koni ,motefavet nistan
sunlight motefavetbode, gwoth morefavet nbode

factore noor tasiri dar rosh ndrd


ekhtelafr msohahede shode beyne nemone ha , az anzare amari significant ( manadar)




C(Fertilizer):C(Sunlight) , joftesh baham taghir kone 0.138390>0.05 --> 

interaction kood va noordehi ham tasiri ndre



p<0.05 -->  tasir dre


'''




'''
Overview


Statistics --> study of data, we must analysis
 

1-Descriptive statistics (mean,median,mode,max,min,...)

2- inferential statistics (estenbat)

H0 --> Frze null zero  = = normal, no difference
H1 -->alternative

T,Z,F,...---> p
p<alpha(0.05) --> reject null hypothesis
p>alpha(0.05) -->fail to reject null hypothesis



Noramlity test 
visual (boxplot, histogram, Q-Q plot , KDE)
Shapiro-wilk ,, anderson-darling

H0 NULL HYPOTHESIS --> dATA IS NORMAL
p<alpha --> data is not normal





sample <----> Population

sample --> popualtion

1-sanple Z test 
1-sample T test(data<30 , unknwon )

H0 --> Mu = Specific = 27 ,...
p<alpha --> Mu !=27 (H1)


Comaprsion
sample1 <--->population1
sample2 --> population2

2-sample Z test
2-sample t test

H0 --> Mu1 = Mu2
P<alpha --> Mu1 != Mu2 (H1)



Levene 

H0 --> var1 = Var2
P < alpha --> var!=var2 (H1)

farze ztest , t test --> Normal, ...



Pearson (khati) 
H0 --> correlationi beyne do variable vojod nadarad

P < alpha --> correlatin vojod dahst
r --> shedat intensity ( --> +1 , -1 nazdik tar bod corraltion bsihtari darad)






age bishtar az 2 goroh khastim moghayese konim 
3 gorho




ANOVA 1-WAY

H0 null hypothesis --> mu1=mu2=mu3=...
F = variance between groups / variance withing group

F>... -->  p < alpha --> mu1!=mu2.... --> factore tasir gozar hast va baese tafavote amari shode





agar bishtar az 1 factor dashti, 2 ,3 factor 

ANOVA 2-WAY
H0 C1 --> mu1=mu2=mu3 -->C1
H0 C2 --> mu1=mu2=mu3 -->C2
H0 C1:C2 --> mu1=mu2=mu3 -->C1:C2

anova

C1 -----> p ---> p<alpha --> H0 reject --> tafavot --> factore C1 tasir gozar hast
C2 -----> p ---> p<alpha --> H0 reject --> tafavot --> factore C2 tasir gozar hast
C1:c2 -----> p ---> p<alpha --> H0 reject --> tafavot --> factore ointeraction c1 va C2 baham tasir gozar hast


'''







#=========================================
'''           10 - Regression          '''
#=========================================

'''

Pearson (Correlation)  beyne 2 ta variable kh balast , darim

age befahmim too anova yek factori tasir gozare 



Ma hala mikhaym rabete beyne onaro dar b airim




Growth = temperature_sunligght ????


gwoth = 4 * temperature_sunligght + 800


Gwoth pishbni koni

dama , estehkam


estehkam = 8.3434 * dama + 323


dama --> estehkam pishbini??




Regression ---> Machine learning (prediction) --> Deep learning


'''






