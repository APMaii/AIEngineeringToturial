"""
Created on Fri Feb 27 09:20:24 2026

@author: Ali Pilehvar Meibody



Numerical calculation
Mohasebate Adadi

"""

#==============================
''' Differential Calculus'''
#==============================
'''
calculus --> study continious change
function --> change study

f(x)



f(x)= x**2
y = x**2


     y
    /\
|   |    \
\   |   /
 \  |  /
  \ | /
   \|/
    -
----0---------->X


raftare yek chizie , yek system , harchizi dar jahano
model koni ba yek tabe

x----> [function] ---> y

fucntion --> Curve ---> 

adad bezari -->javabe tBe ro mibini

moshtagh chie??
moshtagh --> yek noghte ee dari toye tabe
mikhay shibe oon noghte ro bedat biar


differential --> derivative---> Slope (shibe) oon Point noghtas


slope ya - yb / xa - x b  = Delta Y / Delta x

noghteye a va b bayad kheyli kheylli bechasbn b noghte ee k ma
moshtagh mikhahm begirim

ya --> f(xa)


slope = f(xa)-f(xb) / xa-xb



Moshtaghe dar noghete x 

Lim f(xa) - f(xb) / xa - xb 
xb --> xa


f(xa)`   -->moshtaghe xa
az a --> ta yek noghte b 
yek khat rasm mikonim
shibe oon khat mishe moshtaghe ma 
dar ch soorati --> b bechasbe b a
x b --> xa
xb - xa =~ 0


moshtagh dar yek noghte ro begirim
moshtagh dar yek noghte --> shib dar oon noghte

f(xa)` -->moshtaghe tabeye f dar nohgteye a
dar asl ma bayadyek xb peyda konim
yek khat vasl koni b xa --> xb
oon khat dar soorati daghighan shibe noghteye a hast k
b kh kh kh nazdib b a bashad

f(xa)` = Lim f(xa)-f(xb) / xa-xb 
         xa-->xb

e = xa - xb


f(xa)` = Lim f(xa+e) - f(xa) / e
         e--->0

f(xa)` = Lim f(xa+h) - f(xa) / e
         h--->0





#------LIM--------
lim(c)  = c
lim [f(x)+- g(x)] = Lim(fx) +- Lim(gx)
lim [f(x)x g(x)] = Lim(fx) +x Lim(gx)






moshtagh --> alamat darim
f` = df/dx = d/dx f = Df = y`

f` --> lagrange notation
df/dx --> leibniz noation
y.   --> newtonian notation
Df --> euler notation

moshtaghh




darim rooye noghte b noghte harf miznim



     y
    /\
|   |    \
\   |   /
 \  |  /
  \ | /
   \|/
    -
----0---------->X



f(x)=x**2


f(2)` = lim (f(2)-f(b)) /2-b = 2

f(4)`
f(8)`



bazi tabe ha --> mirtoni yek moadele jadid bezari jolosh
bgi agha in maodele hamoon f` eshe
dg done odne noght eb noghte hesab nashe





     y
    /\
    |    
    |   
    |-----------------y=4
    |  
    | 
    |
----0---------->X

f`(2)=0
f`(4)=0
f`(har adadi)=0


differentiation Rules

f(x) =c                 f'(x)=0
f(x)=g(x) + h(x)        f'(x) = g'(x) + h'(x)
f(x)=g(x)h(x)           f'(x)=g(x)h'(x) + h(x)g'(x)
f(x)=g(x)/h(x)          f'(x) = g'(x)h(x) - g(x)h'(x)/h**2(x)
f(x)=x**r               f'(x)=r*x**(r-1)
f(x)=ln(x)              f'(x)=1/x
f(x)=sin(x)             f'(x)=cos(x)
f(x)=cos(x)             f'(x)=-sin(x)
f(x)=tan(x)             f'(x)=1/cos(x)**2
f(x)=g(h(x))            f'(x)=g'(h(x))h'(x)


x**2 ---> 2*x* (2-1) --> 2*x
x**8 --> 8x**7



y = x**2 + 4*x + 3   -->curve noghte b noghte beri moshtagh hesab

y = f(x)  + g(x) + h(x)


y` = f(x)`  + g(x)` + h(x)`

f(x)` = 2*x
g(x)` = 4
h(x)` = 0

y` = 2*x + 4 + 0

y` = 2*x + 4
    



#--------OPtimization

f(x)` == 0 

shib 0 beshe

migan aksar jaha , tabe ha
minimum , maximum 
oonjaee k moshtaghe 0 --> minimum , maximum 


optimization --> behine sazi

yek tabe ee koja minimum mazximum
f(x)` ==0 gharar bedan


#------Gradient
Machine learning



#-----higher order derivative
f(x)= x**3
f(x)` = df/dx = y. = 3*x**2
f(x)`` = df2/dx2 = y.. = 6*x
f(x)``` = df3/dx3 = y... = 6
f(x)```` = df4/dx4 = y.... = 0
f(x)````` =0
f(x)````` = 0
order -->daraje


#---Partial derivatives

f(x,y) 
z = 4x + 2y

df/dx -->4
df/dy -->2
df/dxdy -->


'''



#pip install numpy

#==============================
#==============================
''' Numerical Calculation'''
#==============================
#==============================
#pip install sympy
#pip install scipy

#Py --> Python

#sympy --> sym + py --> sym -> symbol --> sambolic
#scipy -->sci + py --> sci --> scietific --> daneshi 
#joftesh rooye Numpy neevshte shode
#mohasebat

#hezaran tabe hezaran documentation
'''
esme ketabkhoen search
website
quick start, get started
tutorial , documentation

in zamano kamtar ->mojhemtarin noakt ro migam
review --> ezafe mikonm


AI - gpt , gemeni , claud --> tadrise in mozo ha

'''

#--------Differentiation---------

#import sympy as sp
import sympy
#sambolic kar mikon --> sambol
#zarfe shoma -> dar asl yek objecti mishe 
#object symbol --> az dele sympy

#nd array az numpy

x= sympy.symbols('x')

print(type(x))
#<class 'sympy.core.symbol.Symbol'>

#f ya tabe at ro tarif mikonid
#math --> math.sin() math.cos()
#numpy --> np.sin() np.cos() ,....
#sympy --> sp.sin() sp.cos()
#exp --> e** felan

f = sympy.sin(x) * sympy.exp(x)
#f = sin(x)*e**x

print(type(f)) #<class 'sympy.core.mul.Mul'>


#zarf
#moshtagh=

#df/dx
#df_dx
#esme zarf
dfdx = sympy.diff(f,x)
print(type(dfdx)) #<class 'sympy.core.add.Add'>
print(f'derivative: {dfdx}')
#derivative: exp(x)*sin(x) + exp(x)*cos(x)


#daraje do begirid
#df/dx2
#moshtagh_2
dfdx2 = sympy.diff(f,x,2)
print(dfdx2)
#2*exp(x)*cos(x)




#-----beri moshtaghe felano too oon noghte bebini
#1--->manual 
#f`(x)=dfdx

print(dfdx)
#exp(x)*sin(x) + exp(x)*cos(x)
import math
dif_at_2= math.exp(2)*math.sin(2) + math.exp(2)*math.cos(2)
print(dif_at_2) #3.643917376788891



#2---->on moshtaghe . subs
value = dfdx.subs(x,2) #valuate at x=2
print(value)
 
#------- 3 ta symbols
#partial
x,y,z = sympy.sybols('x,y,z')
f = sympy.sin(x*y)+ sympy.sin(y*z)

# df/x y**2

dfdxy= sympy.diff(f,x,1,y,2)


#symbolic --> adade daghigho dare
#Numerical --> adadi -> taghrib 
#---------------------
#Symbolic nadar eva javab nmide
import numpy as np
#from scipy.misc import derivative
import scipy

#tabato injori misazi
def f(x):
    return np.sin(x)*np.exp(x)

#moshtaghe f ro rooye x=2 dar biar
#dx --> taeen mikon e too raveshehs 
#adadi inkaro -->taghribie --> 
#har dx -> y jhavabi -->kochik

#dfx_numeric = scipy.misc.derivative(f,2.0 , dx=1e-5)

import scipy
dfx_numeric = scipy.optimize._numdiff.approx_derivative(f,2.0)

print(dfx_numeric) #[3.64391738]

#argment method
x0=2
scipy.optimize._numdiff.approx_derivative(f, x0, method='2-point')   # forward
scipy.optimize._numdiff.approx_derivative(f, x0, method='3-point')   # central (better)


#pip install numdifftools
#higher order derivatives
#Jacobians
#Hessians
#pip install numdifftools
import numdifftools as nd
def f(x):
    return x**3 + 2*x**2
df = nd.Derivative(f)
print(df(2.0))




#--------Integral---------
#masahata zire nemoodar 
#curve --> masahata ziresh --> integral shenakhte


#f --> f(x)`    f --> integral f(x)`

#x**2    --> 2*x moshtyaghe x**2
#----> integral 2*x ---> x**2

import sympy
x= sympy.symbols('x')
f = sympy.sin(x) * sympy.exp(x)

sympy.integrate(f,x)
#exp(x)*sin(x)/2 - exp(x)*cos(x)/2


'''
limit hasho moshakahs koni

curve 

masahate -> 
az manfie binahayat t mosbate binahayat kolesho?
az x=1 ta x=5
limitesh moheme




'''
#sympy.integrate(f,x)

sympy.integrate(f,(x,-1,1))
'''
-E*cos(1)/2 + exp(-1)*cos(1)/2 + exp(-1)*sin(1)/2 + E*sin(1)/2

'''

from sympy import oo

#sympy.oo

sympy.integrate(f,(x,-oo,oo))

#-oo*sign(AccumBounds(-1, 1))


#-----
#scipy --> -np.inf +np.inf


#---------------Numerical anjam bdi-----
#adadi --> taghrib bzni
from scipy.integrate import quad ,dblquad , tplquad

'''
function    purpose
quad        1d integral
dblquad     2d integral
tplquad     3d integral

'''

def f(x):
    return x

x_lower =0
x_upper= 1

quad(f,x_lower,x_upper)
#Out[75]: (0.5, 5.551115123125783e-15)
#a , b 
val , abserr = quad(f,x_lower,x_upper)

print('computed integral:', val) #computed integral: 0.5

#x --> x**2 / 2 
#1/2 
#0/2 = 0 
#1/2 - 0 --> 1/2

#az 0 ta 1 tabeye x-->ye khate
#ag masaate ziesho bekahy hesab -->mosalas
#nesfe morabe
#morabe --> 1 *1 = 1 
#1/2 --> 1/2

print('numerical erropr:',abserr)
#numerical erropr: 5.551115123125783e-15

#scipy --> f(x)

y = lambda x : x**2

y(2) #Out[81]: 4
y(10) #Out[82]: 100

#scipy --> (f) bejaye tabe --> lambda


from scipy.integrate import quad
'''
def f(x):
    return x**2
'''

val , abserr = quad(lambda x : x**2,0,1)




#-----Higher dimension
#dota ingegral

from scipy.integrate import dblquad

def integrant(x,y):
    return np.exp(-x**2 -y**2)

x_lower = 0
x_upper= 10
y_lower = 0
y_upper=10

val , abserr = dblquad(integrant,x_lower,x_upper, lambda x : y_lower , lambda x : y_upper)



'''
Differential , Integral ro ba Scipy, Sympy anjam bdid

symbolic (sympy)           Numerical (Scipy)
Exactl result              approximate nmber
x --> sympy.symbols()       ------
f --> yek equation az x     func f() lambda
.diff()                     .optimization._diff....
integerate()               quad() dblquad() 
sympy.oo                  np.inf
oo -oo                   -np.inf  np.inf
complex -->slow           Very fast [accuracy paen tare]




When sympy?
zamani k riazie daghighmikhay, moadlat
kare theoritixal math riazi anjam midi analytical


when scipy?
vaghty analyticla solution vojod nadare,
tabe kheyli pichidas , va shoma bayad arian yek ravehs
taghribi va numerical result dashte bashi


'''





