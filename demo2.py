#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/23 21:16
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# 实例化窗口
root = Tk()
# 设置窗口标题
root.title("标题")

style = Style()
#
# relief
# Determines what the border style of a widget will be. Legal values
# are: "raised", "sunken", "flat", "groove", and "ridge".
style.configure("TButton", font=14, relief="flat", background="#00f5ff")
btn = ttk.Button(text="这只是一个按钮", style="TButton")
btn.pack(pady=20)

root.mainloop()
