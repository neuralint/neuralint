num_classes = 10

model.add(Conv2D(32, (5, 5),
                  padding='same',
                  data_format='channels_last',
                  input_shape=input_shape))

model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (5, 5)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (5, 5)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(64, (5, 5)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.25))

model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(loss="categorical_crossentropy", optimizer='adam',  metrics=['accuracy'])    
model.summary()
model.fit(X, y, nb_epoch=20)