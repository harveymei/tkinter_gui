#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/23 21:38
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo4.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
设置窗口样式
"""
# 导入模块
from tkinter import *

# 实例化窗口
win = Tk()
# 设置标题
win.title("标题")
# 设置窗口宽度与高度，中间字符位字母"x"，单位为像素
win.geometry("300x150")
#
win.configure(bg="yellow")
win.maxsize(500, 500)
couple = "\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：真我风采"
txt = Label(win, text=couple, bg="yellow").pack()
win.mainloop()
