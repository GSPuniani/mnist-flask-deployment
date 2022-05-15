# imports

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K


# Hyperparameters

num_classes = 10
batch_size = 128
epochs = 12


# Image Resolution

img_rows, img_cols = 28, 28

# Loading the data.

(x_train, y_train), (x_test, y_test) = mnist.load_data()

