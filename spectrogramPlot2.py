import pyYIN

print(pyYIN.yin_algorithm("./untitled.wav", threshold=0.1, target_Fs=16e3, freq_range=(40, 300), timestep=0.1, Fc=1e3))
