# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2019-06-09 15:09:53
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2019-06-09 15:16:26

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
        random_state = 1)

svm = SVC(C=100)
svm.fit(X_train, y_train)
score = svm.score(X_test, y_test)
print(f"Test set accuracy: {score:.2f}")

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm.fit(X_train_scaled, y_train)
score = svm.score(X_test_scaled, y_test)
print(f"Scaled test set accuracy {score : .2f}")