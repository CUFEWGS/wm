# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : test.py
# @Software : PyCharm

import sklearn

from sklearn.datasets import load_boston, load_iris, load_digits

boston = load_boston()
print(boston.data.shape)

data, target = load_boston(return_X_y=True)
print(data.shape)
print(target.shape)

iris = load_iris()
print(iris.data.shape)
print(iris.target.shape)
list(iris.target_names)

digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)

import matplotlib.pyplot as plt
plt.matshow(digits.images[0])
plt.show()