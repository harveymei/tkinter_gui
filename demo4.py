#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/6/23 21:38
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: demo4.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from tkinter import *


win = Tk()
win.title("标题")
win.geometry("300x150")
win.configure(bg="yellow")
win.maxsize(500, 500)
couple = "\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：真我风采"
txt = Label(win, text=couple, bg="yellow").pack()
win.mainloop()
