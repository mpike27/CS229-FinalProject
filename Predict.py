import numpy as np
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, Conv3D, Conv2DTranspose, Conv3DTranspose, Flatten, Input
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
import os

train_path = 'Data/Training/CSV/'
test_path = 'Data/Testing/CSV/'
test_y_path = "String"
model_path1 = "String"
model_path2 = "String"
model_pat3 = "String"

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

def computeProbs(rec, x, y):
    C = np.array([np.linalg.norm(rec[i] - x[i]) for i in rec.shape[0]])
    Z = (C - np.mean(C)) / np.std(C)
    Y_hat = np.ones(Z.shape[0]) - (1/(1 + np.exp(-Z)) )
    return Y_hat


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
    test_data = getData(test_path)
    test_y = getData(test_y_path)
    model1 = load_model(model_path1)
    model2 = load_model(model_path2)
    model3 = load_model(model_path3)
    rec1 = model1.predict(test_data)
    rec2 = model2.predict(test_data)
    rec3 = model3.predict(test_data)
    preds1 = computeProbs(rec1, test_data, test_y)
    preds2 = computeProbs(rec2, test_data, test_y)
    preds3 = computeProbs(rec3, test_data, test_y)
    


if __name__ == "__main__":
    main()
