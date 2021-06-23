#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/23 21:34
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo3.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from tkinter import *


win = Tk()
# 设置窗口标题
win.title("初级应用")
# 在窗口中添加一行文字
text = Label(win, text="\n\ngame over\n\n").pack()

win.mainloop()
