import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.pyplot as plt
b, a = signal.butter(4, 100, 'low', analog=True)
w,h = signal.freqs(b, a)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [rad/second]')
plt.ylabel('magnitude/gain [dB]')
plt.margins(0,0.1)
#plt.grid(which='both axis='both')
plt.axvline(100, color='g') # cutoff frequency
plt.show()
