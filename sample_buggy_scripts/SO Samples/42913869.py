import neuraLint

from keras.layers.core import Dense
from keras import Sequential

model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
print(neuraLint.check(model))