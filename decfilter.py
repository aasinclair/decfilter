#!/usr/bin/python
import sys
import argparse
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.signaltools import lfilter

# Command line processing
parser = argparse.ArgumentParser(description='Knock coefficient utility')
parser.add_argument('sample', help='Sampling frequency',  type=float)
parser.add_argument('low',    help='Low pass frequency',  type=float)
parser.add_argument('high',   help='High pass frequency', type=float)
parser.add_argument('-graph', help='Display graph', action='store_true')
parser.add_argument('-scale', help='Coefficent scaling',  default=8)
Args = parser.parse_args()

# Get filter coefficients
nyq = 0.5 * Args.sample
bands = [Args.low / nyq, Args.high / nyq]
b, a = signal.butter(2, bands, btype='bandpass')
#b, a = signal.ellip(2, 3, 100, bands, btype='bandpass')

# Scale and invert coefficients
c = b / Args.scale
for i in range(1, 5):
    c = np.append(c, - a[i] / Args.scale)

if max(c) > 1 or max(c) < -1:
    sys.exit('Coefficients out of range' % (file, msg))

print 'Scaled coefficients'
for ci in c:
    print ci

print 'Hex coefficients'
for xi in c:
    coef = int(xi * 0x7FFFFF)
    if coef < 0:
        print('0x%06X' % (0x1000000 + coef))
    else:
        print('0x%06X' % (coef))


# Display frequency response graph if required
if not Args.graph:
    sys.exit()

plt.title('Frequency response')

w, h = signal.freqz(b, a)
w = w * Args.sample / (2 * np.pi)
h = np.clip(20 * np.log10(abs(h)), -60, 100)
plt.plot(w, h, 'b')

plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [Hz]')

plt.show()
