# -*- coding: utf-8 -*-
"""Sub3_LSTM_interpolation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KJbkWdfrsxYzEWjXv4HBHkhiXeyI42cY

### Stock Market Prediction And Forecasting Using  LSTM Jupyter notebook

## Stock Prediction :
Take stock price of any company you
want and predicts its price by using LSTM.
Use only Jupyter notebook code.
"""

# =============================================================================
# Importing the libraries
# =============================================================================
import numpy as np # Data Handling
import matplotlib.pyplot as plt # Data Visualization
import pandas as pd # # Data Handling
import os # Working Directory
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # Transformation of Categorical columns into Numerical Values
from sklearn.compose import ColumnTransformer # Transformation same as level encoding and one hotencoding
from sklearn.model_selection import train_test_split # Splitting Data into Train & Test
from sklearn.preprocessing import StandardScaler # Neural Networks --> generally standarize the data
from sklearn.metrics import confusion_matrix # Model Evaluation
from sklearn.metrics import classification_report # Model Evaluation
import keras # Deep Learning Framework
from keras.models import Sequential # Adding layers in the Neural Network
from keras.layers import Dense # Adding layers in the Neural Network

# =============================================================================
# Importing the dataset
# =============================================================================
df = pd.read_csv('BigData/volumes.csv')

# =============================================================================
# EDA of the Data
# =============================================================================
df.head()

df.tail()

#Shape
df.shape

#Inforrmation about the data
df.info()

#Checking missing values across features
df.isnull().sum()

# Check correlation

# Correlation with columns '1' '15'
corr_0 = df['vol_btc'].corr(df["vol_ada"])
corr_1 = df['vol_btc'].corr(df["vol_avax"])
corr_2 = df['vol_btc'].corr(df['vol_bnb'])
corr_3 = df['vol_btc'].corr(df['vol_dot'])
corr_4 = df['vol_btc'].corr(df['vol_eth'])
corr_5 = df['vol_btc'].corr(df['vol_link'])
corr_6 = df['vol_btc'].corr(df['vol_ltc'])
corr_7 = df['vol_btc'].corr(df["vol_shib"])
corr_8 = df['vol_btc'].corr(df["vol_sol"])
corr_9 = df['vol_btc'].corr(df["vol_wbtc"])
corr_10= df['vol_btc'].corr(df["vol_usdc"])
corr_11= df['vol_btc'].corr(df["vol_usdt"])
corr_12= df['vol_btc'].corr(df["vol_xrp"])
corr_13= df['vol_btc'].corr(df["vol_steth"])



print('Correlation 0:', corr_0)
print('Correlation 1:', corr_1)
print('Correlation 2:', corr_2)
print('Correlation 3:', corr_3)
print('Correlation 4:', corr_4)
print('Correlation 5:', corr_5)
print('Correlation 6:', corr_6)
print('Correlation 7:', corr_7)
print('Correlation 8:', corr_8)
print('Correlation 9:', corr_9)
print('Correlation 10:', corr_10)
print('Correlation 11:', corr_11)
print('Correlation 12:', corr_12)
print('Correlation 13:', corr_13)

import seaborn as sns
import matplotlib.pyplot as plt


# Visualize the  data using seaborn
sns.set(rc={'figure.figsize':(50,7)})

sns.lineplot(x=df['date'], y=df['vol_usdt'])
sns.lineplot(x=df['date'], y=df['vol_eth'])
sns.lineplot(x=df['date'], y=df['vol_bnb'])


plt.legend(['btc', 'eth', 'usdt'])

# =============================================================================
# Data Processing
# =============================================================================

df1 = df[['date', 'vol_btc', 'vol_eth', 'vol_usdt']]

df1

df1.info()

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
df1=scaler.fit_transform(np.array(df1[['vol_btc', 'vol_eth', 'vol_usdt']]).reshape(-1,1))

print(df1)

##splitting dataset into train and test split
training_size=int(len(df1)*0.8)
test_size=len(df1)-training_size
train_data,test_data=df1[0:training_size,:],df1[training_size:len(df1),:1]

training_size,test_size

train_data

import numpy
# convert an array of values into a dataset matrix
def create_dataset(dataset, time_step=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-time_step-1):
		a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100
		dataX.append(a)
		dataY.append(dataset[i + time_step, 0])
	return numpy.array(dataX), numpy.array(dataY)

# reshape into X=t,t+1,t+2,t+3 and Y=t+4
time_step = 100
X_train, y_train = create_dataset(train_data, time_step)
X_test, ytest = create_dataset(test_data, time_step)

print(X_train.shape), print(y_train.shape)

print(X_test.shape), print(ytest.shape)

# reshape input to be [samples, time steps, features] which is required for LSTM
X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)

### Create the Stacked LSTM model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

'''
model=Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(100,1)))
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')
'''

model=Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(1219,3)))
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')

model.summary()



model.fit(X_train,y_train,validation_data=(X_test,ytest),epochs=50,batch_size=64,verbose=1)

### Lets Do the prediction and check performance metrics
train_predict=model.predict(X_train)
test_predict=model.predict(X_test)

##Transformback to original form
train_predict=scaler.inverse_transform(train_predict)
test_predict=scaler.inverse_transform(test_predict)

### Calculate MAE performance metrics
import math
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import f1_score

math.sqrt(mean_absolute_error(y_train,train_predict))
f1_score(y_train, train_predict, average='binary')

### Test Data MAE
math.sqrt(mean_absolute_error(ytest,test_predict))

### Plotting
# shift train predictions for plotting
look_back=5
trainPredictPlot = numpy.empty_like(df1)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(df1)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(df1)-1, :] = test_predict
# plot baseline and predictions
plt.plot(scaler.inverse_transform(df1))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

len(test_data)

x_input=test_data[341:].reshape(1,-1)
x_input.shape

temp_input=list(x_input)
temp_input=temp_input[0].tolist()

temp_input

day_new=np.arange(1,101)
day_pred=np.arange(101,131)

import matplotlib.pyplot as plt

len(df1)

df3=df1.tolist()
df3.extend(df3)
plt.plot(df3[1200:])

df3=scaler.inverse_transform(df3).tolist()

plt.plot(df3)

df3[-120:]
