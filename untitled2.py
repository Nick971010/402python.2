# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 12:22:34 2023

@author: user
"""

import tkinter as tk
''' tkinter GUI '''
window = tk.Tk()
window.title('Nick_Menu')
window.geometry('500x500')
string = tk.StringVar()
def selection():
    lable.conflg(text = "我喜歡" + string.get())
lable = tk.Label(window,bg = '#f00', text = '尚未選擇')
lable.pack()
radio1 = tk.Radiobutton(window,text = 'python',variable = string, value = 'python',command = selection)
radio1.pack()
radio2 = tk.Radiobutton(window,text = 'c++',variable = string, value = 'c++',
                        command = selection)
radio2.pack()
window.mainloop()