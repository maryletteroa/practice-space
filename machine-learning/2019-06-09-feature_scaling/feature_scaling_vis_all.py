# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2019-06-09 14:18:14
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2019-06-09 15:57:03

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, RobustScaler, Normalizer, StandardScaler
import matplotlib.pyplot as plt

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
    random_state = 1)

STANDARD = ("StandardScaler", StandardScaler())
MINMAX = ("MinMaxScaler", MinMaxScaler())
ROBUST = ("RobustScaler", RobustScaler())
NORMALIZER = ("Normalizer", Normalizer())

scales = (STANDARD, ROBUST, MINMAX, NORMALIZER)

fig = plt.figure()


ax = plt.subplot2grid(shape = (3, 2), loc = (0, 0))
ax.set_title("Unscaled data")
ax.scatter(X_train[:, 0], X_train[:, 1], label = "Train set", s = 60)
ax.scatter(X_test[:, 0], X_test[:, 1], label = "Test set", s = 60)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# ax.set_xlabel("Feature 0")
# ax.set_ylabel("Feature 1")

locs = ((1, 0), (1, 1), (2, 0), (2, 1))
for i, scaler in enumerate(scales):
    X_train_scaled = scaler[1].fit_transform(X_train)
    X_test_scaled = scaler[1].transform(X_test)
    ax = plt.subplot2grid(shape = (3, 2), loc = locs[i])
    ax.set_title(scaler[0])
    ax.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1])
    ax.scatter(X_test_scaled[:, 0], X_test_scaled[:, 1])
    # ax.set_xlabel("Feature 0")
    # ax.set_ylabel("Feature 1")
    ax.spines["left"].set_position("zero")
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

fig.legend(loc = "upper center", ncol = 2)
plt.show()
