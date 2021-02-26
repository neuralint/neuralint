rows,cols=x_train.shape[1:]
in_shape=(rows,cols,1)

cnn = Sequential()

cnn.add(Conv2D(64, (5, 50),
padding="same",
activation="relu",data_format="channels_last",
input_shape=in_shape))

cnn.add(MaxPooling2D(pool_size=(2,2),data_format="channels_last"))

cnn.add(Flatten())
cnn.add(Dropout(0.5))

cnn.add(Dense(number_of_classes, activation="softmax"))

cnn.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['accuracy'])

cnn.fit(x_train, y_train,
     batch_size=batch_size,
     epochs=epochs,
     validation_data=(x_test, y_test),
     shuffle=True)