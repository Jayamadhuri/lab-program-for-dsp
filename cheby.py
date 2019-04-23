import numpy as np
import matplotlib.pyplot as plot
from scipy import signal
import matplotlib.pyplot as plt
b,a=signal.cheby1(4, 5, 100, 'low', analog=True)
w,h=signal.freqs(b, a)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Chebyshev filter frequency response')
plt.xlabel('Frequency [rad/sec]')
plt.ylabel('magnitude/gain [dB]')
plt.margins(0, 0.1)
#plt.grid(which='both', axis='both')
plt.axvline(100, color='b') # cutoff frequency
#plt.axhline(-5, color='g') # rp
plt.show()
