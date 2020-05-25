#main file - run this to train the network

import numpy as np
from keras.datasets import cifar10
from datasetFetch import DataFetch
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')
import simplejson
from matplotlib import pyplot
from scipy.misc import toimage
# load data
#(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# create a grid of 3x3 images
#for i in range(0, 9):
#   pyplot.subplot(3,3,1 + i)
#   pyplot.imshow(toimage(X_train[i]))
# show the plot
#pyplot.show()

#init data
CONST_PHOTOS = 400 # number of photos of each type
y_train = []

#train data
data = DataFetch('orange',CONST_PHOTOS)
data1 = data.openPictures()
data = DataFetch('apple', CONST_PHOTOS)
data.removeErrorImages()
data2 = data.openPictures()

#test data
tdata = DataFetch('test-orange',30)
tdata1 = tdata.openPictures()
tdata = DataFetch('test-apple',30)
tdata2 = tdata.openPictures()

#add togheter data
X_train = data.connectData(data1,data2,'train')
y_train = data.getYtrain('train')
X_test = tdata.connectData(tdata1,tdata2,'test')
y_test = tdata.getYtrain('test')

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# normalize inputs from 0-255 to 0.0-1.0
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0

#one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = 2#y_train.shape[1] #number of categories


# Create the model
model = Sequential()
model.add(Conv2D(224, (11, 11), activation='relu', padding='same', input_shape=(224, 224, 3)))
model.add(Dropout(0.2))
model.add(Conv2D(55, (5, 5), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_last"))
model.add(Conv2D(13, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.5))
model.add(Conv2D(13, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_last"))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

# Compile model
epochs = 100
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
#print(model.summary())
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=10)

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

#and then we save
# serialize model to JSON
model_json = model.to_json()
with open("Data/model.json", "w") as json_file:
    json_file.write(simplejson.dumps(simplejson.loads(model_json), indent=4))
# serialize weights to HDF5
model.save_weights("Data/model.h5")
print("Saved model to disk")