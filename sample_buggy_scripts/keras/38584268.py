#
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D

batch_size = 32
num_classes = 10
epochs = 100

# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#C1: feature maps: 15, kernel size = (7, 7)
#S2: feature maps: 15, field-of-view = (2, 2)
#C3: feature maps: 45, kernel size = (6, 6)
#S4: feature maps: 45, field-of-view = (4, 3)
#C5: feature maps: 250, kernel size = (5, 5)
#F6 (fully connected layer): no. of units = 50


model = Sequential()
model.add(Conv2D(15, (7, 7),
            activation='relu',
            padding='same',
            input_shape=x_train.shape[1:]))
model.add(MaxPooling2D((2,2), padding='same'))
model.add(Conv2D(45, (6, 6),
            activation='relu',
            padding='same'))
model.add(MaxPooling2D((4,3), padding='same'))
model.add(Conv2D(250, (5, 5), 
            activation='relu', 
            padding='same'))
#model.add(Flatten()) Bug is to forget the addition of flatten
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# initiate RMSprop optimizer
opt = keras.optimizers.RMSprop(learning_rate=0.0001, decay=1e-6)

# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_test, y_test),
            shuffle=True)

# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])