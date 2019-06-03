# -*- coding: utf-8 -*-
# @Time     : 2019/5/30 13:52
# @Author    ：Wang Guosong
# @File     : eg_call_method.py
# @Software : PyCharm


class Callback:

    def __init__(self, color): # Class with state information
        self.color = color

    def changeColor(self): # A normal named method
        print('turn', self.color)


cb1 = Callback('blue')
cb2 = Callback('yellow')
cb1 = Callback('blue')
obj = cb1.changeColor # Registered event handler
obj()
obj2 = cb1.changeColor()