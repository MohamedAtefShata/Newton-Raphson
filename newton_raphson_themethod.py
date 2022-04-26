from sympy import *

import sympy as sp

def newton_method(f,xn,number_of_digits,epsilon=0,n = 0):
    
    #get used functions ready
    
    y = sympify(f)
    x = sp.symbols('x')
    y_prime = diff(y,x)
    
    #initialize values
    
    xn_1 = xn - ((y.subs({x:xn}))/(y_prime.subs({x:xn})))
    list_of_values =[Float(xn,number_of_digits)]  
    
    #if we want to use epsilon
    
    if(epsilon != 0):
        while(abs(xn_1-xn)>(epsilon/2)):
            list_of_values.append(Float(xn_1,number_of_digits))
            xn = xn_1
            xn_1= xn - ((y.subs({x:xn}))/(y_prime.subs({x:xn})))
            
    #if we want to use repetition n      
    
    else:
        while (n > 1) :
            list_of_values.append(Float(xn_1,number_of_digits))
            xn = xn_1
            xn_1= xn - ((y.subs({x:xn}))/(y_prime.subs({x:xn})))
            n-=1
            
    #return list of values
    return list_of_values   

def halleys_method(f,xn,number_of_digits,epsilon=0,n = 0):
    
    #get used functions ready
    
    y = sympify(f)
    x = sp.symbols('x')
    y_prime = diff(y,x)
    y_double_prime = diff(y_prime,x)
    
    #initialize values
    h = (2*y.subs({x : xn})*y_prime.subs({x : xn}))/((2*pow(y_prime.subs({x : xn}),2))-(y.subs({x : xn})*y_double_prime.subs({x : xn})))
    xn_1 = xn - h
    list_of_values =[Float(xn,number_of_digits)]  
    
    #if we want to use epsilon
    
    if(epsilon != 0):
        while(abs(float(xn_1-xn))>(epsilon/2.0)):
            list_of_values.append(Float(xn_1,number_of_digits))
            xn = xn_1
            h = (2*y.subs(x, xn)*y_prime.subs(x, xn))/((2*pow(y_prime.subs(x, xn),2))-(y.subs(x, xn)*y_double_prime.subs(x, xn))) 
            xn_1= xn - h
            
    #if we want to use repetition n      
    
    else:
        while (n > 1) :
            list_of_values.append(Float(xn_1,number_of_digits))
            xn = xn_1
            h = (2*y.subs(x, xn)*y_prime.subs(x, xn))/((2*pow(y_prime.subs(x, xn),2))-(y.subs(x, xn)*y_double_prime.subs(x, xn)))
            xn_1 = xn - h
            n-=1
    #return list of values
    return list_of_values
 