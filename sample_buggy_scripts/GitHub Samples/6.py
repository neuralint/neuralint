import keras
import neuraLint

BATCH_SIZE = 256
ITERATIONS = 60000 // BATCH_SIZE
EPOCHS = 3
LEARNING_RATE = 3e-3
IN_DIM = 28
KERNEL = 5
STRIDE = 1
IN_CHANNELS = 1
HIDDEN_C1 = 20
HIDDEN_C2 = 50
HIDDEN_FC1 = 256
HIDDEN_FC2 = 100
OUT_N = 10
HIDDEN_CHANNELS = 16

model = keras.Sequential()
model.add(
    keras.layers.Conv2D(
        HIDDEN_CHANNELS,
        (KERNEL, KERNEL),
        batch_input_shape=(
            BATCH_SIZE,
            IN_DIM,
            IN_DIM,
            IN_CHANNELS,
        ),
    )
)
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.AveragePooling2D())
model.add(keras.layers.Conv2D(HIDDEN_CHANNELS, (KERNEL, KERNEL)))
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.AveragePooling2D())
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(HIDDEN_FC2))
model.add(keras.layers.Activation("relu"))
model.add(keras.layers.Dense(OUT_N))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
print(neuraLint.check(model))