import matplotlib.pyplot as plt
import Config
from keras.layers import LayerNormalization
from keras.models import load_model
import AutoencoderParsing as ap
import numpy as np
import os

def main():
    model = load_model(Config.MODEL_PATH,custom_objects={'LayerNormalization': LayerNormalization})
    print("got model")
    # test_sequences = ap.get_single_test()
    # print("got test - shape: ", test_sequences.shape)
    #
    # # get the reconstruction cost of all the sequences
    # reconstructed_sequences = model.predict(test_sequences,batch_size=4)
    # sequences_reconstruction_cost = np.array([np.linalg.norm(np.subtract(test_sequences[i],reconstructed_sequences[i])) for i in range(len(test_sequences))])
    # sa = (sequences_reconstruction_cost - np.min(sequences_reconstruction_cost)) / np.max(sequences_reconstruction_cost)
    # sr = 1.0 - sa
    #
    # # plot the regularity scores
    # plt.plot(sr)
    # plt.ylabel('regularity score Sr(t)')
    # plt.xlabel('frame t')
    # plt.show()

    #-------------------------- Predict.py --------------------------#
    test_clips = sorted(os.listdir(Config.TESTSET_PATH))
    # print(len(test_clips))
    #Test on NUM_TESTS randomly chosen clips from the testing set
    # test_clips = random.sample(test_clips, Config.NUM_TESTS)
    for test_clip in test_clips:
        print("Testing on " + test_clip)
        if test_clip[0] == '.':
            print("%s not a clip. Skipping..." %test_clip)
            continue
        test_sequences = ap.get_single_test(test_clip)
        print("got test - shape: ", test_sequences.shape)
        # get the reconstruction cost of all the sequences
        reconstructed_sequences = model.predict(test_sequences,batch_size=4)
        sequences_reconstruction_cost = np.array([np.linalg.norm(np.subtract(test_sequences[i],reconstructed_sequences[i])) for i in range(0,len(test_sequences))])
        sa = (sequences_reconstruction_cost - np.min(sequences_reconstruction_cost)) / np.max(sequences_reconstruction_cost)
        sr = 1.0 - sa

        # plot the regularity scores
        plt.figure()
        plt.plot(sr)
        plt.ylabel('regularity score Sr(t)')
        plt.xlabel('frame t')
        plt.savefig(test_clip +'.png')

if __name__ == '__main__':
    main()
