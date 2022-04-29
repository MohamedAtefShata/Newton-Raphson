
from sympy import *

import sympy as sp

class NewtonRaphson:
    
    def __init__(self,fx,x0,number_of_digits=1,epsilon=10**-16,max_n = 1000):
        self.fx=fx = sympify(fx)
        x = sp.symbols('x')
        self.f_prime=f_prime = diff(fx,x)
        self.f_d_prime =f_d_prime = diff(f_prime,x)
        # solve_xi=lambda xi_1:  xi_1 - ((fx.subs({x:xi_1}))/(f_prime.subs({x:xi_1})))
        # formatDigits='.'+str(number_of_digits)+"f"
        self.newton_rational=sympify(fx/f_prime)
        
        
        
        self.itteration_list=[]
        
        self.x_val=xn_1=xn=x0=Float(x0,number_of_digits)
        
        i=1
        
        while  True:
            xn_1=xn
            fxi=fx.subs({x:xn_1})
            fxpi=f_prime.subs({x:xn_1})
            fxdpi=f_d_prime.subs({x:xn_1})
            xn=Float(xn_1- (fxi/fxpi))
            xn=xn.round(number_of_digits)
            self.itteration_list.append({"n":i,
                              "fx":fxi,
                              "fdx":fxpi,
                              # "fddx":fxdpi,
                               "newton":xn,
                               
                               })
            
            i+=1
            # print(abs(Float(xn-xn_1,number_of_digits+1)))
            if (abs(Float(xn-xn_1,number_of_digits+1))<(epsilon/2)) or i>max_n: 
                break
        self.x_val=xn
        # xn=xn_1=x0
        # i=0
        # while  True:
            # xn_1=xn
            # xn=
        
            

# newt=NewtonRaphson("x**2-2",1,number_of_digits=4)
# for e in newt.itteration_list:
#     print(e)
#
