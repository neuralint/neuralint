from keras.models import Model
from keras.layers import Input, Activation, merge, Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D, AveragePooling2D
from keras.layers.normalization import BatchNormalization
import neuraLint

def _conv_bn_relu(nb_filter, nb_row, nb_col, subsample=(1, 1)):
    def f(input):
        conv = Convolution2D(nb_filter=nb_filter, nb_row=nb_row, nb_col=nb_col, subsample=subsample,
                             init="he_normal", border_mode="same")(input)
        norm = BatchNormalization()(conv)
        return Activation("relu")(norm)

    return f


def _bn_relu_conv(nb_filter, nb_row, nb_col, subsample=(1, 1)):
    def f(input):
        norm = BatchNormalization()(input)
        activation = Activation("relu")(norm)
        return Convolution2D(nb_filter=nb_filter, nb_row=nb_row, nb_col=nb_col, subsample=subsample,
                             init="he_normal", border_mode="same")(activation)

    return f


def _basic_block(nb_filters, init_subsample=(1, 1)):
    def f(input):
        conv1 = _bn_relu_conv(nb_filters, 3, 3, subsample=init_subsample)(input)
        residual = _bn_relu_conv(nb_filters, 3, 3)(conv1)
        return _shortcut(input, residual)

    return f


def _shortcut(input, residual):
    stride_width = input._keras_shape[1] // residual._keras_shape[1]
    stride_height = input._keras_shape[2] // residual._keras_shape[2]
    equal_channels = residual._keras_shape[3] == input._keras_shape[3]
    # debug
    print(stride_width, stride_height, equal_channels)

    shortcut = input
    if stride_width > 1 or stride_height > 1 or not equal_channels:
        shortcut = Convolution2D(nb_filter=residual._keras_shape[3], nb_row=1, nb_col=1,
                                 subsample=(stride_width, stride_height),
                                 init="he_normal", border_mode="valid")(input)

    return merge([shortcut, residual], mode="sum")


def _residual_block(block_function, nb_filters, repetations, is_first_layer=False):
    def f(input):
        for i in range(repetations):
            init_subsample = (1, 1)
            if i == 0 and not is_first_layer:
                init_subsample = (2, 2)
            input = block_function(nb_filters=nb_filters, init_subsample=init_subsample)(input)
        return input

    return f


def resnet(img_channels=3, img_rows=32, img_cols=32, nb_classes=10):
    input = Input(shape=(img_channels, img_rows, img_cols))
    # input = Input(shape=(img_rows, img_cols, img_channels))

    conv1 = _conv_bn_relu(nb_filter=64, nb_row=3, nb_col=3)(input)
    pool1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), border_mode="same")(conv1)

    # Build residual blocks..
    block_fn = _basic_block
    block1 = _residual_block(block_fn, nb_filters=64, repetations=18, is_first_layer=True)(conv1)
    print("finish block1")
    # print("before block1", pool1)
    # block1 = _residual_block(block_fn, nb_filters=64, repetations=18, is_first_layer=True)(pool1)
    # print("finish block1", block1.shape)
    block2 = _residual_block(block_fn, nb_filters=128, repetations=18)(block1)
    print("finish block2")
    block3 = _residual_block(block_fn, nb_filters=256, repetations=18)(block2)
    print("finish block3")

    # Classifier block
    pool2 = AveragePooling2D(pool_size=(8, 8), strides=(1, 1), border_mode="same")(block3)
    flatten1 = Flatten()(pool2)
    dense = Dense(output_dim=nb_classes, init="he_normal", activation="softmax")(flatten1)

    model = Model(input=input, output=dense)
    return model


### AllConvNet
def allconvnet(img_channels=3, img_rows=32, img_cols=32, nb_classes=10):
    input = Input(shape=(img_rows, img_cols, img_channels))
    # dp1 = Dropout(0.2, input_shape=X_train.shape[1:])(input)
    # conv1 = Convolution2D(96, 3, 3, border_mode='same')(dp1)
    conv1 = Convolution2D(96, 3, padding='same')(input)
    relu1 = Activation('relu')(conv1)
    conv2 = Convolution2D(96, 3, padding='same')(relu1)
    relu2 = Activation('relu')(conv2)
    ## stridced conv
    conv3 = Convolution2D(96, 3, strides=(2, 2), padding='valid')(relu2)
    ## add bn1
    bn1 = BatchNormalization()(conv3)
    relu3 = Activation('relu')(bn1)
    conv4 = Convolution2D(192, 3, padding='same')(relu3)
    relu4 = Activation('relu')(conv4)
    conv5 = Convolution2D(192, 3, padding='same')(relu4)
    relu5 = Activation('relu')(conv5)
    ## stridced conv
    conv6 = Convolution2D(192, 3, strides=(2, 2), padding='valid')(relu5)
    ## add bn2
    bn2 = BatchNormalization()(conv6)
    relu6 = Activation('relu')(bn2)
    conv7 = Convolution2D(192, 3, padding='same')(relu6)
    relu7 = Activation('relu')(conv7)
    ## replace fc to 1x1 convolution
    conv8 = Convolution2D(192, 1, padding='valid')(relu7)
    relu8 = Activation('relu')(conv8)
    conv9 = Convolution2D(nb_classes, 1, padding='valid')(relu8)
    relu9 = Activation('relu')(conv9)
    ## global average pooling
    gap = AveragePooling2D(pool_size=(7, 7))(relu9)
    flt = Flatten()(gap)
    sftm = Activation('softmax')(flt)
    model = Model(input, sftm)

    return model

model = allconvnet(3, 32, 32, 10)
# model = resnet(3, 32, 32, 10)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

print(neuraLint.check(model))