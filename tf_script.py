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
