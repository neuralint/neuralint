model = Sequential()
model.add(Conv1D(filters=20, kernel_size=4,activation='relu',padding='same',input_shape=(600,1)))
model.add(MaxPooling1D(pool_size = 2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(50, activation='relu', input_dim = 600))
model.add(Dense(1, activation='softmax'))

model.compile(loss="binary_crossentropy", optimizer="nadam", metrics=['accuracy'])

model.fit(np.array(X), np.array(Y), epochs=100, batch_size=8, verbose=1, validation_data=(np.array(X1),np.array(Y1)))