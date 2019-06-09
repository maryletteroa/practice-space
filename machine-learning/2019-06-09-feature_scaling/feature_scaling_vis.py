# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2019-06-09 10:35:27
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2019-06-09 14:49:34


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, RobustScaler, Normalizer, StandardScaler
import matplotlib.pyplot as plt

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
            random_state = 1)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

fig, axes = plt.subplots(2, figsize = (8, 8))
axes[0].scatter(X_train[:, 0], X_train[:, 1],
    label = "Training set", s = 60)
axes[0].scatter(X_test[:, 0], X_test[:, 1],
    label = "Test set", s = 60)
axes[0].legend(loc = "upper left")
axes[0].set_title("Original Data")



axes[1].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
    label = "Training set", s = 60)
axes[1].scatter(X_test_scaled[:, 0], X_test_scaled[:, 1],
    label = "Test set", s = 60)
axes[1].legend(loc = "upper left")
axes[1].set_title("Scaled Data")

for ax in axes:
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")
fig.tight_layout()

plt.show()
