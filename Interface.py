import tkinter as tk
import tkinter.messagebox
import pickle
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Mouse_Getter import *
import time



window = ttk.Window(themename="minty")
window.resizable(False,False)
window.title('o7')
window.geometry('400x350')


l=tk.Label(window, text="EVE ONLINE MINER BOT", fg='black', font=('Arial', 12), width=30, height=2)
l.pack()



def about():
    webbrowser.open("https://github.com/Andyli807/EVE_ONLINE_MINER_BOT")

def setting_window():
    window_setting = tk.Toplevel(window)
    window_setting.geometry('250x250')
    window_setting.title('SETTING')
    window_setting.wm_attributes('-topmost',True)
    window_setting.resizable(False,False)


def start_window():
    window_setting = tk.Toplevel(window)
    window_setting.geometry('250x250')
    window_setting.title('BOT WORKING')
    window_setting.wm_attributes('-topmost',True)
    window_setting.resizable(False,False)

def initialize():
 

    test(False)
    print(111)






btn_initialize = tk.Button(window, text='Initialize', fg='black', font=('Arial', 13), width=20, height=1, command=initialize)
btn_initialize.place(x=45, y=60)
btn_setting = tk.Button(window, text='Setting', fg='black', font=('Arial', 13), width=20, height=1, command=setting_window)
btn_setting.place(x=45, y=120)
btn_start = tk.Button(window, text='Strat', fg='black', font=('Arial', 13), width=20, height=1, command=start_window)
btn_start.place(x=45, y=180)
btn_about = tk.Button(window, text='About', fg='black', font=('Arial', 13), width=20, height=1, command=about)
btn_about.place(x=45, y=240)



window.mainloop()