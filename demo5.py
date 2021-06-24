#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/24 10:02
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo5.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
设置窗口大小及位置
"""

from tkinter import *

win = Tk()
win.title("窗口位置")
# 设置窗口背景颜色
win.configure(bg="#a7ea90")
# 赋值窗口宽高变量
winw = 300
winh = 220
# 获取屏幕宽高赋值变量，单位：像素
scrw = win.winfo_screenwidth()
scrh = win.winfo_screenheight()
# 屏幕宽高减窗口宽高除2分别赋值x与y变量
x = (scrw - winw) / 2
y = (scrh - winh) / 2
# 通过计算得出的x和y坐标值，使窗口在屏幕中居中显示
# 格式户字符串
win.geometry("%dx%d+%d+%d" % (winw, winh, x, y))
hello = "这里\n是一\n句话"
txt = Label(win, text=hello, bg="#a7ea90").pack()

win.mainloop()
