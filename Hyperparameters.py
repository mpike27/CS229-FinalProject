#------------------------- Training Hyperparameters -------------------------#
# These hyperparameters are tuned to maximize the validation loss, ie the mse of
# the reconstruction
CLIP_LEN = 10#clips
FPS = 1#frames per second
FRAME_RES = 32# (128, 128)
lr = {"Base_Auto": 0.0001, "3DConv_Auto": 0.0001, "LSTM_Auto": 1e-6}
decay = {"Base_Auto": 0.0001, "3DConv_Auto": 0.00001, "LSTM_Auto": 1e-7}
eps = {"Base_Auto": 1e-05, "3DConv_Auto": 0.00001, "LSTM_Auto": 1e-8}
num_filters = 64
kernel_size = 3

#------------------------- Evaluation Hyperparameters -------------------------#
# These hyperparameters are tuned to maximize the evaluation score, ie how accurately
# the model can classify clips as highlights or not
HIGHLIGHT_RATIO = 0.1# 10% of full match are highlights
