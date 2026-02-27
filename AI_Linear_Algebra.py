"""
Created on Fri Feb 27 07:52:53 2026

@author: Ali Pilehvar Meibody



in jalase --> riaziate ziad dare
vali negarani nadare
gharar nist kolesho emrooz ya in hafte motvaje beshim
yek darsname ee hast k kam kam bayad yad begirim
ta jalase e ke varede algoritheme hooshe masnooe mishim
machine learning



---------Linear Algebra-----------------
Jabre khati

Machine learning [algorithem] aksareshon vabastan b hamin ghavanine
dakhele jabre khati 

Jabre khati --> yek space , vector + matrices vojod dare

"""

'''
quantity (adad) --> rocket ba sorate 700 Km/h harekat mikone
magnitude ---> 700 na jahat dare na hichi /direction 

700 Km/h dare mire masalan b samte bala + --> +700KM/h (magnitude + direction)
bordar Vector ---> az chnata scaler 

rocket soratsh [0 +700]  , [+700 0] dota rocket sorata barabare
vali yeki roo b balast yeki roo b paeen
vector ---> Bordar 

Vector ha chan bodian
1 D --> [adad]
2 D --> [adad , adad]
3 D --> [adad , adad , adad]
**frgh dare ba dimension numpy --> radif-->jadval --> chnata jadval XXXXXX

Machine learning --> yek vide darid

vide = [10.5 , 5.2 , 3.25 ,7]
video 10.5 minutes , only 5.2% viewere
3.25 darsad like , 7 IMDB score



#----> BORDAR fght

Y
/\
|        (x=5,y=5)
|       /\
|      /
|     /
|    /
|  []
|  (x=3,y=3)
|  
|------------------>X





Y
/\
|        
|       
|      
|     
|    
|  []
| / (x=3,y=4)
|/  
|------------------>X

a =[3,4]



'''

#1 D v = [3]
#2 D v = [3  , 4]
#3D v = [1,2,3]

#------2D Vectors
#------> har vector 2D yek noghte hast dar fazaye 2D (x,y) bordar behesh vasl shodde
#az mabda (0,0)
import numpy as np
u = np.array([2,5]) #yek noghte dar fazaye 2 Bodi
v = np.array([3,1])

#----3D Vector
'''
Y
/\
|        
|       
|      
|     
|    
|  []
| / (x=3,y=4,z=3)
|/  
|------------------>X
\
 \
  \
   \
    \
     \
      \
      \/ Z




'''

z = np.array([3,4,3])


'''
Norm
the norm of vector (u) noted ||u|| is measure of length(magnitude) of u
ma chand no length darim --> 
we have a lot of norm but most common is Euclidian Norm
vector =[scaler, scaler scaler]

scaler be tavane 2 done done bebari + ham koni 
--> radicalo begiri mishe norme oon

|| u || = radical [ zigma ui**2]



'''
import numpy as np
v = np.array([3,4])

#noghte dar 3,4 --> bordar ham hesab mishe ag mabda az 0,0
#3**2 = 9  | 4**2 = 16 --> 25 radical 25 -->5
#norm ya length ya andaze ya magnitude in bordar --> 5
print(type(v)) #<class 'numpy.ndarray'>

#linealg --> linear algebra
norm_v = np.linalg.norm(v)

print('||V|| = ', norm_v)
#||V|| =  5.0

#---YEJOR DG
#1
from numpy import linalg
norm_v = linalg.norm(v)

#2
from numpy.linalg import norm
norm_v = norm(v)

#3
import numpy as np

norm_v = np.linalg.norm(v)


import numpy as np
import math

def pm_norm(vector):
    #check mikone numpy
    #chan bodie 
    print(vector.size)
    print(vector.shape)
    
    n_size = vector.size
    
    scaler_squared = []
    for i in range(0,n_size):
        
        scaler_squared.append((vector[i])**2)
        
    #zigma [scaler**2]
    scaler_zigma=sum(scaler_squared)
    
    vector_norm = math.sqrt(scaler_zigma)
    
    return vector_norm

#tabe ee k dar numpy --> dar linalg 
#be name norm
        
v= np.array([3,4])
pm_norm(v) #Out[9]: 5.0
np.linalg.norm(v) #Out[10]: 5.0
    
    

v= np.array([10,20])
np.linalg.norm(v) #Out[11]: 22.360679774997898
pm_norm(v) #Out[12]: 22.360679774997898

#---------Vector Operations --------
#1----Addition
#vector same size dashte bashe mitoni add koni dotaro
'''
[2 5]
[3 1]
-------
[5 6]
element-wise


vector addition is commutative --> u + v = v + u
vector addition is associative --> u + (v+w) = (u+v) +w


fahme ina -->niaz b shekle 3d dare va fazaye grpahically




Y
/\
|        
|       
|      
|     
|    
|  []          []
| / (x=3,y=4)  (x=8 , y=4)
|/      
|------------------>X

Y
/\
|        
|       
|            /\
|            |
|           |
|  []       |       
| /        |4
|/      --->3    
|------------------>X




vector1 --> 3 ta dar x , 4 ta dar y
vector 2 --> 8 ta dar x , 4 ta dar y


| 8 ta
--------> 11 ta dar rastaye x

'''
v1 = np.array([3,4])
v2 = np.array([8,4])
v_sum = v1 + v2

print('v1 + v2 =',v_sum)
#v1 + v2 = [11  8]



#b.scaler myltiplication
#------Multiplication by scaler
v = np.array([1,2])

#scaler age multiplication(zarb) -->scaled mikone

v_scaled = 3 * v

#3 * 1   | 3 * 2 
print('3 * v =' , v_scaled)
#3 * v = [3 6]


#bordare zarb koni ch x ch y --> scale 
#bozorg namae ya kochik namaee
#x1 x2 x3 x4 


#3.dot product
'''
add ,scaler multiplciation --> output --> Vector
dot prorudtc --> scaler 
zarbe dakheli , 

u.v 

2 ta vector
u.v = ||u||  x ||v|| x cos(theta)
dota bordar yek zavie ee beyneshoone

dot product is commmutative u.v = v.u 
not associative nist --> (u.v).w = u.(v.w)



'''

import numpy as np
u = np.array([2,5]) 
v = np.array([3,1])

np.dot(u,v) #11


#------
def pm_norm(vector):
    #check mikone numpy
    #chan bodie 
    print(vector.size)
    print(vector.shape)
    
    n_size = vector.size
    
    scaler_squared = []
    for i in range(0,n_size):
        
        scaler_squared.append((vector[i])**2)
        
    #zigma [scaler**2]
    scaler_zigma=sum(scaler_squared)
    
    vector_norm = math.sqrt(scaler_zigma)
    
    return vector_norm


def pm_dot(u,v,theta_u_v=0):
    #check
    u_norm= pm_norm(u)
    v_norm= pm_norm(v)
    #tabe dg benevisim k zavieye beyne u and v ro hesab kone
    dot = u_norm * v_norm * math.cos(theta_u_v)
    return dot
    
    

#-----Matrices --> ماتریکس
#khode bordar --> dg mishe agah --> numpy array 2D

#numpy array 0D --> Scaler
#numpy array 1D --> Vector [s] [s s ] [s s s] [s s s s]
#Numpy array 2D --> Matrix [ [radif1] , [radif2]]

'''
    | 3   4 |
A = |       |
    |5    1 |


'''

import numpy as np

a = np.array([ [3,4] , [5,1]  ])
print('Matrix A : ' , a)
'''
Matrix A   [[3 4]
            [5 1]]


moshakahseye matrix , andazash
(row x columns)

matriix 2 x 2
matrix 
'''
a.shape #Out[19]: (2, 2)
a.size #Out[20]: 4  shape dakheli (2,2) --> 2 * 2 = 4

#radif
a[0] #Out[21]: array([3, 4])

#soton
a[:,0] #Out[22]: array([3, 5])

#element
a[0,1] #Out[23]: 4

#jolosh adad -->taghir

#numpy dars dade shode
#va baham hamposhani dare

#oidentity matrix
np.eye(3)
'''
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

'''




#zero matrix
np.zeros((2,3))
'''
array([[0., 0., 0.],
       [0., 0., 0.]])

'''


np.diag([4,5,6])
'''
array([[4, 0, 0],
       [0, 5, 0],
       [0, 0, 6]])

'''


np.diag([3,4,5],k=1)
'''
array([[0, 3, 0, 0],
       [0, 0, 4, 0],
       [0, 0, 0, 5],
       [0, 0, 0, 0]])

'''


#----MATRIX OPERATIONS-------
#a . adding matrices
#bayad hatman ham andaze bashan
#element-wise add mikonim
'''

a --> (3,5) ---->  (4,6)








    3    4
a  = 5   6


    1    2
b  = 3   4

     1+3    4+2
a+b = 3+5   4+6

     4    6
a+b = 8   10
'''

a= np.array([[3,4],[5,6]])
b= np.array([[1,2],[3,4]])
print('a+b = ', a+b)
'''
a+b =  [[ 4  6]
        [ 8 10]]



commutative hast --> A + B = B +A
sassociative --> A + (B+ C) = (A+B) + C


'''


#b SCALER multiplication
#scaler * matrix

'''
    3    4
a  = 5   6



3 * a = 
element wwide



'''
a= np.array([[3,4],[5,6]])

print(3*a)
'''
[[ 9 12]
 [15 18]]

'''



#element-wise multiplication
a= np.array([[3,4],[5,6]])
b= np.array([[1,2],[3,4]])

print(a*b)

'''
    3    4
a  = 5   6


    1    2
b  = 3   4

      3*1   4*2
a**b = 3*5   6*4
'''

'''
[[ 3  8]
 [15 24]]
'''


#----Matrix multiplication(mohem tarin ghesmate linear algebra)

#matrix a --> (m*n)    b-->(k*z)
#fght dar yek soorat mitonid matrix multiplication anjam bedid
#n = k bashe
#tedade sotone matrix Aval == tedade radife matrixe dovom


'''
(2,2)  (2,3)

    1   2
a = 3   4

   1  2  3
b = 4  5  6


az avalie radifesho varmidare
dar soton dovomi zar mikon

avalish --> [1 2]  [1 4] --> [1*1 + 4*2]

       1*1 +2*4       1*2+2*5   1*3+2*6
a @ b = 3*1 +4*4       3*2+4*5    3*3+4*6


       9      12   15
a @ b =19     26   33

'''

a = np.array([[1,2],[3,4]])
a.shape #Out[31]: (2, 2)

b= np.array([[1,2,3] ,[4,5,6]])
b.shape #Out[32]: (2, 3)


#tedad sotone a ba tedade radif b barabare
#mishe anjam dad -->errror mide
c = a.dot(b)
print(c)
'''
[[ 9 12 15]
 [19 26 33]]

'''

#zarbe dakheli
#2 ta vector dot migirm --> ||v|| x ||u|| x cos (theta) -->scaler

#zarbe kahreji
#2 ta matrix dot migritim --> radife avali * sotone dovomi element wise mishe

c = a@b
print(c)
'''
array([[ 9, 12, 15],
       [19, 26, 33]])
'''
b@a#error
b.shape #Out[38]: (2, 3)
a.shape #Out[39]: (2, 2)
#3 /= 2




d = a *b
print(d) #hameye a ba b shape yeksan b ashe


'''
Commutative nist --> a * b =/ b * a

associative --> q (r*s) = (q*r)*s

distributive --> (q+r)s = q*s + r * s
'''


#matrix -->
#matrix transpose
#a t

a = np.array([[1,2],[3,4]])
print(a)
'''
[[1 2]
 [3 4]]

'''

a.T

'''
array([[1, 3],
       [2, 4]])

'''


#determoinant

M = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9] 
    ])

'''
M1,1 --> 1*5 - 2*4
M2,2 --->1*9 - 3*7
M3.3. -->5*9 - 8*8
Det(M) = M1,1 + M2.2 + M3.3


'''
np.linalg.det(M)
#Out[44]: -9.51619735392994e-16



'''
matrix dari --> equation system
mige ke matrix -> invertible , system unique solution

determinant = 0 --> matrix is singular (not invertible nis)

'''

a = np.array([[1,2],[3,4]])
print(a)
'''
[[1 2]
 [3 4]]

'''


#transpose
a.T
'''
array([[1, 3],
       [2, 4]])

(q + r)* T = qT + rT
(Q.R)T = rT . qT


'''

#inverse----
#A -1
np.linalg.inv(a)
'''
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

m.m-1 = m-1.m = I (identity matrix)

(landa * M)-1 = 1/landa *  M-1


'''

#checkkoni k in aya inv hamon has

#A @ A -1 = Identity (eye)

b = a @ np.linalg.inv(a)
print(b)
'''
[[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]

'''

np.eye(2)
'''
array([[1., 0.],
       [0., 1.]])
'''


#matrix --> orthogonal matriox
#H -1  = H T

#https://github.com/ageron/handson-ml2/blob/master/math_linear_algebra.ipynb
#--------------------------------

#Numerical calculation







