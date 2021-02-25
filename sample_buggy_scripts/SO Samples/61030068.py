model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(72, 1)))
model.add(MaxPooling1D(2))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(2))
model.add(Dense(64, activation='relu'))
model.add(Dense(28, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(training_features, training_labels, batch_size=32, epochs=3, validation_split=0.1)