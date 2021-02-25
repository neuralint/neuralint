import neuraLint
from keras import layers
from keras.models import Model

def _depthwise_conv_block(inputs, pointwise_conv_filters, alpha,
                          depth_multiplier=1, strides=(1, 1), block_id=1):
    channel_axis = 1
    pointwise_conv_filters = int(pointwise_conv_filters * alpha)

    x = layers.ZeroPadding2D((1, 1), name='conv_pad_%d' % block_id)(inputs)
    # if strides == (1, 1):
    #    x = inputs
    # else:
    #    x = layers.ZeroPadding2D(((0, 1), (0, 1)),
    #                             name='conv_pad_%d' % block_id)(inputs)
    x = layers.DepthwiseConv2D((3, 3),
                               padding='valid',
                               # padding='same' if strides == (1, 1) else 'valid',
                               depth_multiplier=depth_multiplier,
                               strides=strides,
                               use_bias=False,
                               name='conv_dw_%d' % block_id)(x)
    x = layers.BatchNormalization(
        axis=channel_axis, name='conv_dw_%d_bn' % block_id)(x)
    x = layers.Activation('relu', name='conv_dw_%d_relu' % block_id)(x)
    x = layers.Conv2D(pointwise_conv_filters, (1, 1),
                      padding='same',
                      use_bias=False,
                      strides=(1, 1),
                      name='conv_pw_%d' % block_id)(x)
    x = layers.BatchNormalization(axis=channel_axis,
                                  name='conv_pw_%d_bn' % block_id)(x)
    return layers.Activation('relu', name='conv_pw_%d_relu' % block_id)(x)


def _conv_block(inputs, filters, alpha, kernel=(3, 3), strides=(1, 1)):
    channel_axis = 1
    filters = int(filters * alpha)
    # x = layers.ZeroPadding2D(padding=(1, 1), name='conv1_pad')(inputs)
    x = layers.ZeroPadding2D(padding=((0, 1), (0, 1)), name='conv1_pad')(inputs)
    x = layers.Conv2D(filters, kernel,
                      padding='valid',
                      use_bias=False,
                      strides=strides,
                      name='conv1')(x)
    x = layers.BatchNormalization(axis=channel_axis, name='conv1_bn')(x)
    return layers.Activation('relu', name='conv1_relu')(x)


img_input = layers.Input(shape=[224, 224, 224])
alpha = 0.5
# x = _conv_block(img_input, 32, alpha=0.5, strides=(1, 1))
# x = Model(img_input, x)
# y= _depthwise_conv_block(img_input, 32, alpha=0.5, strides=(1, 1))
# y = Model(img_input, y)
# x.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics='accuracy')
# y.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics='accuracy')

depth_multiplier = 1
x = _conv_block(img_input, 32, alpha, strides=(2, 2))
x = _depthwise_conv_block(x, 64, alpha, depth_multiplier, block_id=1)
x = _depthwise_conv_block(x, 128, alpha, depth_multiplier,
                          strides=(2, 2), block_id=2)
x = _depthwise_conv_block(x, 128, alpha, depth_multiplier, block_id=3)
x = _depthwise_conv_block(x, 256, alpha, depth_multiplier,
                          strides=(2, 2), block_id=4)
x = _depthwise_conv_block(x, 256, alpha, depth_multiplier, block_id=5)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier,
                          strides=(2, 2), block_id=6)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier, block_id=7)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier, block_id=8)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier, block_id=9)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier, block_id=10)
x = _depthwise_conv_block(x, 512, alpha, depth_multiplier, block_id=11)
x = _depthwise_conv_block(x, 1024, alpha, depth_multiplier,
                          strides=(2, 2), block_id=12)
x = _depthwise_conv_block(x, 1024, alpha, depth_multiplier, block_id=13)

x = Model(img_input, x)
x.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics='accuracy')

print(neuraLint.check(x))