
import scipy.io.wavfile as wav
import numpy as np
import sys

sample_rate, data = wav.read("flag.wav")
for i in data:
    print(i)
flag=''
#n位振幅值，近似值取整
def repla(n):
    if n == -3:
        return '00'
    elif n == -1:
        return '01'
    elif n == 1:
        return '10'
    elif n == 3:
        return '11'

for x, y in data:
    n1 = round(float(x))
    n2 = round(float(y))
    flag += repla(n1)
    flag += repla(n2)
print(flag)
