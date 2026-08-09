#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:20:13 2026

@author: apm


SKlearn_Conclusion

"""

#data ro ma import konim? -> Pandas

#------------Imports------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import train_test_split




#======================================
'''        Delivery  Dataset       '''
#======================================

#mitoni fght esme data ro bezni az on oon bala samte rast beri oonja 
df_delivery = pd.read_csv('delivery_time_dataset.csv')


#bejaye inke mahale run ro bbri jaei k data hast 

#biay asan begi harjaei k run shod mohem nsit, addrese kamel bedi ba kerneli run kone


#df_delivery = pd.read_csv('/Users/apm/desktop/AIEngineeringToturial/Quiz/quiz_data/delivery_time_dataset.csv')


#data cleaning ---> (1-cell empty, 2-type error,3-logical, 4-duplicated)
#chiori tashkhis dade beshe, chijori bahash rafatr beshe

#.info() -->    , dropna(inplace=True) , [column].dropna() .fillna() yek adad ,
#soton.mean(), median()  , fillna(method='ffill' ,'bfill')




#df_cleaned --> data

#--> numpy x, y


#Yek EDA --> Graph --> az GPT estefadd koni --> namahaye khobi az data

#--> train test split ---> x_train,x_test,y_train,y_test

#---> Pipeline misazi -> mdoel import, preprocessor 

#--> Gridsearch(pipeline, param_grids)

#gridsearch(pipe_line(model)) .fit(x_train,y_train)

#grid.best_score_  .best_params_

#best_model=grid.best_estimator_

#y_test_pred = best_model.predict(x_test)


#metrics.MAE(y_test,y_test_pred) ---> test score ro behet mide








#======================================
'''        Delivery  Taxi       '''
#======================================


df_taxi = pd.read_excel('/Users/apm/desktop/AIEngineeringToturial/Quiz/quiz_data/taxi_fare_dataset.xlsx')



#======================================
'''        Delivery  Energy       '''
#======================================

df_energy = pd.read_excel('/Users/apm/desktop/AIEngineeringToturial/Quiz/quiz_data/home_energy_consumption_dataset.xlsx')





#======================================
'''        Delivery  Material       '''
#======================================

df_material = pd.read_excel('/Users/apm/desktop/AIEngineeringToturial/Quiz/quiz_data/Material_Strength_Temperature.xlsx')



#======================================
#======================================
#======================================
#======================================
#======================================



'''

Python overview - Class (OOP)

Advanced function, OOP advanced , CLI , Bash

Git , telegram bot

Overview on Cli , python, 

- Numpy
- Matplotlib.pyplot  --> gpt , seaborn
- algebra , differential (Scipy,sympy)
- Pandas (data , data cleaning)
- Statistics (statistic test)  before AI 
- Into on ML concept  , regression
- Machine elarning (Sklearn) ,Models
- Gridsearch, crossvalidation, yperpamater , extractions,selection (pipeline)
- 3 example vaghei real ro dar Supervised classification, supervised regression, unsupervised tadris krdim


--> Azinja bebad --> Sklearn (traditional ML ) tamom shod --> ina barye yek darke concepte , zamani k dataye shoma kam hast 
--> data ziad beshe ---> Deep learning 

Sklearn -->

Agar khdoe code zanisho , ketabkhone ro --> 
1-GPT Tutorial (begid yekbar dg beheton tadris kone ) yek sakhtare derakht
(Pipeline , gridsearch ) --> hala 20 jalase advanced


2- Khode website sklearn hast --> kh kh jolo miofti 
roozi 2 ssaat bezari done done page haro bekhoni, source code  (github) felan model 

class DecisionTreeRegressor() 


Model ha beshi (barat model ha kh mohem tare (theory , riaziat))-->
1- Youtube videos specific

2- Introduction to Machine Learning with Python 
Oreilley 
Andreas C. Müller & Sarah Guido





-----Baraye taghviat ------------
https://scikit-learn.org/stable/api/sklearn.datasets.html

from sklearn.datasets import load_diabetes

nesbat b tadrisi (example)

hal kardan --> gpt enhance --> chia kame chia ziade
chi behesh ezafe kon

4,5 bar anjam bedi ---> sklearn engineer













'''



















