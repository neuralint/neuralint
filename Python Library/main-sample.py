# A sample for using NeuraLint as a Python library on the top of TensorFlow/Keras

from keras.layers import Dropout
from keras.models import Sequential
from keras.layers import Dense, Flatten, GaussianNoise, Convolution2D
from tensorflow.keras import regularizers
from keras.optimizers import SGD
from keras.constraints import maxnorm
import neuraLint

model = Sequential()
# model.add(GaussianNoise(0.1, input_shape=(32, 3, 3)))
model.add(GaussianNoise(0.1, input_shape=(3, 32, 32)))
model.add(Convolution2D(32, 3, 3, input_shape=(3, 32, 32), activation='relu', padding='same'))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(l2=1e-4)))
model.add(Dense(1024, activation='relu', kernel_regularizer=maxnorm(3)))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
# model.add(Dense(512, init='glorot_uniform'))
model.add(Dense(512, activation='relu', kernel_regularizer=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))
# Compile model
lrate = 0.01
nb_epoch = 1000
decay = lrate / (nb_epoch)
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
print(neuraLint.check(model))
