# -*- coding: utf-8 -*-
# @Time     : 2019/5/26 20:39
# Author    ：Wang Guosong
# @File     : class_coding_details.py
# @Software : PyCharm

class ShareData:
    spam = 42

x = ShareData()
y = ShareData()
x.spam, y.spam


ShareData.spam = 99
x.spam, y.spam, ShareData.spam

x.spam = 88
x.spam, y.spam, ShareData.spam