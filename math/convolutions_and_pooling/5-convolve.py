#!/usr/bin/env python3
'''adsf'''


import numpy as np
import matplotlib.pyplot as plt

def convolve(images, kernels, padding='same', stride=(1, 1)):
    '''adsf'''
    m, h, w, c = images.shape
    kh, kw, c, nc = kernels.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(np.ceil((sh * (h - 1) + kh - h) / 2))
        pw = int(np.ceil((sw * (w - 1) + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    images_padded = np.pad(images, ((0,0), (ph,ph),(pw,pw), (0,0)), 'constant', constant_values=0)
    oh = int((h + 2 * ph - kh) / sh + 1)
    ow = int((w + 2 * pw - kw) / sw + 1)
    output = np.zeros((m, oh, ow, nc))
    for i in range(m):
        for j in range(oh):
            for k in range(ow):
                for l in range(nc):
                    output[i, j, k, l] = np.sum(images_padded[i,
                        j*sh:j*sh+kh, k*sw:k*sw+kw, :] * kernels[:, :, :, l])
    return output
