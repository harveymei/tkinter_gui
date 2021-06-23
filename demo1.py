#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/23 20:55
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo1.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
使用tkinter模块在窗口中添加Button组件
"""
# 导入模块
from tkinter import *

# 实例化窗口
win = Tk()
# 添加窗口标题
win.title("这是一个ttk小demo")
# 添加按钮组件
# 设置按钮上的文字，字号，边框样式，背景颜色
btn = Button(win, text="这只是一个按钮", font=14, relief="flat", bg="#00f5ff")
# 包装按钮，让按钮显示在窗口
btn.pack(pady=20)

win.mainloop()
