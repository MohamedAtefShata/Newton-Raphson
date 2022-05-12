
from sympy import *

import sympy as sp

class NewtonRaphson:
    
    def __init__(self,fx,x0,number_of_digits=1,epsilon=10**-16,max_n = 1000):
        self.fx=fx = sympify(fx)
        x = sp.symbols('x')
        self.f_prime=f_prime = diff(fx,x)
        self.f_d_prime =f_d_prime = diff(f_prime,x)
        epsilon=sympify(epsilon)
        # solve_xi=lambda xi_1:  xi_1 - ((fx.subs({x:xi_1}))/(f_prime.subs({x:xi_1})))
        # formatDigits='.'+str(number_of_digits)+"f"
        self.newton_rational=sympify(fx/f_prime)
        
        self.halley_rational=sympify((2*fx*f_prime)/ ( (2*f_prime*f_prime)-(fx*f_d_prime)  ) )
        
        self.itteration_list=[]
        
        self.x_val=xn_1=xn=x0=Float(x0,number_of_digits)
        
        i=1
        
        while  True:
            e = sp.symbols('e')
            xn.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            xn_1=xn
            xn_1.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxi=fx.subs({x:xn_1})
            fxpi=f_prime.subs({x:xn_1})
            fxdpi=f_d_prime.subs({x:xn_1})
            fxi=fxi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxpi=fxpi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxdpi=fxdpi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            xn=Float((xn_1- (fxi/fxpi)))
            self.itteration_list.append({"n":i,
                              # "fx":fxi,
                              # "fdx":fxpi,
                              # "fddx":fxdpi,
                               "newton":f'{xn}',
                               "hally":"--"
                               
                               })
            
            i+=1
            
            if (abs(xn-xn_1)<(epsilon/2)) or i>max_n: 
                break
        self.x_val=xn
        max_n=i-1
        xn=xn_1=x0
        i=0
        while  True:
            xn_1=xn
            xn.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            xn_1.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxi=fxi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxpi=fxpi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            fxdpi=fxdpi.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            # fxi=fx.subs({x:xn_1})
            # fxpi=f_prime.subs({x:xn_1})
            # fxdpi=f_d_prime.subs({x:xn_1})
            h=self.halley_rational.subs({x:xn_1})   #(2*fxi*fxpi)/((2*fxpi*fxpi)-(fxi*fxdpi))
            h = h.subs({e: 2.718281828459045235360287471352662497757247093699959574966967627724076630353})
            xn=Float(xn_1 -h,number_of_digits)
            
            self.itteration_list[i]["hally"]=f'{Float(xn):.{number_of_digits}f}'
            i+=1
            # print(abs(Float(xn-xn_1,number_of_digits+1)))
            if (abs(Float(xn-xn_1,number_of_digits+1))<(epsilon/2)) or i>=max_n: 
                break
            