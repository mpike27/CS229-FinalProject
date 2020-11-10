import numpy as np


train_path = 'Data/Training/CSV/'

def getData(path):
    return np.array([np.load(file) for file in os.listdir(path)])


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

if __name__ == "__main__":
    main()
