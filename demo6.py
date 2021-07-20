#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/24 11:48
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo6.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
指定窗口大小及文字样式
"""
from tkinter import *

win = Tk()
win.geometry("300x200")
# Label(win, text="小扣柴扉久不开", foreground="red", background="#C3DEEF").pack()
# 设置组建的宽度与高度，单位为行
Label(win, text="小扣柴扉久不开", fg="red", bg="#C3DEEF", width=20, height=3).pack()
win.mainloop()
