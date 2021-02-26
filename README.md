# NeuraLint

`NeuraLint` is a toolset for verifying deep learning models using meta-modeling and graph transformations.
This toolset performs verification of deep learning models that are specified using graph transformations by the Groove toolset.
A deep learning program as input must be written using `Tensorflow` or `Keras`. First, the program is parsed to extract relevant information according to the meta-model. The model of the program is a graph that conforms to the type graph (meta-model). Then, the graph is verified by `Groove` as a model checker. The output graph of Groove is used to extract relevant Information for the final report.

`groove-x_x_x-bin` and `DNN-metamodel.gps` folders are the Groove toolset and type graph respectively which are needed for running `NeuraLint`.

`Keras_graphs` and `TF_graphs` folders are also used for intermediate calculation and required to run `NeuraLint`.

The tool is written in `Python` and it can be easily run in the command line. To use the toolset, please enter following options with running command:

```
$ python endToEnd.py [name of deep learning programs (.py)] [input size] [output size] [parser type] [name of the output file]
```

- `[name of deep learning programs (.py)]` should be entered with `.py`

- `[input size]` and `[output size]` should be entered as table like `[x1, x2, x3, ...]`

- `[parser type]` should be `tf` or `keras`

- `[name of the output file]` should be entered without file type


## Examples
### TensorFlow Example

The following code is a sample `TensorFlow` script:
```python
import tensorflow as tf
import click
import numpy as np
from tensorflow.keras.datasets import mnist

class Dataset:

    def __init__(self, X, y, batch_size):
        dset = tf.data.Dataset.from_tensor_slices((X, y))
        dset = dset.map(self.preprocess_example)
        dset = dset.shuffle(10000)
        dset = dset.batch(batch_size)
        self.dset = dset 
        self.iterator = self.dset.make_initializable_iterator()
        self.next_batch = self.iterator.get_next()

    def init(self, sess):
        sess.run(self.iterator.initializer)

    def preprocess_example(self, *example):
        new_image = tf.image.convert_image_dtype(tf.reshape(example[0], [28, 28, 1]), tf.float32)
        new_label = tf.cast(tf.one_hot(example[1], 10), tf.float32)
        return new_image, new_label

def build_model(input, scope='lenet', reuse=False, training=True):
    with tf.variable_scope(scope, reuse=reuse):
        conv1 = tf.layers.conv2d(inputs=input,
                                    filters=32,
                                    kernel_size=[15, 15],
                                    padding='valid',
                                    activation=tf.nn.relu)
        reg_conv1 = tf.layers.dropout(inputs=conv1, rate=0.35, training=training)
        conv1_norm = tf.layers.batch_normalization(reg_conv1, training=training)
        pool1 = tf.layers.max_pooling2d(inputs=conv1_norm, pool_size=[4, 4], strides=2)

        conv2 = tf.layers.conv2d(inputs=pool1, filters=64, kernel_size=[7, 7],
                                    padding='valid', activation=tf.nn.relu)
        reg_conv2 = tf.layers.dropout(inputs=conv2, rate=0.3, training=training)
        conv2_norm = tf.layers.batch_normalization(reg_conv2, training=training)
        pool2 = tf.layers.max_pooling2d(inputs=conv2_norm, pool_size=[4, 4], strides=2)

        pool2_flat = tf.layers.flatten(pool2)
        dense = tf.layers.dense(inputs=pool2_flat, units=512, activation=tf.nn.relu)
        dense_reg = tf.layers.dropout(inputs=dense, rate=0.25, training=training)
        dense_norm = tf.layers.batch_normalization(dense_reg, training=training)
        logits = tf.layers.dense(inputs=dense_norm, units=10, activation=None)
        return logits

def train(n_epochs, learning_rate, batch_size):
    X_train, y_train = mnist.load_data()[0]
    X_test, y_test = mnist.load_data()[1]
    train_dataset = Dataset(X_train, y_train, batch_size)
    test_dataset = Dataset(X_test, y_test, batch_size)
    X, y = train_dataset.next_batch
    y_pred = build_model(X, scope='lenet', reuse=False, training=True)
    train_loss = tf.losses.softmax_cross_entropy(y, y_pred)
    train_acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1)), tf.float32))
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    with tf.control_dependencies(update_ops):
        optimizer = tf.train.AdamOptimizer(learning_rate)
        train_op = optimizer.minimize(train_loss)

    X_test, y_test = test_dataset.next_batch
    y_pred_test = build_model(X_test, reuse=True, training=False)
    test_loss = tf.losses.softmax_cross_entropy(y_test, y_pred_test)
    test_acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y_test, 1),tf.argmax(y_pred_test, 1)), tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(n_epochs):
            train_dataset.init(sess)
            epoch_errs = []
            epoch_accs = []
            try:
                while True:
                    _, err, acc = sess.run([train_op, train_loss, train_acc])
                    epoch_errs.append(err)
                    epoch_accs.append(acc)
            except tf.errors.OutOfRangeError:
                print(f"Epoch {epoch}:")
                print(f"  - Train err: {np.mean(epoch_errs)}")
                print(f"  - Train acc: {np.mean(epoch_accs)}")
                test_dataset.init(sess)
                test_errs = []
                test_accs = []
                try:
                    while True:
                        err, acc = sess.run([test_loss, test_acc])
                        test_errs.append(err)
                        test_accs.append(acc)
                except tf.errors.OutOfRangeError:
                    epoch_test_err, epoch_test_acc = np.mean(test_errs), np.mean(test_accs) 
                print(f"  - Test err: {epoch_test_err}")
                print(f"  - Test acc: {epoch_test_acc}")

@click.command()
@click.option('--n-epochs', type=int, default=5)
@click.option('--lr', type=float, default=3e-4)
@click.option('--batch-size', type=int, default=32)
def main(n_epochs, lr, batch_size):
    train(n_epochs, lr, batch_size)

if __name__ == '__main__':
    main()
```

User can use the following command to parse above-mentioned code using `NeuraLint`: 

```
$ python endToEnd.py tf_script.py [32,28,28,1] [32,10] tf result
```

The result of `NeuraLint` is

```
tf_script.py

Layer 1 ==> A learning layer should no longer include a bias when it is followed by batchnorm., The local window size for spatial filtering should generally increase or stay the same throughout the convolutional layers.
Layer 3 ==> Batchnorm layer should be before the dropout., Dropout layer must be placed after the pooling layer to be more effective.
Layer 6 ==> A learning layer should no longer include a bias when it is followed by batchnorm., A processing layer should receive sufficient-sized feature space to perform its spatial filtering or pooling.
Layer 8 ==> Batchnorm layer should be before the dropout., Dropout layer must be placed after the pooling layer to be more effective.
Layer 10 ==> A processing layer should receive sufficient-sized feature space to perform its spatial filtering or pooling.
Layer 12 ==> A learning layer should no longer include a bias when it is followed by batchnorm.
Layer 14 ==> Batchnorm layer should be before the dropout.
```
### Keras Example
The following code is a sample `Keras` script:

```python
from k.layers.convolutional import *
from k.layers import *
from k.layers.core import *

model = Sequential()
model.add(Conv1D(32,2, input_shape = (32, 1)))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Conv1D(32,2))
model.add(Activation('relu'))

model.add(Dense(32))
model.add(Activation('sigmoid'))

model.compile(loss = 'binary_crossentropy',
              optimizer = 'rmsprop',
              metrics=['accuracy'])
              
model.fit(inputData,labelData)
```

Again, user can use the following command to parse mentioned code using `NeuraLint`. 

```
$ python endToEnd.py keras_script.py [32,32,1] [32,1] keras result
```

The result of `NeuraLint` is:

```
keras_script.py

Learner ==> The loss should be correctly defined and connected to the layer in accordance with its input conditions (i.e.shape and type)-post_activation
Layer 7 ==> A processing layer that operates on a N-dimensional tensors, should receive a valid input tensor with exactly N-dimensional shape(missing flatten ).
```

### Python library
Moreover, it can be called inside a DL program as a Python library on the top of TensorFlow/Keras. The developer can import `NeuraLint` as a Python library and simply call it in his own code by feeding the DL model and receiving the analysis report. For example:
```
import neuraLint
...

report = neuraLint.check(model)
print(report)
```
This library is in the `Python Library` folder. Please note that you should place `groove-x_x_x-bin` and `DNN-metamodel.gps` folders in its root prior to using it. An example is provided in `main-sample.py`.
