import tensorflow as tf
import numpy as np
import os
from tensorflow.keras import layers
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from tensorflow import keras


import pathlib



data_dir = pathlib.Path('F:\\Hands Hands Hands\\side\\')

batch_size = 32
img_height = 90
img_width = 50

train_ds = keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.1,
    subset="training",
    seed=1256,
    color_mode="grayscale",
    image_size=(img_height, img_width),
    batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)


num_classes = 2

data_augmentation = tf.keras.Sequential([

    layers.experimental.preprocessing.RandomRotation(0.1),
    layers.experimental.preprocessing.RandomZoom(0.1),
    layers.experimental.preprocessing.RandomContrast(0.1)

])

model = tf.keras.Sequential([
     #data_augmentation,



    layers.experimental.preprocessing.Rescaling(1. / 255),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),

    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['sparse_categorical_accuracy'])

model.fit(train_ds, epochs=15)




valds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.1  ,
    subset="validation",
    seed=123,
    color_mode="grayscale",
    image_size=(img_height, img_width),
    batch_size=batch_size)





test_loss, test_acc = model.evaluate(valds, verbose=2)
print(class_names)
print("accuracy" + str(test_acc))


print(model.summary())





model.save("TrainedSide.h5")
