import numpy as np
from scipy.io import wavfile
fs = 16e3
t = np.arange(0,0.25,1/fs)
c = np.sin(2*np.pi*262*t)
d = np.sin(2*np.pi*294*t)
e = np.sin(2*np.pi*330*t)
f = np.sin(2*np.pi*349*t)
g = np.sin(2*np.pi*392*t)
a = np.sin(2*np.pi*440*t)
b = np.sin(2*np.pi*494*t)
c1 = np.sin(2*np.pi*523*t)
zeros = [np.zeros(len(t))]
gundul_pacul = []
gundul_pacul = np.append(c,e)
gundul_pacul = np.append(gundul_pacul, c)
gundul_pacul = np.append(gundul_pacul, e)
gundul_pacul = np.append(gundul_pacul, c)
gundul_pacul = np.append(gundul_pacul, e)
gundul_pacul = np.append(gundul_pacul, f)
gundul_pacul = np.append(gundul_pacul, g)   
gundul_pacul = np.append(gundul_pacul, g)
gundul_pacul = np.append(gundul_pacul, zeros)
gundul_pacul = np.append(gundul_pacul, b)
gundul_pacul = np.append(gundul_pacul, c1)
gundul_pacul = np.append(gundul_pacul, b)
gundul_pacul = np.append(gundul_pacul, c1)
gundul_pacul = np.append(gundul_pacul, b)
gundul_pacul = np.append(gundul_pacul, g)
gundul_pacul = np.append(gundul_pacul, zeros)
gundul_pacul = np.append(gundul_pacul, zeros)
wavfile.write('./file1.wav', int(fs), gundul_pacul.astype(np.float32))