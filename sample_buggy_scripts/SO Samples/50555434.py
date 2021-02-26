import neuraLint

from keras.layers.core import Dense
from keras import Sequential

# X = np.loadtxt("compiledFeatures.csv", delimiter=",")
# Y = np.loadtxt("naive_compiledDate.csv", delimiter=",")

# create model
model = Sequential()
model.add(Dense(20, input_dim=28, kernel_initializer='normal', activation='relu'))
model.add(Dense(15, kernel_initializer='normal', activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='sigmoid'))

# Compile model
model.compile(optimizer="adam", loss='mae')
# Fit the model
# model.fit(X, Y, epochs=2000, verbose=2, validation_split=0.15)
# calculate predictions
# predictions = model.predict(X)

print(neuraLint.check(model))