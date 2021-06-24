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
win.title("这里是窗口位置")
# 设置窗口背景颜色
win.configure(bg="#a7ea90")
# 赋值窗口宽高变量
win_w = 300
win_h = 220
# 获取屏幕宽高赋值变量，单位：像素
screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()
# 屏幕宽高减窗口宽高除2分别赋值x与y变量
x = (screen_w - win_w) / 2
y = (screen_h - win_h) / 2
# 通过计算得出的x和y坐标值，使窗口在屏幕中居中显示
# 格式户字符串
win.geometry("%dx%d+%d+%d" % (win_w, win_h, x, y))
hello = "锄禾日当午\n汗滴禾下土\n谁知盘中餐\n粒粒皆辛苦"
txt = Label(win, text=hello, bg="#a7ea90")
txt.pack()

win.mainloop()
