model = Sequential()
model.add(Conv1D(100,700,activation='relu',input_shape=(18000,1))) #kernel_size is 700 because 18000 rows = 60 seconds so 700 rows = ~2.33 seconds and there is two heart beat peak in every 2 second for ecg signal.
model.add(Conv1D(50,700))
model.add(Dropout(0.5))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling1D(4))
model.add(Flatten())
model.add(Dense(6,activation='softmax'))

adam = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(train_x,train_y,epochs = 50, batch_size = 32, validation_split=0.33, shuffle=False)