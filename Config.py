class Config:
    DATASET_PATH = "/Data/Training/Frames"
    SINGLE_TEST_PATH = "/Data/Testing/Frames"
    RELOAD_DATASET = True
    RELOAD_TESTSET = True
    RELOAD_MODEL = True
    CACHE_PATH = "cache"
    MODEL_PATH = "model" + str(1)
    BATCH_SIZE = 1
    EPOCHS = 1
    # S(t) is the reconstruction score for frame t to t+9
    SEQ_LEN = 10#frames
    PLAY_LEN = 30#seconds
    FPS = 2#frames per second
    FPP = PLAY_LEN * FPS#frames per play
