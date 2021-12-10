import pyaudio
import struct

import numpy as np
import matplotlib.pyplot as plt

CHUNK= 1024*4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE =44100


p= pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()

x = np.arange(0,2 *CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK),'r')
ax.set_ylim(0,255)
ax.set_xlim(0,CHUNK)
fig.show()
while True:
    data =stream.read(CHUNK)
    data_int= np.array(struct.unpack(str(2* CHUNK)+'H',data), dtype='h')[::2] +127
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()


print(pa.get_device_count())
