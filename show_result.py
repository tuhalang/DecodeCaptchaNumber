from cut_image import find_location, add_matrix

import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers import regression
from tflearn.data_utils import to_categorical

import cv2
import numpy as np

BATCH_SIZE = 32
IMG_SIZE = 75
N_CLASSES = 9
LR = 0.001
N_EPOCHS = 50


tf.reset_default_graph()

network = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1]) #1

network = conv_2d(network, 32, 3, activation='relu') #2
network = max_pool_2d(network, 2) #3

network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)

network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)

network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)

network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)

network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)

network = fully_connected(network, 1024, activation='relu') #4
network = dropout(network, 0.8) #5

network = fully_connected(network, N_CLASSES, activation='softmax')#6
network = regression(network)

model = tflearn.DNN(network) #7


model.load('mymodel.tflearn')

url_image = "images/4623.png"

delta = 3
location = find_location(url_image)
start = location[1]+delta
diff = int((location[3] - 2*delta)/5)

image = cv2.imread(url_image,0)
rs = ""
for i in range(5):
    sub = image[location[2]:location[2]+location[4],start:start+diff]
    mark = np.zeros((75,75))
    start = start+diff
    sub_img = add_matrix(sub,mark)
    sub_img = sub_img.reshape(-1,75,75,1)
    result = model.predict(sub_img)
    result = np.argmax(result, axis=-1)
    rs = rs + str(result[0])
print(rs)