#!/usr/bin/env python3
"""Dense block"""
import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """Dense block"""
    init = K.initializers.he_normal()
    activation = K.activations.relu
    for layer in range(layers):
        Batch_Norm1 = K.layers.BatchNormalization(axis=3)(X)
        ReLU1 = K.layers.Activation(activation)(Batch_Norm1)
        C1 = K.layers.Conv2D(filters=(4 * growth_rate),
                             kernel_size=(1, 1),
                             padding='same',
                             kernel_initializer=init)(ReLU1)
        Batch_Norm3 = K.layers.BatchNormalization(axis=3)(C1)
        ReLU3 = K.layers.Activation(activation)(Batch_Norm3)
        C3 = K.layers.Conv2D(filters=growth_rate,
                             kernel_size=(3, 3),
                             padding='same',
                             kernel_initializer=init)(ReLU3)
        X = K.layers.concatenate([X, C3])
        nb_filters += growth_rate
    return X, nb_filters
