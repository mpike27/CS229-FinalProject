from VideoScraper import VideoScraper
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import matplotlib.pyplot as plt    # for plotting the images
from keras.utils import np_utils
import skimage
from skimage.transform import resize
from sklearn.model_selection import train_test_split


MAPPING_PATH = 'Data/Training/DF/train-milestone.csv'
TEST_SIZE = 0.3
NUM_EPOCHS = 100
def milestoneModel():
    train_x, train_y, test_x, test_y = getData()
    print("Shape of train_x: ", train_x.shape)
    print("Shape of train_y: ", train_y.shape)

    baseline = keras.Sequential()
    baseline.add(layers.Conv3D(2, 3, input_shape=train_x.shape[1:]))
    baseline.add(layers.Dense(1))
    baseline.fit(train_x, train_y)
    preds = baseline.predict(test_x)

def getData():
    data = pd.read_csv(MAPPING_PATH)
    x = []
    for img_path in data.image:
        x.append(plt.imread(img_path))

    x = np.array(x)
    return train_test_split(x, data['class'], test_size=TEST_SIZE)

def getDataTutorial():
    data = pd.read_csv(MAPPING_PATH)
    x = []
    for img_path in data.image:
        x.append(plt.imread(img_path))

    x = np.array(x)

    image = []
    for i in range(0,x.shape[0]):
        a = resize(x[i], preserve_range=True, output_shape=(224,224)).astype(int)      # reshaping to 224*224*2
        image.append(a)
    X = np.array(image)

    from keras.applications.vgg16 import preprocess_input
    X = preprocess_input(X)      # preprocessing the input data
    return train_test_split(X, data['class'], test_size=TEST_SIZE)


def milestoneFromTutorial():
    x_train, x_valid, y_train, y_valid = getDataTutorial()
    base_model = keras.applications.vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))    # include_top=False to remove the top layer
    X_train = base_model.predict(x_train)
    X_valid = base_model.predict(x_valid)
    X_train = X_train.reshape(len(x_train), 7*7*512)
    X_valid = X_valid.reshape(len(x_valid), 7*7*512)      # converting to 1-D

    train = X_train/X_train.max()      # centering the data
    valid = X_valid/X_valid.max()
    model = keras.models.Sequential()
    model.add(keras.layers.InputLayer((7*7*512,)))    # input layer
    model.add(keras.layers.Dense(units=1024, activation='sigmoid')) # hidden layer
    model.add(keras.layers.Dense(1, activation='sigmoid'))    # output layer

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
    model.fit(train, y_train, epochs=NUM_EPOCHS)

    predictions = model.predict(valid)
    np.savetxt(predictions)
    print("Accuracy: ", np.mean(predictions == y_valid))
def main():
    """
    Function: main
    --------------
    This is the driver function for our supervised models
    --------------
    Arguments: None
    --------------
    Return: None
    """
    #x_train, x_valid, y_train, y_valid = getData()
    #milestoneModel()
    milestoneFromTutorial()



if __name__ == "__main__":
    main()
