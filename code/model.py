from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
 
model = Sequential()
model.add(Dense(10, input_shape=(48, 48, 3)))
model.add(Activation('linear'))
