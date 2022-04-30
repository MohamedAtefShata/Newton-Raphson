"""
    Root frame file : this file contain all about window view that show to user 
                      frame and input fields and texts 
        
"""
# -- import tkinter library 
import tkinter as tk
from tkinter import ttk
from widgets.entryplaceholder import *
from tkinter import PhotoImage
from widgets.dialogs import *
#------ matploit ---------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
matplotlib.use('TkAgg')

from newton_raphson_themethod import *
from newton_raphson import *


class Root:
    def __init__(self,frame):
        ''' constructoer that draw and configure all component in root'''
        self.frame=frame
        
        self.type_input=["f(x)=0","root","PI","e"]
        self.type_input_val={"f(x)=0":0,"root":1,"PI":2,"e":3}
        
        self.type_digits=["1 digit","2 digits","5 digits","7 digits","9 digits","11 digits","13 digits","15 digits","16 digits","32 digits","64 digits"]
        self.type_digits_val={"1 digit":1,"2 digits":2,"5 digits":5,"7 digits":7,"9 digits":9,"11 digits":11,"13 digits":13,"15 digits":15,"16 digits":16,"32 digits":32,"64 digits":64}
        
        self.labelfont=labelfont=("Jf Flat", 14)
        self.input_type=0
        self.title_plot_color='white'

        self.__build_equation_box_frame()
        self.__build_equtions_view()
        self.__build_table_view()
        #---------------------------------------------          
    def __build_equation_box_frame(self):
        # -----------eauation box frame-------------
        self.equation_box = equation_box = ttk.LabelFrame(
            self.frame, text='Enter Equation', width=610, height=150
            )
        equation_box.place(x=20, y=10)
        
        # comb = ttk.Label(equation_box,text = "f(x)",font=("Arial", 14))
        # label_f_of_x.place(x=40,y=10,width=30,height=30)
        
        label_comb = ttk.Label(equation_box,text = "select type:",font=("Arial",8))
        label_comb.place(x=10,y=0,width=70,height=20)
        # selection type  combobox
        def type_combbox_event(event):
            self.readonly_combo.selection_clear()
            self.__change_input_type(self.type_input_val[self.readonly_combo.get()])
        self.readonly_combo = ttk.Combobox(
            equation_box, state="readonly", values=self.type_input,font=self.labelfont
        )
        self.readonly_combo.current(0)
        self.readonly_combo.place(x=10,y=20,height=40,width=100)
        self.readonly_combo.bind("<<ComboboxSelected>>",type_combbox_event)
        
        # ===========================================================================
        # ===========================================================================
        
        self.changableBox_place=changableBox_place={"x":130,"y":20,"height":70,"width":480}
        #--------------------------------------------- 
        self.eqatuation_fx=eqatuation_fx=tk.Frame(self.frame)
        eqatuation_fx.place(changableBox_place)
        # equation_text=ttk.Label(self.eqatuation_fx,text = "f(x):",font=("Arial",8))
        # equation_text.place(x=12,y=7,width=80,height=20)
        equation_text=ttk.Label(eqatuation_fx,text = "f(x)=",font=self.labelfont)
        equation_text.place(x=20,y=27,width=40,height=40)
        self.equation_entry_fx=equation_entry_fx=EntryWithPlaceholder(eqatuation_fx,"    Enter f(x) here")
        equation_entry_fx.place(x=65,y=27,width=300,height=40)
        
        x0_text=ttk.Label(eqatuation_fx,text = "X0=",font=self.labelfont)
        x0_text.place(x=375,y=27,width=40,height=40)
        self.x0_entry_fx=x0_entry_fx=EntryWithPlaceholder(eqatuation_fx,"")
        x0_entry_fx.place(x=415,y=27,width=60,height=40)
        
        #--------------------------------------------- 
        
        self.eqatuation_root=eqatuation_root=tk.Frame(self.frame)
        # eqatuation_root.place(changableBox_place)
        #

        text=ttk.Label(eqatuation_root,text = "P=",font=self.labelfont).place(x=20,y=27,width=20,height=40)
        powerOfRoot_entry=EntryWithPlaceholder(eqatuation_root,"power of Root")
        powerOfRoot_entry.place(x=45,y=27,width=100,height=40)
        
        text=ttk.Label(eqatuation_root,text = "X=",font=self.labelfont).place(x=150,y=27,width=20,height=40)
        
        innerOfRoot_entry=EntryWithPlaceholder(eqatuation_root,"inner of Root")
        innerOfRoot_entry.place(x=175,y=27,width=100,height=40)
       
        
        
        # ===========================================================================
        # ===========================================================================
        
        epslion_text=ttk.Label(equation_box , text="ε=",font=("Arial",18))
        epslion_text.place(x=15,y=70,width=35,height=40)
        self.epslion_entry=epslion_entry=EntryWithPlaceholder(equation_box,"10^(-16)")
        epslion_entry.place(x=50,y=70,width=80,height=40)
        
        max_n_text=ttk.Label(equation_box , text="max_n=",font=self.labelfont)
        max_n_text.place(x=135,y=70,width=65,height=40)
        self.max_n_entry=max_n_entry=EntryWithPlaceholder(equation_box,"1000")
        max_n_entry.place(x=205,y=70,width=60,height=40)
        
        numberofdigits_text=ttk.Label(equation_box , text="digits:",font=self.labelfont)
        numberofdigits_text.place(x=275,y=70,width=50,height=40)
        self.number_of_digits_combobox=number_of_digits_combobox = ttk.Combobox(
            equation_box, state="readonly", values=self.type_digits,font=("Jf Flat",12)
        )
        number_of_digits_combobox.current(0)
        number_of_digits_combobox.place(x=330,y=70,height=40,width=100)
        number_of_digits_combobox.bind("<<ComboboxSelected>>", 
                                       lambda e:number_of_digits_combobox.selection_clear())
        solve_btn=ttk.Button(equation_box,text="solve",style="Accent.TButton",command=self.solve_command)
        solve_btn.place(x=500,y=70,height=40,width=85)
        
        
    def __build_table_view(self):
        self.tabel_data=tabel_data = ttk.Treeview(self.frame)
        tabel_data.place(x=20, y=170,width=580,height=200)
        # add scrollbars
        # sx = ttk.Scrollbar(self.frame, orient='horizontal', command=tabel_data.xview)
        # sx.place(x=20,y=160+200,width=600,height=20)
        sy = ttk.Scrollbar(self.frame, orient='vertical', command=tabel_data.yview)
        sy.place(x=20+580,y=170,width=30,height=200)
        tabel_data.configure(yscrollcommand=sy.set,)
        
        tabel_data['columns'] = ('step', 'nx','nxh')
        
        tabel_data.column("#0", width=0,  stretch=tk.NO)
        tabel_data.column("step",anchor=tk.CENTER, width=70)
        # tabel_data.column("fx",anchor=tk.CENTER,width=95)
        # tabel_data.column("fdx",anchor=tk.CENTER,width=95)
        # tabel_data.column("fddx",anchor=tk.CENTER,width=95)
        tabel_data.column("nx",anchor=tk.CENTER,width=110)   
        tabel_data.column("nxh",anchor=tk.CENTER,width=110)
        
        tabel_data.heading("#0",text="",anchor=tk.CENTER)
        tabel_data.heading("step",text="n",anchor=tk.CENTER)
        # tabel_data.heading("fx",text="f(x_)",anchor=tk.CENTER)
        # tabel_data.heading("fdx",text="f'(x_)",anchor=tk.CENTER)
        # tabel_data.heading("fddx",text="f\"(x_)",anchor=tk.CENTER)
        tabel_data.heading("nx",text="Newton/Raphson",anchor=tk.CENTER)
        tabel_data.heading("nxh",text="Halleyss",anchor=tk.CENTER)
        
        self.table_row_next_id=0
        tabel_data.tag_configure('oddrow', background='white')
        
           
        
        
        # tabel_data.insert(parent='',index='end',iid=0,text='',
        # values=('1','fx','fdx','fddx', '0', '0'),tags = ('oddrow',))
        # tabel_data.insert(parent='',index='end',iid=0,text='',
        # values=('1','fx','fdx','fddx', '0', '0'),tags = ('oddrow',))
       
        
    def __insert_to_table(self,vals):
        self.tabel_data.insert(parent='',index='end',iid=self.table_row_next_id,text='',
        values=vals,tags = ('evendrow'if self.table_row_next_id %2==0 else'oddrow',))
        
        self.table_row_next_id=self.table_row_next_id+1
    def __build_equtions_view(self):
        '''
            function to build equtions matploit views in frame
        '''
        
        entered_equation_live_view_width=350
        entered_equation_live_view_height=380
        entered_equation_live_view_dpi=100
        
        entered_equation_live_view=ttk.Label(self.frame,padding=0)
        entered_equation_live_view.place(x=640,y=50,width=entered_equation_live_view_width,height=entered_equation_live_view_height)
        
        self.fig = matplotlib.figure.Figure(figsize=((entered_equation_live_view_width/entered_equation_live_view_dpi),
                                                (entered_equation_live_view_height/entered_equation_live_view_dpi)),
                                                 dpi=entered_equation_live_view_dpi)
        
        self.fig.set_facecolor('#fafafa')
        self.canvas = FigureCanvasTkAgg(self.fig, master=entered_equation_live_view)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas._tkcanvas.pack(side="top", fill="both", expand=True)
        self.fig.subplots_adjust(left=0,right=0.99,top=1,bottom=0.01,hspace=0.1,wspace=0.1)
        
        
        self.ax_x_val = self.fig.add_subplot(811)
        # self.ax.set_facecolor('xkcd:salmon')
        self.ax_x_val.get_xaxis().set_visible(False)
        self.ax_x_val.get_yaxis().set_visible(False)
        self.ax_x_val.text(0.5, 0.5, "x=", horizontalalignment='center',
                                   verticalalignment='center', fontsize='xx-large') 
        # self.ax_x_val.set_title("Entered Equation:")
        
        self.ax_fx = self.fig.add_subplot(812)
        self.ax_fx.get_xaxis().set_visible(False)
        self.ax_fx.get_yaxis().set_visible(False)
        self.ax_fx.text(0.5,0.5,"f(x)=",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_fdx = self.fig.add_subplot(813)
        self.ax_fdx.get_xaxis().set_visible(False)
        self.ax_fdx.get_yaxis().set_visible(False)
        self.ax_fdx.text(0.5,0.5,"f'(x)=",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_fddx = self.fig.add_subplot(814)
        self.ax_fddx.get_xaxis().set_visible(False)
        self.ax_fddx.get_yaxis().set_visible(False)
        self.ax_fddx.text(0.5,0.5,"f\"(x)=",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_xn_newton = self.fig.add_subplot(816)
        self.ax_xn_newton.get_xaxis().set_visible(False)
        self.ax_xn_newton.get_yaxis().set_visible(False)
        self.ax_xn_newton.set_title("Newtom/Raphson")
        self.ax_xn_newton.text(0.5,0.5,"$X_n= x_{n-1}+\\frac{f(x)}{f'(x)}$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_xn_halley = self.fig.add_subplot(818)
        self.ax_xn_halley.get_xaxis().set_visible(False)
        self.ax_xn_halley.get_yaxis().set_visible(False)
        self.ax_xn_halley.set_title("halleys_method")
        self.ax_xn_halley.text(0.5,0.5,"$X_n= x_{n-1}$",fontsize='large',horizontalalignment='center', verticalalignment='center')
    def __set_ax_values(self,x_val="",fx="",fdx="",fddx="",xnewton="",xhalley=""):
        self.ax_fx.clear()    
        self.ax_fx.text(0.5,0.5,"$f(x)="+fx+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_x_val.clear()    
        self.ax_x_val.text(0.5,0.5,"$x="+str(x_val)+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_fdx.clear()    
        self.ax_fdx.text(0.5,0.5,"$f'(x)="+fdx+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_fddx.clear()    
        self.ax_fddx.text(0.5,0.5,"$f''(x)="+fddx+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_xn_newton.clear()  
        self.ax_xn_newton.set_title("Newtom/Raphson")  
        self.ax_xn_newton.text(0.5,0.5,"$X_n= x_{n-1}-"+xnewton+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.ax_xn_halley.clear()
        self.ax_xn_halley.set_title("Halley ")
        self.ax_xn_halley.text(0.5,0.5,"$X_n= x_{n-1}-"+xhalley+"$",fontsize='large',horizontalalignment='center', verticalalignment='center')
        
        self.canvas.draw()
            
    def solve_command(self):
        epsilon=self.epslion_entry.get()
        max_n=self.max_n_entry.get()
        digits=self.type_digits_val[self.number_of_digits_combobox.get()]
        view_list=[]
        newt=''
        if self.input_type==0:
            eq=self.equation_entry_fx.get()
            x0=self.x0_entry_fx.get()
                    # -----------check_input-------------
            try:
                sympify(eq)
            except:
                worried = PhotoImage(file='img\worried2.png')
                show_message("Error in Equation", "you enter wrong equation in f(x).\nCheck your entered equation.",icon=worried)
                
            newt=NewtonRaphson(eq,x0,number_of_digits=digits,max_n=int(max_n),epsilon=epsilon)
            view_list=newt.itteration_list
            
        
        self.__set_ax_values(x_val=newt.x_val, 
                             fx=latex(newt.fx), 
                             fdx=latex(newt.f_prime), 
                            fddx=latex(newt.f_d_prime), 
                            xnewton=latex(newt.newton_rational),
                            xhalley=latex(newt.halley_rational)
                            )
        self.tabel_data.delete(*self.tabel_data.get_children())
        self.table_row_next_id=1
        for row in view_list:
            self.__insert_to_table([row["n"],row["newton"],row["hally"]])
        # print("x")
                
    def __change_input_type(self,type_val):
            # print(self.readonly_combo.get())
            # self.frame.focus_set()
            self.input_type=type_val
            
            hide=lambda e: {e.pack_forget() , e.pack() }
            show=lambda e:e.place(self.changableBox_place)
            
            if type_val==0:
                show(self.eqatuation_fx)#.place(self.changableBox_place)
                hide(self.eqatuation_root)#.pack_forget(),self.eqatuation_root.pack()
            elif type_val== 1:
                hide(self.eqatuation_fx)    
                show(self.eqatuation_root)
            else:
                hide(self.eqatuation_fx)
                hide(self.eqatuation_root)
                
    def change_theme_mode(self,them_mode):
        
        
        if them_mode=="light":
            self.title_plot_color='black'
            self.fig.set_facecolor('#fafafa')
            self.tabel_data.tag_configure('oddrow', background='white')

        else :
            self.title_plot_color='white'
            self.fig.set_facecolor('#1c1c1c')
            self.tabel_data.tag_configure('oddrow', background='black')

        self.ax_xn_newton.set_title("Newtom/Raphson",color=self.title_plot_color) 
        self.ax_xn_halley.set_title("Halley ",color=self.title_plot_color)
        
  
        
        self.canvas.draw()
    
    