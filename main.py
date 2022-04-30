
###########################################################
##         IMPORT Libraries
###########################################################
#-----Tkinter--------
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import PhotoImage


from rootframe import Root

def change_theme(frame,rootframe,val):
    # NOTE: The theme's real name is sun-valley-<mode>
    # print(agreement.get())
    rootframe.change_theme_mode(val)
    if  val=="light":#root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        frame.tk.call("set_theme", "light")
        style.configure("Placeholder.TEntry", foreground="#c2c2c2")

    else:
        # Set dark theme
        # rootframe.fig.set_facecolor('#1c1c1c')
        frame.tk.call("set_theme", "dark")
        style.configure("Placeholder.TEntry", foreground="#a1a1a1")

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
    # root.change_theme_mode("dark")
    
    # change theme switch
    agreement = tk.StringVar(value="dark")
    

    # var_2.trace(mode, callback)
    switch = ttk.Checkbutton(
                frame, text="Dark", style="Switch.TCheckbutton",
                variable=agreement,
                onvalue='dark',
                offvalue='light',
                
                command=lambda :change_theme(frame,root,agreement.get())
            )
    switch.place(x=900,y=15,width=100,height=30)
    
    change_theme(frame,root,"dark")
    
    
    # run frame
    frame.mainloop()
    