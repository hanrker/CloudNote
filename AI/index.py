# def calculate_fee(distance_travelled):
#     return 10 + 2 * distance_travelled

# for x in [1.0,3.0,5.0,9.0,10.0,20.0]:
#     print(calculate_fee(x))


import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt

print(tf.version)

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# print(train_images[0])

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)

plt.show()