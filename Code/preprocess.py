import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

freq_sample, sig_audio = wavfile.read("G:/PPT/2 - 2/AI DS/Project/Code-Mixing Translation DataSet/Modified Dataset (1 "
                                      "to 25)/Modified_Voice_013.wav")
print('\nShape of Signal:', sig_audio.shape)
print('Signal Datatype:', sig_audio.dtype)
print('Signal duration:', round(sig_audio.shape[0] / float(freq_sample), 2), 'seconds')
sig_length = len(sig_audio)
half_length = np.ceil((sig_length + 1) / 2.0).astype(int)
signal_freq = np.fft.fft(sig_audio)
signal_freq = abs(signal_freq[0:half_length]) / sig_length
signal_freq **= 2
transform_len = len(signal_freq)
if sig_length % 2:
    signal_freq[1:transform_len] *= 2
else:
    signal_freq[1:transform_len - 1] *= 2
exp_signal = 10 * np.log10(signal_freq)
x_axis = np.arange(0, half_length, 1) * (freq_sample / sig_length) / 1000.0
plt.plot(x_axis, exp_signal, color='green', linewidth=1)
plt.show()
