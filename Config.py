
TRAINSET_PATH = "../../max/max-git/Data/Training/CSV"
TESTSET_PATH = "Data/Testing/Frames/WolvesManUtd031619"
SINGLE_TEST_PATH = "Data/Training/Frames/ManUtdTot100520H/clip10"
RELOAD_DATASET = True
RELOAD_TESTSET = True
RELOAD_MODEL = True
CACHE_PATH = "cache"
MODEL_PATH = 'Saved_Models'#"model" + str(1)
BATCH_SIZE = 4
EPOCHS = 3
# S(t) is the reconstruction score for frame t to t+9
SEQ_LEN = 10#frames
PLAY_LEN = 30#seconds
FPS = 2#frames per second
FPP = PLAY_LEN * FPS#frames per play
