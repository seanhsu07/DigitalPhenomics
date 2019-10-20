# preallocation

import os
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


base_dir = "./test_img"
train_dir = os.path.join(base_dir, 'train')
# validation_dir = os.path.join(base_dir, 'validation')

# Model Parameters
BATCH_SIZE = 500
IMG_WIDTH = 800
IMG_HEIGHT = 962

# Data Augmentation
# This function will plot images in the form of a grid with 1 row and 5 columns where images are placed in each column.
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()

# horizontal image flip

# image_gen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
# train_data_gen = image_gen.flow_from_directory(batch_size=BATCH_SIZE,
#                                                 directory=train_dir,
#                                                 shuffle=True,
#                                                 target_size=(IMG_SHAPE, IMG_SHAPE))
#
# # # plot augmented_images
# # augmented_images = [train_data_gen[0][0][0] for i in range(5)]
# # plotImages(augmented_images)
#
# # image rotation
# image_gen = ImageDataGenerator(rescale=1./255, rotation_range=45)
# train_data_gen = image_gen.flow_from_directory(batch_size=BATCH_SIZE,
#                                                 directory=train_dir,
#                                                 shuffle=True,
#                                                 target_size=(IMG_SHAPE, IMG_SHAPE))
#
# random zoom
# image_gen = ImageDataGenerator(rescale=1./255, zoom_range=0.5)
# train_data_gen = image_gen.flow_from_directory(batch_size=BATCH_SIZE,
#                                                 directory=base_dir,
#                                                 shuffle=True,
#                                                 target_size=(IMG_WIDTH, IMG_HEIGHT),
#                                                 save_to_dir = './aug_img_val')

# all in one modification
image_gen_train = ImageDataGenerator(rescale=1./255,
                                      rotation_range=40,
                                      width_shift_range=0.2,
                                      height_shift_range=0.2,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True,
                                      fill_mode='nearest')

train_data_gen = image_gen_train.flow_from_directory(batch_size=BATCH_SIZE,
                                                     directory=base_dir,
                                                     shuffle=True,
                                                     target_size=(IMG_WIDTH,IMG_HEIGHT),
                                                     class_mode='binary',
                                                     save_to_dir = 'D:\\aug_img')

image_gen_val = ImageDataGenerator(rescale=1./255)
for i in range(4):
    next(train_data_gen)
    pass
