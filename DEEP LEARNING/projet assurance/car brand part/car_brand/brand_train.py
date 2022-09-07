import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
import csv
from itertools import zip_longest
import pathlib
data_dir= 'car_brand/datasets'
data_dir=pathlib.Path(data_dir)
# Acura_ILX=list(data_dir.glob('Acura_ILX/*.jpg'))
cars_images_dict={
    'Acura_ILX' : list(data_dir.glob('Acura_ILX/*')),
    'Acura_MDX' : list(data_dir.glob('Acura_MDX/*')),
    'Acura_NSX' : list(data_dir.glob('Acura_NSX/*')),
    'Acura_RDX' : list(data_dir.glob('Acura_RDX/*')),
    'Acura_RLX' : list(data_dir.glob('Acura_RLX/*')),
    'Acura_TLX' : list(data_dir.glob('Acura_TLX/*')),
    'Alfa_Romeo' : list(data_dir.glob('Alfa Romeo/*')),
    'Alfa_Romeo_Giulia' : list(data_dir.glob('Alfa Romeo_Giulia/*')),
    'Alfa_Romeo_Stelvio_20' : list(data_dir.glob('Alfa Romeo_Stelvio_20/*')),
    'Aston_Martin_DB11' : list(data_dir.glob('Aston Martin_DB11/*')),
    'Aston_Martin_DBS' : list(data_dir.glob('Aston Martin_DBS/*')),
    'Aston_Martin_Vanquish' : list(data_dir.glob('Aston Martin_Vanquish/*')),
    'Aston_Martin_Vantage' : list(data_dir.glob('Aston Martin_Vantage/*')),
    'Audi_A3' : list(data_dir.glob('Audi_A3/*')),
    'Audi_A4' : list(data_dir.glob('Audi_A4/*')),
    'Audi_A5' : list(data_dir.glob('Audi_A5/*')),
    'Audi_A6' : list(data_dir.glob('Audi_A6/*')),
    'Audi_A7' : list(data_dir.glob('Audi_A7/*')),
    'Audi_A8' : list(data_dir.glob('Audi_A8/*')),
    'Audi_e-tron' : list(data_dir.glob('Audi_e-tron/*')),
    'Audi_Q3' : list(data_dir.glob('Audi_Q3/*')),
    'Audi_Q5' : list(data_dir.glob('Audi_Q5/*')),
    'Audi_Q7' : list(data_dir.glob('Audi_Q7/*')),
    'Audi_Q8' : list(data_dir.glob('Audi_Q8/*')),
    'Audi_R8' : list(data_dir.glob('Audi_R8/*')),
    'Audi_TT' : list(data_dir.glob('Audi_TT/*')),

}
# print(cars_images_dict['Acura_ILX'])

flowers_labels_dict = {
    'Acura_ILX': 0,
    'Acura_MDX': 1,
    'Acura_NSX': 2,
    'Acura_RDX': 3,
    'Acura_RLX': 4,
    'Acura_TLX': 5,
    'Alfa_Romeo': 6,
    'Alfa_Romeo_Giulia': 7,
    'Alfa_Romeo_Stelvio_20': 8,
    'Aston_Martin_DB11': 9,
    'Aston_Martin_DBS': 10,
    'Aston_Martin_Vanquish': 11,
    'Aston_Martin_Vantage': 12,
    'Audi_A3': 13,
    'Audi_A4': 14,
    'Audi_A5': 15,
    'Audi_A6': 16,
    'Audi_A7': 17,
    'Audi_A8': 18,
    'Audi_e-tron': 19,
    'Audi_Q3': 20,
    'Audi_Q5': 21,
    'Audi_Q7': 22,
    'Audi_Q8': 23,
    'Audi_R8': 24,
    'Audi_TT': 25,


}

x,y=[],[]
brand_name=[]

for car_name,images in cars_images_dict.items():
    for image in images:
        img=cv2.imread(str(image))
        resized_img=cv2.resize(img,(100,100))
        brand_name.append(car_name)
        x.append(resized_img)
        y.append(flowers_labels_dict[car_name])
# brand_name=list(set(brand_name))
# print(brand_name)
brand_name_final=[]
for element in brand_name:
    if element not in brand_name_final:
        brand_name_final.append(element)
file_list=[brand_name_final]
exported=zip_longest(*file_list)
with open("car_brand/brand_name.csv", "w", encoding="utf-8") as file:
    wr=csv.writer(file)
    wr.writerow(["brand"])
    wr.writerows(exported)
x=np.array(x)
y=np.array(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

data_augmentation = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomFlip("horizontal", input_shape=(100, 100, 3)),
  layers.experimental.preprocessing.RandomZoom(0.2),
  layers.experimental.preprocessing.RandomContrast(0.2),
])
x_train_scaled=x_train/255
x_test_scaled=x_test/255
num_classes=26

model = Sequential([
    data_augmentation,
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),  # best 0.2 generalization
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax'),

])

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

hist=model.fit(x_train_scaled,y_train,epochs=100)
model.save('car_brand/carBrand_model.h5',hist)

model.evaluate(x_test_scaled,y_test)
