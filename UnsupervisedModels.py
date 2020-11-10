import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
import os

train_path = 'Data/Training/CSV/'
test_path = 'Data/Testing/CSV/'

def getData(path):
    data = []
    for file in os.listdir(path):
        if file[-3:]== "npy":
            data.append(np.load(path + file, allow_pickle=True))
    return collapseData(np.array(data))
    # return np.array([np.load(file, allow_pickle=True) for file in os.listdir(path)])

def collapseData(data):
    new_data = []
    for i in range(data.shape[0]):
        for j in range(data[i].shape[0]):
            new_data.append(data[i][j])
    return np.array(new_data)

def experiment1(train_data, test_data):
    train_flat = np.array([np.ravel(train_data[i]) for i in range(train_data.shape[0])])
    test_flat = np.array([np.ravel(test_data[i]) for i in range(test_data.shape[0])])
    model = Sequential()
    model.add(Dense(int(train_flat.shape[1] / 2), input_shape=train_flat.shape))
    model.add(Dense(train_flat.shape[1]))
    model.compile(optimizer="adam", loss="mse")
    checkpoint = ModelCheckpoint( # used for training loss
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    model_callbacks = [checkpoint]

    model.fit(train_flat, train_flat, epochs=20, callbacks=model_callbacks)
    preds = model.predict(test_flat)
    print(preds - test_flat)



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
    print(train_data.shape)
    test_data = getData(test_path)
    print(test_data.shape)
    experiment1(train_data, test_data)


if __name__ == "__main__":
    main()
