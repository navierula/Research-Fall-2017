# -*- coding: utf-8 -*-
"""
@navrajnarula
http://thelillysblog.com/2017/08/18/machine-learning-k-fold-validation/
"""
import nltk # needed for Naive-Bayes
import numpy as np
from sklearn.model_selection import KFold


from pandas import read_csv


data = read_csv('data/130N_Cycles_1-47.csv')

# data is an array with our already pre-processed dataset examples
kf = KFold(n_splits=3)
sum = 0
for train, test in kf.split(data):
    train_data = np.array(data)[train]
    test_data = np.array(data)[test]
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    sum += nltk.classify.accuracy(classifier, test_data)
average = sum/3

