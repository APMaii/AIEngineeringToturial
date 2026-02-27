"""
Created on Fri Feb 27 09:20:24 2026

@author: Ali Pilehvar Meibody



Numerical calculation
Mohasebate Adadi

"""

#==============================
''' Numerical modeling '''
#==============================
'''

aksaran yek tabe ee darid mikhahid on tabe ro hal konid

x**2 + 4*x = 8

ch x i inja gharar begire --> in moadele doros dar miad
hale masale

x**2 + 4*x - 8 =0

x dar in tabe -->0

f(x)=0
f(x)=c
f(x)-c =0
g(x)=0

tabe = 0 

halesh koni



3 ravesh vojod dare
1-Analythical --> exact number -->daghigh hal mishe
2- Numerical --> taghrib taghribe adadi
3- Graphically ->hal mikoni nemoodar mikeshi


donyaye computer, machine learning -->moadele hal mikone



ma bayad tamame Equation (moadelat ro) daste badni konim

hameye inaro balad bashim? na
negah kon behesh asan 2 mah tol bkshe
har hafte do ghesmat 50 khato yad migirm ba detail ba gpt

'''

#===================================
'''     1- Linear Algebric  Equation '''
#===================================

#linear --> khatie , algebric --> jabri , moadele

#ax + b =0

#4*x -8 =0
#4*x = 8
#x = 8/4 = 2 

#analytical
import sympy

x=sympy.symbols('x')

#f 
eq = 4*x - 8

sol = sympy.solve(eq,x)
print(sol) #[2]


# X sakhtan tooye sympy
#x = Symbol('x' , real= True)
#x = Symbol('x' , positive = True)
#x = rational(4,5)

#-----------
import numpy as np 
import sympy
x = sympy.symbols('x')
f_symb = (x + sympy.pi)**2
f=sympy.lambdify([x],f_symb,'numpy')
print(type(f)) #<class 'function'>

x_vec = np.linspace(0, 10,100)
f_vec = f(x_vec)
print(f_vec)


import matplotlib.pyplot as plt

plt.scatter(x_vec,f_vec,s=5)
plt.ylabel('f nmpy')
plt.xlabel('x')
plt.title('Symbolic to Numpy visualization')
plt.grid()
plt.show()




#------sympy
sympy.expand((x+1)*(x+2)*(x+3))
#x**3 + 6*x**2 + 11*x + 6


#----
#1/(x+1 - 1/x+2

f1 = 1/ ((x+1)*(x+2))
sympy.apart(f1)
#-1/(x + 2) + 1/(x + 1)



f2 = 1/(x+1) + 1/(x+3)
sympy.together(f2)
#2*(x + 2)/((x + 1)*(x + 3))



#---sigma --> Sum,s and products
n = sympy.symbols('n')
#zigma 1/n**2   n 1-->10

#1/1**2 + 1/2**2 + 1/3**2 + 1/4**2 +....+ 1/10**2

sympy.Sum(1/n**2,(n,1,10))
#Sum(n**(-2), (n, 1, 10))

sympy.Sum(1/n**2,(n,1,10)).evalf() #1.54976773116654



sympy.Sum(1/n**2,(n,1,sympy.oo)).evalf() #1.64493406684823



#--> + Suym , zarb she beynesh ---> product

#n -->  1 ta 10 
#1 * 2 * 3 * 4 ..* 10 -->10!
#1/x 
#1/sx**2


sympy.Product(n,(n,1,10))
#Product(n, (n, 1, 10))

sympy.Product(n,(n,1,10)).evalf() #3628800.00000000



#----Limits
sympy.limit(sympy.sin(x)/x , x,0) #1


#-----
#e*x -- 1 + x + x**2/2 + x**3/6 + ...
sympy.series(sympy.exp(x),x)
#1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + O(x**6)


sympy.series(sympy.exp(x),x,1)
'''
E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + O((x - 1)**6, (x, 1))

'''


sympy.series(sympy.exp(x), x, 1, 10)
'''
E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + E*(x - 1)**6/720 + E*(x - 1)**7/5040 + E*(x - 1)**8/40320 + E*(x - 1)**9/362880 + O((x - 1)**10, (x, 1))

'''


#---special tabe
from scipy.special import jn , yn 
#bassel function






#===================================
'''     2- Non-Linear Algebric  Equation '''
#===================================
#linear algebbric equation ha  --> okeye
#4*x ++ 8 --> analytical hal mishe (daghigh)
#niazi b numerical (adadi) taghrib nadarad


#Non-Linear
'''
qudratic --> ax**2 + bx + c =0
cubic --> ax**3 + bx**2 + c*x + d =0
exponential --> e**x - ...
logarithmic --> log , ln ... 
trigonometric --> sin(x) = 1.05

'''

#-----Analytical
#ax**2 + bx + c =0

#b*2 - 4ac --> delta
#delta + - 0 

#delta manfi javab nadasht
#delta = 0  -b/2a
#delta> --> x1 = -b + radical delta / 2a ||| x2 = -b - radical delta / 2a

#a*x**2 + b*x + c =0
import math
def solve_quadratic(a,b,c):
    delta = b**2 - 4 * a *c
    if delta<0:
        print('javab nadarad')
        return None
    
    elif delta==0:
        x = -1 * b  / 2*a
        return x
    
    else:
        x1= (-b + math.sqrt(delta))/2*a
        x2= (-b - math.sqrt(delta))/2*a
        return x1,x2
    

#x**2 -3x + 2 = 0

#delta --> 9 - 8  = 1 

#r1= - -3 + 1 / 2 = 2
#r2= - - 3 - 1 / 2 = 1
#(x-1)(x-2) = 0 

solve_quadratic(1,-3,2)
#Out[104]: (2.0, 1.0)



#sympy --> anlyical
#import sympy
#sympy symbols

from sympy import symbols, solve


x = symbols('x')
eq = x**2 - 3*x +2

solution = solve(eq,x)

print(solution) #[1, 2]




eq = sympy.sin(x) - 0.5

solution = solve(eq,x)

print(solution) #[0.523598775598299, 2.61799387799149]



eq = sympy.log(x) -100
solution = solve(eq,x)
print(solution) #[exp(100)]



#gahan yek non linear equation --> kh skahte
#yani asan anlytically nemitone javab dashte bashe
#---> Numerical taghribi 
'''
alaghe mande mitone riazisho bekhone


iteration methods---> g(x) = x with intiial guess and .....

wegeshtain method ---> more speed up because we have x1=g(x0) so
x m+1 = xm-1 g(x) .....


Newton Method --> first we have initial guess (x0) and then we havederivatiev f'(x0) and 
we must know each cross y=0 at which point and this is our new x and .......
f'(x0) = f(x0) / x0 - x1
X m+1 = xm - f(xm)/f'(xm)

secant method --> instead of f'() we use the approixmated of that 


Bisection method --> f(a) and f(b) must be non same sign and ..
c= a+b/2 --> f(c) and then ....

'''
#scipy 
#bisect
from scipy.optimize import bisect

def f(x):
    return x**3 - x - 2  # Example function

root = bisect(f, 1, 2)  # Bracketing between 1 and 2
print(root)


#--newtono
from scipy.optimize import newton

def f(x):
    return x**3 - x - 2

def df(x):  # Derivative
    return 3*x**2 - 1

root = newton(f, x0=1.5, fprime=df)  # Starts at x0=1.5
print(root)

#-----
from scipy.optimize import fixed_point

def g(x):
    return (x + 2/x)**0.5  # Example transformation

root = fixed_point(g, x0=1.5)
print(root)





#---ROOT -->khodesh tarjih mide az methdoe
##Uses various numerical solvers (Newton, Broyden, Hybr, LM, etc.).


from scipy.optimize import root

def f(x):
    return x**3 - x - 2

x0 = 1.5  # Initial guess

sol = root(f, x0, method='hybr')  # Hybrid method (default)
print(sol.x)  # Root found
'''
hybr	Trust Region	General Problems (Default)
lm (Levenberg-Marquardt)	Trust Region	Nonlinear Least Squares
broyden1	Quasi-Newton	Large Sparse Problems
broyden2	Quasi-Newton	Large Sparse Problems
anderson	Iterative	Fixed-Point Problems
krylov	Iterative	Large Systems
diagbroyden	Quasi-Newton	Diagonal Jacobians
excitingmixing	Iterative	Physics & Engineering
linearmixing	Iterative	Fixed-Point Equations
'''




#---sympy --> solve --> nsolve (numerical solve) --> newton raphson
import sympy

x = sympy.symbols('x')
eq = x**3 - x - 2

#solution = sympy.solve(eq,x)

root = sympy.nsolve(eq,x,1.5) #intiial guess
print(root)



#-----------
#1-Linear Algebric equations --> analytical
#2-Non-Linear Algebric Equations --> analytical  + Numerical (metyhod ha)

#algberic (lin, non-lin)
#hamashon yedone equation bodan
#ag chanta dashte bashim ? --> equation systems

#==============================================
'''     3- Linear Algebric System equations '''
#==============================================
'''
system az dota moadele hast


2*x + y = 5
x - y = 1


dasti k mizanid

3*x = 6
x = 2

2*2 + y = 5
y=1


migan ino b forme matrix beneviss



2*x + y = 5
x - y = 1


A*x = B
A --> matrix zarayeb
x --> majhool
B --> matrixe javab



|2    1|   |x|      |5|
|1   -1|  |y|    =  |1|

A = |2    1|   
    |1   -1|
    
    
    |x|
x = |y|

   |5|
b =|1|



har equation sytems ro besoorate yek matrix benevisid



Cramer’s rule  --> X = | | / | | --> not efficient
Gussian Elimination ---> Can have numerical instability
Gauss Jordan 
Matrix Inversion:--->Ax=B  A-1 Ax=A-1 b  Ix=x=A-1b
LU Decomposition
Cholesky Decomposition

'''


#---Gussian Elimination / Substitution
#analytically 
import  sympy
x , y = sympy.symbols('x,y')
eq1 = sympy.Eq(2*x + 3*y , 7)
eq2 = sympy.Eq(4*x +y , 5 )
solution = sympy.solve((eq1,eq2),(x,y))

solution[x] #4/5

solution[y] #9/5



#----LU decomposition
#--cholesky decomposition


#analytical
# Eq

#----------------
#fast tar , sari tar in equation haro hal konim
#4*x + 1y = 1
#1*x + 3*y = 2
import numpy
a = np.array([[4,1],[1,3]])
print(a)

'''
matrix zarayeb
[[4 1]
 [1 3]]
'''
b= np.array([1,2])
print(b)
#[1 2]

#A * x = B

from scipy.sparse.linalg import cg

x,info = cg(a,b)

print(x) #[0.09090909 0.63636364]

#symmetric positibve 



#genmerlize minima residual method
from scipy.sparse.linalg import gmres

x , info = gmres(a,b)
#slow 
print(x) #[0.09090909 0.63636364]

print(4*0.09090909  + 1*0.63636364) #1.0
print(1*0.09090909 + 3*0.63636364) #2.00000001



#==============================================
'''     4- Non-Linear Algebric System equations '''
#==============================================

#analytically 
import sympy

x,y= sympy.symbols('x,y')

eq1= sympy.Eq(x**2 + y**2 , 4)
eq2 = sympy.Eq(4*x+3*y , 2)

solution = sympy.solve((eq1,eq2),(x,y))



#numerical hal konid
#Grober basis
from sympy import nonlinsolve
x,y= sympy.symbols('x,y')
solutions = nonlinsolve([x**2 + y**2-4 ,4*x+3*y-2 ], (x,y))


'''
--------ALGEBRIC---------- Jabri
1-linear algebric equation -> analytical (sympy)
2- Non-linear algebric equation --> analytical (sympy) numerical (scipy)
3- Linear algebric system equations  **mohemtrin
4- Non-linear algberic system equations ( rare)


gheyre jabri --> Differential
5- Differential Equations -->yedone equation
moshtagh dare

Ordinary differential equation (ODE)

f(x,y,y`,y``,...)=0

dy/dx + y = 0


y`` + y` + 2*y = 0 



Parial differential equation (PDE)
f(x1,x2,y, dy/dx1 , dy/dx2,....)=0




6- Differential System equations 
dy/dx + y = 0
dy/dx + 2*y = 0
dy2/dx2 + 4y=0




na ma niazi darim behesh na asan dakhele elme compute bekar miad
mire tooye hite physic complex system


dakhele MD --> alaghe mand hastan ham 
ham reference ,
ghesmataye avaliasho por konm

AI_Diffeerential_Numerical_Solution.md

'''











