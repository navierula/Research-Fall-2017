# -*- coding: utf-8 -*-
"""
@navrajnarula
https://machinelearningmastery.com/make-predictions-time-series-forecasting-python/
"""

# load libraries
import pandas
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import numpy

# read in data file
xl = pandas.ExcelFile("data/130N_Cycles_1-47.xlsx")
series = xl.parse("Specimen_RawData_1")

# print first five lines of data
print(series.head())

# plot entire dataset
series.plot()
pyplot.show()

# create a difference transform of the dataset
def difference(dataset):
	diff = list()
	for i in range(1, len(dataset)):
		value = dataset[i] - dataset[i - 1]
		diff.append(value)
	return numpy.array(diff)
 
# Make a prediction give regression coefficients and lag obs
def predict(coef, history):
	yhat = coef[0]
	for i in range(1, len(coef)):
		yhat += coef[i] * history[-i]
	return yhat
 
series = Series.from_csv('data/130N_Cycles_1-47.csv', header=0)
# split dataset
X = difference(series.values)
size = int(len(X) * 0.70)
train, test = X[0:size], X[size:]

# train autoregression
model = AR(train) #values above 9 might be better
model_fit = model.fit(maxlag=30, disp=False)
window = model_fit.k_ar
coef = model_fit.params

# walk forward over time steps in test
history = [train[i] for i in range(len(train))]
predictions = list()
for t in range(len(test)):
	yhat = predict(coef, history)
	obs = test[t]
	predictions.append(yhat)
	history.append(obs)
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test[:50])
pyplot.plot(predictions[:50], color='green')

pyplot.show()

