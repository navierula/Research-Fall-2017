# -*- coding: utf-8 -*-
"""
@navrajnarula
https://machinelearningmastery.com/persistence-time-series-forecasting-with-python/
"""

import pandas
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas import DataFrame
 

#def parser(x):
#	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('data/130N_Cycles_1-47.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
series.plot()
pyplot.show()


# Create lagged dataset
values = DataFrame(series.values)
dataframe = pandas.concat([values.shift(1), values], axis=1)
dataframe.columns = ['t-1', 't+1']
print(dataframe.head(5))



# split into train and test sets
X = dataframe.values
train_size = int(len(X) * 0.66)
train, test = X[1:train_size], X[train_size:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

# persistence model
def model_persistence(x):
	return x

print(test_X)
# walk-forward validation
predictions = list()
for x in test_X:
	yhat = model_persistence(x)
	predictions.append(yhat)
#test_score = mean_squared_error(test_y, predictions)
#print('Test MSE: %.3f' % test_score)

# plot predictions and expected results
pyplot.plot(train_y)
pyplot.plot([None for i in train_y] + [x for x in test_y])
pyplot.plot([None for i in train_y] + [x for x in predictions])
print(len)
pyplot.show()

print(len(train_y), len(test_y))
print(len(train_y), len(predictions))
print(len(train_y)+len(predictions))

predictions = predictions

import matplotlib.pyplot as plt

#lines = plt.plot(predictions)
#print(lines)






