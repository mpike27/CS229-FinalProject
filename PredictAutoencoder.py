import matplotlib.pyplot as plt
import Config
from keras.layers import LayerNormalization
from keras.models import load_model
import AutoencoderParsing as ap

def main():
    model = load_model(Config.MODEL_PATH,custom_objects={'LayerNormalization': LayerNormalization})
    print("got model")
    test = ap.get_single_test()
    print("got test")

    # get the reconstruction cost of all the sequences
    reconstructed_sequences = model.predict(sequences,batch_size=4)
    sequences_reconstruction_cost = np.array([np.linalg.norm(np.subtract(sequences[i],reconstructed_sequences[i])) for i in range(0,sz)])
    sa = (sequences_reconstruction_cost - np.min(sequences_reconstruction_cost)) / np.max(sequences_reconstruction_cost)
    sr = 1.0 - sa

    # plot the regularity scores
    plt.plot(sr)
    plt.ylabel('regularity score Sr(t)')
    plt.xlabel('frame t')
    plt.show()

if __name__ == '__main__':
    main()
