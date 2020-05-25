model = Sequential()
model.add(Conv1D(input_shape = (10, 4),
                        filters=16,
                        kernel_size=4,
                        padding='same'))
model.add(BatchNormalization())
model.add(LeakyReLU())
model.add(Dropout(0.2))
model.add(Conv1D(filters=8,
                        kernel_size=4,
                        padding='same'))
model.add(BatchNormalization())
model.add(LeakyReLU())
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(64))
model.add(BatchNormalization())
model.add(LeakyReLU())

model.add(Dense(1))
model.add(Activation('softmax'))

reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.9, patience=30, min_lr=0.000001, verbose=0)

model.compile(optimizer='adam', 
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, 
          nb_epoch = 100, 
          batch_size = 128, 
          verbose=0, 
          validation_data=(X_test, y_test),
          callbacks=[reduce_lr],
          shuffle=True)

y_pred = model.predict(X_test)