#!/usr/bin/env python3
"""Layer with dropout"""


import tensorflow as tf
"""Layer with dropout"""


def dropout_create_layer(prev, n, activation, keep_prob):
    """Layer with dropout"""
    dropout = tf.layers.Dropout(keep_prob)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    tensor = tf.layers.Dense(units=n, activation=activation,
                             kernel_initializer=init,
                             kernel_regularizer=dropout)
    return tensor(prev)
