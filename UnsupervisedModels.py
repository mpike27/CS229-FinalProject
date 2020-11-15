import numpy as np
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Conv3D, Conv2DTranspose, Conv3DTranspose, Flatten, Input
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
import os

train_path = 'Data/Training/CSV/'
test_path = 'Data/Testing/CSV/'

def getData(path):
    data = []
    for file in os.listdir(path):
        if file[-3:] == "npy":
            data.append(np.load(path + file, allow_pickle=True))
    return collapseData(data)

def collapseData(data):
    new_data = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            new_data.append(data[i][j])
    return np.array(new_data)

def experiment1(train_data, val_data, test_data):
    train_flat = np.array([np.ravel(train_data[i]) for i in range(train_data.shape[0])])
    val_flat = np.array([np.ravel(val_data[i]) for i in range(val_data.shape[0])])
    test_flat = np.array([np.ravel(test_data[i]) for i in range(test_data.shape[0])])
    model = Sequential()
    model.add(Dense(int(train_flat.shape[1] / 2), activation="relu", input_shape=(train_flat.shape[1],)))
    model.add(Dense(train_flat.shape[1]))
    model.compile(optimizer="adam", loss="mse")
    model.summary()
    es = EarlyStopping(min_delta=1, verbose=1, patience=3)
    model.fit(train_flat, train_flat, validation_data=(val_flat, val_flat), epochs=100, callbacks=[es])
    preds = model.predict(test_flat)
    print(np.linalg.norm(preds - test_flat) / np.linalg.norm(test_flat))

def experiment2(train_data, val_data, test_data):
    filters = 64
    kernel_size = 3
    input = Input(shape=(train_data.shape[1], train_data.shape[2], train_data.shape[3], 1))
    conv = Conv3D(filters, kernel_size, activation="relu")(input)
    bottle = Conv3D(int(filters / 2), kernel_size, activation="relu")(conv)
    bottleT = Conv3DTranspose(filters, kernel_size, activation="relu")(bottle)
    convT = Conv3DTranspose(1, kernel_size, activation="relu")(bottleT)
    model = Model(inputs=input, outputs=convT)

    model.compile(optimizer="adam", loss="mse")
    model.summary()
    es = EarlyStopping(min_delta=1, verbose=1, patience=3)
    model.fit(train_data, train_data, validation_data=(val_data, val_data), epochs=100, callbacks=[es])
    preds = model.predict(test_data)
    preds = preds.reshape(preds.shape[0], preds.shape[1], preds.shape[2], preds.shape[3])
    print(np.linalg.norm(preds - test_data) / np.linalg.norm(test_data))


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
    train_data = getData(train_path)
    train_data, _, val_data, _ = train_test_split(train_data, train_data, test_size=0.1)
    print(f"Train_data shape is {train_data.shape}")
    test_data = getData(test_path)
    print(f"Test_data shape is {test_data.shape}")
    experiment1(train_data, val_data, test_data)
    experiment2(train_data, val_data, test_data)


if __name__ == "__main__":
    main()
