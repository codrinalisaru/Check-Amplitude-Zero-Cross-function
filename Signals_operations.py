#https://stackoverflow.com/questions/74096733/synchronizing-two-noisy-sinusoids-out-of-phase

import numpy as np
from scipy import fft
from matplotlib import pyplot as plt

sr = 200
time = np.arange(0, 60, 1/sr)

amp = 2
F = 0.25
omega = 2 * np.pi * F

signal1 = amp*np.sin(omega * time + np.pi)
signal2 = amp*np.sin(omega * time + np.pi/3)

mu, sigma = 0.2, 0.1 # mean and standard deviation
noise1 = np.random.normal(mu, sigma, len(signal1))
noise2 = np.random.normal(mu, sigma, len(signal2))


noisy_signal1 = signal1 + noise1
noisy_signal2 = signal2 + noise2

# Get frequency in samples
fft1 = fft.fft(noisy_signal1)
fft2 = fft.fft(noisy_signal2)
max_f = np.argmax(np.abs(fft1))
f = len(noisy_signal1) / max_f

# Perform correlation to determine best fit for phase difference (in samples)
corr = np.correlate(noisy_signal1, noisy_signal2, 'full')
delta_p = int(round(np.argmax(corr) % f))

# Chop phase difference (maximum 1/2 cycle)
fi = int(round(f,0))
if delta_p < fi/ 2:
    noisy_signal1 = noisy_signal1[delta_p:]
    noisy_signal2 = noisy_signal2[:-delta_p]
    time = time[delta_p:]
else:
    noisy_signal1 = noisy_signal1[:delta_p - fi]
    noisy_signal2 = noisy_signal2[fi - delta_p:]
    time = time[:delta_p - fi]

plt.figure()
plt.plot(time, noisy_signal1)
plt.plot(time, noisy_signal2)
plt.show() 

