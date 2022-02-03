import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np

sample_rate, samples = wavfile.read('./untitled.wav')

frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

print(len(frequencies))

    
#plt.pcolormesh(times, frequencies, spectrogram)
#plt.imshow(spectrogram)
#plt.ylabel('Frequency [Hz]') 129
#plt.xlabel('Time [sec]') 1305
#plt.show()