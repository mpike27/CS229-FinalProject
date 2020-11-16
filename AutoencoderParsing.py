from os import listdir
from os.path import isfile, join, isdir
import numpy as np
from PIL import Image
import Config

def get_clips_by_stride(stride, frames_list, sequence_size):
    """ For data augmenting purposes.
    Parameters
    ----------
    stride : int
        The distance between two consecutive frames
    frames_list : list
        A list of sorted frames of shape 256 X 256
    sequence_size: int
        The size of the lstm sequence
    Returns
    -------
    list
        A list of clips , 10 frames each
    """
    clips = []
    sz = len(frames_list)
    clip = np.zeros(shape=(sequence_size, 256, 256, 1))
    cnt = 0
    for start in range(0, stride):
        for i in range(start, sz, stride):
            clip[cnt, :, :, 0] = frames_list[i]
            cnt = cnt + 1
            if cnt == sequence_size:
                clips.append(clip)
                cnt = 0
    return clips

def get_training_set():
    """
    Returns
    -------
    list
        A list of training sequences of shape (NUMBER_OF_SEQUENCES,SINGLE_SEQUENCE_SIZE,FRAME_WIDTH,FRAME_HEIGHT,1)
    """
    clips = []
    # loop over the training folders (Train000,Train001,..)
    for f in sorted(listdir(Config.DATASET_PATH)):
        directory_path = join(Config.DATASET_PATH, f)
        if isdir(directory_path):
            all_frames = []
            # loop over all the images in the folder (0.tif,1.tif,..,199.tif)
            for c in sorted(listdir(directory_path)):
                img_path = join(directory_path, c)
                if str(img_path)[-3:] == "tif":
                    img = Image.open(img_path).resize((256, 256))
                    img = np.array(img, dtype=np.float32) / 256.0
                    all_frames.append(img)
            # get the 10-frames sequences from the list of images after applying data augmentation
            for stride in range(1, 3):
                clips.extend(get_clips_by_stride(stride=stride, frames_list=all_frames, sequence_size=Config.SEQ_LEN))
    return clips

#----------------------------- Parse Data From Max DB ----------------------------#
def get_max_training_set():
    """
    Returns
    -------
    list
        A list of training sequences of shape (NUMBER_OF_SEQUENCES,SINGLE_SEQUENCE_SIZE,FRAME_WIDTH,FRAME_HEIGHT,1)
    """
    #####################################
    # cache = shelve.open(Config.CACHE_PATH)
    # return cache["datasetLSTM"]
    #####################################
    clips = []
    # loop over the training folders (Train000,Train001,..)
    print('Found %d games' %len(listdir(Config.TRAINSET_PATH)))
    for game in sorted(listdir(Config.TRAINSET_PATH))[:3]:
        all_frames = np.load(join(Config.TRAINSET_PATH, game))
        print("loaded shape: ", all_frames.shape)
        print("reshaped shape: ", all_frames.reshape(-1, 256, 256).shape)
        all_frames = all_frames.reshape(-1, 256, 256)
        print("Loaded ", game)
        # get the SEQ_LEN sequences from the list of images after applying data augmentation
        for stride in range(1, 3):
#             print('all_frames.shape: ', np.array(all_frames).shape)
            clips.extend(get_clips_by_stride(stride=stride, frames_list=all_frames, sequence_size=Config.SEQ_LEN))
#             print('clips.shape: ', np.array(clips).shape)
#             input()
    return clips
# def get_single_test():
#     test = np.zeros(shape=(Config.FPP, 256, 256, 1))
#     cnt = 0
#     for f in sorted(listdir(Config.SINGLE_TEST_PATH)):
#         if str(join(Config.SINGLE_TEST_PATH, f))[-3:] == "tif":
#             img = Image.open(join(Config.SINGLE_TEST_PATH, f)).resize((256, 256))
#             img = np.array(img, dtype=np.float32) / 256.0
#             test[cnt, :, :, 0] = img
#             cnt = cnt + 1
#
#     sz = test.shape[0] - Config.SEQ_LEN
#     sequences = np.zeros((sz, Config.SEQ_LEN, 256, 256, 1))
#     # apply the sliding window technique to get the sequences
#     for i in range(0, sz):
#         clip = np.zeros((Config.SEQ_LEN, 256, 256, 1))
#         for j in range(0, Config.SEQ_LEN):
#             clip[j] = test[i + j, :, :, :]
#         sequences[i] = clip
#     return sequences

def get_single_test(test_clip):
    test = np.zeros(shape=(Config.FPP, 256, 256, 1))
    cnt = 0
    for f in sorted(listdir(join(Config.TESTSET_PATH, test_clip))):
        if cnt == Config.FPP:
            break
        if str(join(join(Config.TESTSET_PATH, test_clip), f))[-3:] == "tif":
            img = Image.open(join(join(Config.TESTSET_PATH, test_clip), f)).resize((256, 256))
            img = np.array(img, dtype=np.float32) / 256.0
            test[cnt, :, :, 0] = img
            cnt += 1

    sz = test.shape[0] - Config.SEQ_LEN
    sequences = np.zeros((sz, Config.SEQ_LEN, 256, 256, 1))
    # apply the sliding window technique to get the sequences
    for i in range(0, sz):
        clip = np.zeros((Config.SEQ_LEN, 256, 256, 1))
        for j in range(0, Config.SEQ_LEN):
            clip[j] = test[i + j, :, :, :]
        sequences[i] = clip
    return sequences
