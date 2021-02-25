from keras import Sequential
from keras.applications import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.layers import Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import neuraLint

IMG_WIDTH, IMG_HEIGHT = 224, 224
TRAIN_DATA_DIR = 'C:\\Private\\BMW\\car_photos_224x224\\train'
VALIDATION_DATA_DIR = 'C:\\Private\\BMW\\car_photos_224x224\\validation'
TEST_DATA_DIR = 'C:\\Private\\BMW\\car_photos_224x224\\test'
BATCH_SIZE = 8
EPOCHS = 100

def prepare_data():
    train_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=True)
    validation_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    validation_generator = validation_datagen.flow_from_directory(
        VALIDATION_DATA_DIR,
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=True)
    # test_datagen = ImageDataGenerator(rescale=1./255)
    # test_generator = test_datagen.flow_from_directory(
    #     TEST_DATA_DIR,
    #     target_size=(IMG_WIDTH, IMG_HEIGHT),
    #     batch_size=BATCH_SIZE,
    #     class_mode='categorical',
    #     shuffle=True)
    # return train_generator, validation_generator, test_generator
    return train_generator, validation_generator


def show_history(history):
    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


def training():
    # train_generator, validation_generator = prepare_data()
    # train_generator, validation_generator, test_generator = prepare_data()
    conv_network = ResNet50(include_top=False,
                            weights='imagenet',
                            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))
    for layer in conv_network.layers[:-3]:
        layer.trainable = False

    model = Sequential()
    model.add(conv_network)
    # model.add(AveragePooling2D((7, 7), name='avg_pool'))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    # model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=0.001),
                  metrics=['accuracy'])

    print(neuraLint.check(model))
    # neuraLint.check(model)

training()