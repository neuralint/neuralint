from k.layers.convolutional import *
from k.layers import *
from k.layers.core import *

model = Sequential()
model.add(Conv1D(32,2, input_shape = (32, 1)))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Dense(32))
model.add(Activation('sigmoid'))

model.compile(loss = 'binary_crossentropy',
              optimizer = 'rmsprop',
              metrics=['accuracy'])
              
model.fit(inputData,labelData)