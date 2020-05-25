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
        return new_image, example[1]

def build_model(input, scope='lenet', reuse=False, training=True):
    with tf.variable_scope(scope, reuse=reuse):
        conv1 = tf.layers.conv2d(inputs=input,
                                    filters=32,
                                    kernel_size=[5, 5],
                                    padding='same',
                                    activation=tf.nn.relu)
        pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

        conv2 = tf.layers.conv2d(inputs=pool1, filters=64, kernel_size=[5, 5],
                                    padding='same', activation=tf.nn.relu)
        pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

        pool2_flat = tf.layers.flatten(pool2)
        dense = tf.layers.dense(inputs=pool2_flat, units=512, activation=tf.nn.relu)
        dropout = tf.layers.dropout(inputs=dense, rate=0.25, training=training)
        logits = tf.layers.dense(inputs=dropout, units=1, activation=tf.nn.softmax)
        return logits

def train(n_epochs, learning_rate, batch_size):
    X_train, y_train = mnist.load_data()[0]
    y_train = (y_train % 2)
    y_train = y_train.reshape(-1, 1)
    X_test, y_test = mnist.load_data()[1]
    y_test = (y_test % 2)
    y_test = y_test.reshape(-1, 1)
    train_dataset = Dataset(X_train, y_train, batch_size)
    test_dataset = Dataset(X_test, y_test, batch_size)
    X, y = train_dataset.next_batch
    #X_reshaped = tf.reshape(X, [32,28,28,-1])
    y_pred = build_model(X, scope='lenet', reuse=False, training=True)
    #y_pred = tf.nn.softmax(y_logits)
    train_loss = tf.losses.log_loss(y, y_pred)
    train_acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1)), tf.float32))
    optimizer = tf.train.AdamOptimizer(learning_rate)
    train_op = optimizer.minimize(train_loss)
    
    X_test, y_test = test_dataset.next_batch
    y_pred_test = build_model(X_test, scope='lenet', reuse=True, training=False)
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