from keras.layers.convolutional import Conv2D
from keras.layers.merge import concatenate
from keras.models import Model
from keras.layers import Input, Activation, merge, Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D, AveragePooling2D

import neuraLint

# -*- coding: utf-8 -*-
"""
DenseNet implemented in Keras
This implementation is based on the original paper of Gao Huang, Zhuang Liu, Kilian Q. Weinberger and Laurens van der Maaten.
Besides I took some influences by random implementations, especially of Zhuang Liu's Lua implementation.
# References
- [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
- [DenseNet - Lua implementation](https://github.com/liuzhuang13/DenseNet)
@author: Christopher Masch
"""

input_1 = Input(shape=(100, 100, 1), dtype='float32')
input_2 = Input(shape=(100, 100, 1), dtype='float32')
input_3 = Input(shape=(100, 100, 1), dtype='float32')
input_4 = Input(shape=(100, 100, 1), dtype='float32')

output_1 = Conv2D(32, (3, 3), activation='relu')(input_1)
output_1 = MaxPooling2D(pool_size=(2, 2))(output_1)
output_1 = Conv2D(32, (3, 3), activation='relu')(output_1)
output_1 = MaxPooling2D(pool_size=(2, 2))(output_1)
output_1 = Flatten()(output_1)

output_2 = Conv2D(32, (3, 3), activation='relu')(input_2)
output_2 = MaxPooling2D(pool_size=(2, 2))(output_2)
output_2 = Conv2D(32, (3, 3), activation='relu')(output_2)
output_2 = MaxPooling2D(pool_size=(2, 2))(output_2)
output_2 = Flatten()(output_2)

output_3 = Conv2D(32, (3, 3), activation='relu')(input_3)
output_3 = MaxPooling2D(pool_size=(2, 2))(output_3)
output_3 = Conv2D(32, (3, 3), activation='relu')(output_3)
output_3 = MaxPooling2D(pool_size=(2, 2))(output_3)
output_3 = Flatten()(output_3)

output_4 = Conv2D(32, (3, 3), activation='relu')(input_4)
output_4 = MaxPooling2D(pool_size=(2, 2))(output_4)
output_4 = Conv2D(32, (3, 3), activation='relu')(output_4)
output_4 = MaxPooling2D(pool_size=(2, 2))(output_4)
output_4 = Flatten()(output_4)

inputs = [input_1, input_2, input_3, input_4]
outputs = [output_1, output_2, output_3, output_4]

combine = concatenate(outputs)

output = Dense(64, activation='relu')(combine)
output = Dense(4, activation='sigmoid')(output)

model = Model(inputs=inputs, outputs=[output])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

print(neuraLint.check(model))