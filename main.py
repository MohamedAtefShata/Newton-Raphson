
###########################################################
##         IMPORT Libraries
###########################################################
#-----Tkinter--------
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import PhotoImage


from rootframe import Root



'''--------------------------------------------------- 
            Main Function
---------------------------------------------------'''
if __name__ == "__main__":
    #--- intialize frame size and data
    frame = tk.Tk()       
    frame.title("Newton-Raphson solver")
    # --- configratuion frame proparties( heigth and width and location) ---
    width=1000
    height=450
    screenwidth = frame.winfo_screenwidth()
    screenheight = frame.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    frame.geometry(alignstr)
    frame.resizable(width=True, height=True)
    
    #----- load theme -----------
    style = ttk.Style(frame)
    frame.tk.call("source", "sun-valley/sun-valley.tcl")
    frame.tk.call("set_theme", "light")
    style.configure('Accent.TButton', font=('JF flat', 13),padding=0)
    style.configure("Placeholder.TEntry", foreground="#c2c2c2")

    root=Root(frame)
    
    # run frame
    frame.mainloop()
    