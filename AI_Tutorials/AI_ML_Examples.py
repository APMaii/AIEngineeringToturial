#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD

Created on Fri Jul 24 11:06:48 2026

@author: Ali Pilehvar Meibody



1- Supervised Regression 

2- Supervised Classification

3- Unsupervised clustering










-------Review--------------
Ai --> 70-80% Machine learning 

Tamame masaele jahan ro be vorodi - khoorji (input-output) tabdil konim

donbale rahi hastim k vorodi ra b khoroji mortabet konim



agar data baaraye ma kamel vojod dahste bashe

agar data y esh malom bod dahstimesh 
1- Supervsied --> regression (y continious ) , classification (gosaste)
2-Unsupervised --->  dimentional reduction (visualization, preprocess before model)
ya baraye clustering

3- Deep learning --> supervised , unsupeevised


agar data vojod ndre az ghabl , va incrementally miad 
4- Reinforcemnet learning (RL)




3 ravesh (strategy baraye training vojod darad)




1- Basic --> 
import data , clean, train_test_split , model (from skle) , 
model.fit(x_train,y_train) , predict --> test_score, train_score

test_score khob bod awli
ag bad bood -> train score

train score kh paeine -> asan model yad ngrfte --> underfitting (complex tar koni)

train score kh kh bala --> model hata khata ham , generlaization-> overfitting (simple tar koni)



2 - GridsearchCV  (ghole marhale 2 )--> complex , simple , hyperparamter
import data, clean , [train test nadari] ,model , 
GridsearchCV (model, hyperparametr_range, cv = 5 )
gridssearch.fit(all data , x, y )

behtrin hyperparamtee, bhtrin model , .....




3- Pipeline --> 
data, clean, train test , model , preprocesor
kolesho bzar toye pipeline ,

gridsearchXCV(pipeline, hyperparmater range(hyperpamrter model, preprocess))

fit(x_train,y_train)

gridsearch.best_estimator_ .predict(x_test)

megtruics ---> test score 


ham tamame preprocessor hameye chizha dar yek pipeline bashe
train validation test 

train validation --> behtrin hypeparmateer peyda mikonim
ba teest khali --> test score bedast mairim




"""



#==========================================
#==========================================
#==========================================
'''  Supervised Regression Example  '''
#==========================================
#==========================================
#==========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing


housing = fetch_california_housing(as_frame=True)


df = housing.frame.copy()



print(type(df))

#<class 'pandas.core.frame.DataFrame'>

print(housing.feature_names)
'''
['MedInc', 
 'HouseAge',
 'AveRooms', 
 'AveBedrms',
 'Population', 
 'AveOccup',
 'Latitude', 
 'Longitude']

'''

print(housing.target_names)

#['MedHouseVal']


print(housing.DESCR[:1000])

'''

California Housing dataset
--------------------------

**Data Set Characteristics:**

:Number of Instances: 20640

:Number of Attributes: 8 numeric, predictive attributes and the target

:Attribute Information:
    - MedInc        median income in block group
    - HouseAge      median house age in block group
    - AveRooms      average number of rooms per household
    - AveBedrms     average number of bedrooms per household
    - Population    block group population
    - AveOccup      average number of household members
    - Latitude      block group latitude
    - Longitude     block group longitude

:Missing Attribute Values: None

This dataset was obtained from the StatLib repository.
https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

The target variable is the median house value for California districts,
expressed in hundreds of thousands of dollars ($100,000).

This dataset was derived from the 1990 U.S. census, using one row per ce
'''


# x , y --> supervised learning

# y --> gheymate khone hast --> continious --> peyvaste --> supervised regression

#mikhahim ba x ha [avbedrom, housage ,...]
#gheyajte khone ro pishbini konim --> entehaye kair (goal , hadafemon)


#------------------------------
#---------Clean----------------

df.head()

'''
   MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
0  8.3252      41.0  6.984127  ...     37.88    -122.23        4.526
1  8.3014      21.0  6.238137  ...     37.86    -122.22        3.585
2  7.2574      52.0  8.288136  ...     37.85    -122.24        3.521
3  5.6431      52.0  5.817352  ...     37.85    -122.25        3.413
4  3.8462      52.0  6.281853  ...     37.85    -122.25        3.422

[5 rows x 9 columns]

'''


df.isnull().sum()

'''
MedInc         0
HouseAge       0
AveRooms       0
AveBedrms      0
Population     0
AveOccup       0
Latitude       0
Longitude      0
MedHouseVal    0
dtype: int64

'''


df.duplicated().sum() #0

#1- Empty cell (dropna, fillna())
#2- rtype --> .as_type()
#3- logical erro
#4-duplicated


#------------------------------
#-----------EDA------------


df.hist(figsize=(14,10),bins=30)
plt.show()



df.plot(kind='box',subplots=True,layout=(3,3),figsize=(15,10),sharex=False,sharey=False)
plt.show()

#df = df[df['MedHouseVal']<4.5]


#asan x ha chghd ba y correlation dare
#pearson correlation


#numeric boodan

correlation_matrix = df.corr(numeric_only=True)


fig, ax = plt.subplots(figsize=(10,8))

image = ax.imshow(correlation_matrix)

ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))


ax.set_yticklabels(correlation_matrix.columns,rotation=90)

fig.colorbar(image)

ax.set_title('Correlation amtrix')

plt.tight_layout()
plt.show()


#-------

plt.scatter(df['MedInc'],df['MedHouseVal'],alpha=0.25)

plt.xlabel('median income')
plt.ylabel('median house value')

plt.title('median income vs median house value')

plt.show()



plt.scatter(df['HouseAge'],df['MedHouseVal'],alpha=0.25)

plt.xlabel('median age of house')
plt.ylabel('median house value')

plt.title('median age of house vs median house value')

plt.show()




#------------------------------
#-----------Pipeline------------
#import data --> sklearn.datasetsz3
#EDA
# clean data 

#x , y 
x = df.drop(columns='MedHouseVal')  #Inplace = False
y = df['MedHouseVal']

print(x.shape) #(20640, 8)
print(y.shape) #(20640,)



#train test split

from sklearn.model_selection import train_test_split


x_train, x_test , y_train , y_test = train_test_split(x,y ,test_size=0.20, shuffle=True, random_state=42)


print('training samples : ',x_train.shape[0])

print('test samples : ',x_test.shape[0])

'''
training samples :  16512
test samples :  4128

'''

#----Pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#model haye dg --> 4,5 model mohem , SVR , Linear (sgd ) , random forest, decision tree, 
from sklearn.linear_model import Ridge

scaler=StandardScaler()

model = Ridge()

ridge_pipeline = Pipeline([
    
    ('scaler',scaler),
    ('model',model)])




#gridsearchCV --> parametr grid 

#task -> har mdoel yekseri hyperparametr dare k moheme

#entehaye in jalase , yek file mizaram tozihe mohmtrin hyperparametr

# GPT , CLaude --> kole pipeline , --> paraM_grdi besaz 
#baste b config system 


ridge_param_grid = {
    #'scaler' : [None,StandardScaler() , MinMaxScaler() ,...,PCA]
    #'scaler__n_components': [2,3,4,5,5,]
    'model__alpha' :[0.001,0.01,0.1,1,10,100]
    
    }



#ai ? --> ai midone ch hyperparametr mohem hastan 10 ta 4 ta , 
# range hashon , alpha 10 b tavani , 1 , 2, 3
# raNge --> cover koni 


from sklearn.model_selection import GridSearchCV



grid = GridSearchCV(
    estimator =ridge_pipeline,
    param_grid = ridge_param_grid,
    scoring= 'neg_mean_absolute_percentage_error',
    cv = 5 ,
    n_jobs=-1)

#movazi parallel


grid.fit(x_train,y_train)

#x_train, y_train -->> train , vaklidation --> behtrin hyopeparamter


grid.best_score_ #-0.3151441974454266


grid.best_params_ #{'model__alpha': 100}






#---hala bayad rooye test ham anjam bdid

best_model  = grid.best_estimator_

y_pred = best_model.predict(x_test)



from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error


mae = mean_absolute_error(y_test,y_pred)

mape = mean_absolute_percentage_error(y_test,y_pred)


print(mae) #0.5330142193095552 --> +- 0.53 
print(mape) #0.31900996753924055




#-------
plt.figure(figsize=(8,6))

plt.scatter(y_test,y_pred , alpha=0.35)

plt.show()










plt.figure(figsize=(8,6))

plt.scatter(y_test,y_pred , alpha=0.35)

minimum_value = min(y_test.min(), y_pred.min())
maximum_value = max(y_test.max(), y_pred.max())

plt.plot(
    [minimum_value, maximum_value],
    [minimum_value, maximum_value],
    linestyle="--"
)

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted House Values")

plt.show()





#evliuate ->chan darsad accuracy
#use --> estefade konid


#best_model --> zakhirash koni ,....

#website , jaee --> deploy

#vorodi -> pishbini

#frontend , frontend , dataharo yeki vared

#frontend --> backend --> best_mdoel.rpedict(x) -->y

#Khoroji friontend namayesh mdie 













#------modelamo avaz mikonm

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#model haye dg --> 4,5 model mohem , SVR , Linear (sgd ) , random forest, decision tree, 
from sklearn.svm import SVR


scaler=StandardScaler()

model = SVR()

svr_pipeline = Pipeline([
    
    ('scaler',scaler),
    ('model',model)])




#gridsearchCV --> parametr grid 

#task -> har mdoel yekseri hyperparametr dare k moheme

#entehaye in jalase , yek file mizaram tozihe mohmtrin hyperparametr

# GPT , CLaude --> kole pipeline , --> paraM_grdi besaz 
#baste b config system 


svr_param_grid = {
    #'scaler' : [None,StandardScaler() , MinMaxScaler() ,...,PCA]
    #'scaler__n_components': [2,3,4,5,5,]
    'model__kernel' :['linear','poly','rbf'],
    'model__C':[0.001,0.01,0.1,1]
    
    }



#ai ? --> ai midone ch hyperparametr mohem hastan 10 ta 4 ta , 
# range hashon , alpha 10 b tavani , 1 , 2, 3
# raNge --> cover koni 


from sklearn.model_selection import GridSearchCV



grid = GridSearchCV(
    estimator =svr_pipeline,
    param_grid = svr_param_grid,
    scoring= 'neg_mean_absolute_percentage_error',
    cv = 5 ,
    n_jobs=10)

#movazi parallel


grid.fit(x_train,y_train)

#x_train, y_train -->> train , vaklidation --> behtrin hyopeparamter


grid.best_score_ #-0.3151441974454266


grid.best_params_ #{'model__alpha': 100}


#scorer dakheli , test besanjid --> nadidi


#----------


#==========================================
#==========================================
#==========================================
'''  Supervised Classification Example  '''
#==========================================
#==========================================
#==========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer(as_frame=True)


df = cancer.frame.copy()



df.shape #(569, 31)  31 soton

cancer.feature_names
'''
array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'], dtype='<U23')

'''

cancer.target_names
'''
Out[53]: array(['malignant', 'benign'], dtype='<U9')

malignant --> bad khim --> 1
benign --> khosh khim --> 0 



'''


df.head()

'''
   mean radius  mean texture  ...  worst fractal dimension  target
0        17.99         10.38  ...                  0.11890       0
1        20.57         17.77  ...                  0.08902       0
2        19.69         21.25  ...                  0.08758       0
3        11.42         20.38  ...                  0.17300       0
4        20.29         14.34  ...                  0.07678       0

[5 rows x 31 columns]

'''



df['target'].value_counts()

'''
target
1    357 --> badkhim
0    212 ---> khosh khim
Name: count, dtype: int64

'''


#azz x ha histohgram -> distribution , soton ha 

#rasm haro anjam bdid , correlation,
#radius , hast yua nis

#colour



#PCA 31 soton--> 2 soton

df.columns

'''
Index(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension',
       'target'],
      dtype='object')

'''
x = df.drop(columns='target')

y = df['target']


x.shape #(569, 30)
y.shape #(569,)

plt.hist(y,bins=30)
plt.show()


#------Pipeline-----------
from sklearn.model_selection import train_test_split

x_train,x_test , y_train, y_test = train_test_split(x,y,test_size=0.2 , shuffle=True,random_state=42)

#50 ta badkhm --> train etst , cv --> stratify=y  doros taghsim 

 


from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression #modele clasification
#from sklearn.svm import SVC

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

model = LogisticRegression(max_iter=5000,random_state=42)

#SGD , logisticregression, Randomforest

classification_pipeline = Pipeline([
    ('scaler',scaler),
    ('model',model)])

#-----parametr grids

cl_param_grid = {
    'model__C':[0.001,0.01,0.1,1,10,100],
    'model__penalty':['l1','l2']}




from sklearn.model_selection import GridSearchCV


grid = GridSearchCV(
    estimator = classification_pipeline,
    param_grid = cl_param_grid,
    cv = 5 , 
    scoring = 'accuracy') #inja mae , mape , .. faslee red - 




grid.fit(x_train,y_train)


#train validation test 
grid.best_score_ # 0.9758241758241759

grid.best_params_ #{'model__C': 1, 'model__penalty': 'l2'}








best_model = grid.best_estimator_

y_pred = best_model.predict(x_test)


from sklearn.metrics import accuracy_score


accuracy_shoma = accuracy_score(y_test , y_pred)


print('test accuracy : ',accuracy_shoma)

#test accuracy :  0.9736842105263158


from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test , y_pred)

print(conf_mat)


'''
[[41  2]
 [ 1 70]]

'''



'''

140 bimar --> test  pishbini 


97 darsad --> 135 doros zadim 5 taro ghalat

accuracy kafie kh kh jaha migan kefayat mikone


5 tae k ghalat pishbini krdim vaziat chi bode



yeksan nistan yek khata dar nazar 


eshtebahe inke shoam yeki khosh khim bod e, badkhim --> stress, hazineye bishtari bayad bede  FP

eshtebahe 0--> bad khime , pishbini khosh khim --> rsike marg taraf hast FN


200 --> 20 ta ghalayt pishbini kardde

180 / 200 --> 90% accuracy awli 


10% -> khat abhm 









Matrix Confusion 
                       pishbini khosh khim      pishbini badkhim
vaghean khosh khim         TN                     FP
vghean bad khim             FN                    TP


Positive --> badkhim


accuracy = TN + TP  / all (TN + TP + FP+ FN )


Precision --> az miane tyamamew nemone haye k badkhim elam shode, chan darsad badkhim bodan

precision = TP / TP + FP


RECALL --> az miane tamame nemone hayi k badkhim vaghean bdoan , chan darsad doros pishbini

recall = TP / TP + FN


F1 = 2 * prrecision x recall / precision + recall



'''



from sklearn.metrics import confusion_matrix

conf_mat = confusion_matrix(y_test,y_pred)

print(conf_mat)


'''

pishbini    khosh khim    badkhim
khosh khim  [[41           2]
badkhim     [ 1           70]]




'''
from sklearn.metrics import accuracy_score


accuracy = accuracy_score(y_test,y_pred)
print(accuracy) #0.9736842105263158

print((70+41) / (70+41+1+2)) #0.9736842105263158


#Metrics


print(type(x_test))

x_test.columns

plt.scatter(x_test['mean radius'],x_test['mean texture'],c=y_test)
plt.show()

plt.scatter(x_test['mean radius'],x_test['mean texture'],c=y_pred)
plt.show()



plt.scatter(y_test,y_pred)
plt.show()





#==========================================
#==========================================
#==========================================
'''  Unsupervised Example  '''
#==========================================
#==========================================
#==========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine


wine = load_wine(as_frame=True)


df = wine.frame.copy()


wine.feature_names

'''
['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']

'''

df.shape #(178, 14)

#az 178 ta 13 ta bema feature moshakahste 






#nadarid  XXXXXXXXXXXX
wine.target_names
'''
Out[87]: array(['class_0', 'class_1', 'class_2'], dtype='<U7')

'''


#data ro amadd konid




df.hist(figsize=(14,10),bins=20)
plt.show()


#corrrelation --> target



x = df.drop(columns='target')

y_real = df['target']



#kmeans --> clustering mikrd 

#kmean(k=chan khoshe taghsim)

from sklearn.cluster import KMeans
#elbow

k_values= range(1,11)

inertia_values=[]

for k in k_values :
    
    model = KMeans(n_clusters = k ,random_state=42,n_init=20)
    
    elbow_Pipeline = Pipeline([
        ('scaler',StandardScaler()),
        ('kmeans',model)])
    
    elbow_Pipeline.fit(x)
    
    inertia = (elbow_Pipeline.named_steps['kmeans'].inertia_)
    
    inertia_values.append(inertia)



#11 ta kmeans roye kole data 

plt.figure(figsize=(8,6))

plt.plot(list(k_values),inertia_values,marker='o')

plt.xlabel('number of cluster(k)')

plt.ylabel('inertia')

plt.title('elbow methoid')

plt.show()


best_k = 3



#-----------------------------
final_clustering = Pipeline(
    [('scaler',StandardScaler()),
     ('kmeans',KMeans(
         n_clusters=best_k,
         random_state=42,
         n_init=20))])




cluster_labels = final_clustering.fit_predict(x)



#label zad --> kmeans 3 ghesmat

plt.hist(cluster_labels,bins=30)
plt.show()




clustered_df = x.copy()

clustered_df['cluster']=cluster_labels
clustered_df['real_class']=y_real.values



clustered_df.head()

'''
   alcohol  malic_acid   ash  ...  proline  cluster  real_class
0    14.23        1.71  2.43  ...   1065.0        2           0
1    13.20        1.78  2.14  ...   1050.0        2           0
2    13.16        2.36  2.67  ...   1185.0        2           0
3    14.37        1.95  2.50  ...   1480.0        2           0
4    13.24        2.59  2.87  ...    735.0        2           0

[5 rows x 15 columns]

'''

x.columns

#alcohol

#malic_acid


plt.scatter(clustered_df['alcohol'],clustered_df['malic_acid'],c=clustered_df['cluster'])
plt.xlabel('alcohols')
plt.ylabel('malic acis')
plt.show()



#internal scoring


from sklearn.metrics import silhouette_score

score = silhouette_score(x,cluster_labels)

print(score) #0.1942818409408564


#from sklearn.metrics import calinski_herabsz_score

#from sklearn.metrics import davies_bouldin_score


#gerd boane khsohe , fasele , 



#external scoring

#khodet dasti az beyne dataha 20 taro label, tedadi k mishe
#va bbini k azin 20 ta chghdresh doros bode

#from skelarn.metrics import accuracy_score

#fuynction(label_zadi_dasti , cluster_tavastote_model)


#semi supervised --> supervsieed , unsupervised






#supervised regression -> 1 modele estefade --> reportesho .py
#superiesd clasification --> 1 modele estefade --> reproetesho
# unsupervies ->kmeans --> aggloremative_clustering 


#dataset --> sklearn --> dataset --> bairim bala estefade konid 




