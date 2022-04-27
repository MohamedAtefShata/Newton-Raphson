"""
    Root frame file : this file contain all about window view that show to user 
                      frame and input fields and texts 
        
"""
# -- import tkinter library 
import tkinter as tk
from tkinter import ttk

class Root:
    def __init__(self,frame):
        ''' constructoer that draw and configure all component in root'''
        self.frame=frame
        # -----------eauation box frame-------------
        equation_box = ttk.LabelFrame(self.frame, text='Enter Equation', width=600, height=100)
        equation_box.place(x=20, y=10)
        label_f_of_x = ttk.Label(equation_box,text = "f(x)",font=("Arial", 14))
        label_f_of_x.place(x=40,y=10,width=30,height=30)