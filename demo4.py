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
# geometry
# This is a string of the form widthxheight, where width and height are measured in pixels
# for most widgets (in characters for widgets displaying text). For example: fred["geometry"] = "200x100".
win.geometry("300x150")
# 设置窗口背景颜色
win.configure(bg="yellow")
# 设置窗口的最大尺寸（即最大化按钮或拖拉水平和垂直边框所能得到的最大窗口）
win.maxsize(500, 500)
# 定义字符串变量（9行）
couple = "\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：真我风采"
# 设置Label赋值变量并包装显示
# 此处的背景色为标签的背景色，如不设置，默认为白色。
txt = Label(win, text=couple, bg="yellow")
txt.pack()

win.mainloop()
