import pyaudio
import numpy
import struct
import time

CHUNK = 128

start = time.time()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNK)
while(time.time() - start < 5):
    
    data = stream.read(CHUNK)
    print (numpy.fromstring(data, numpy.int16)) # use external numpy module
    print (struct.unpack('h'*CHUNK, data)) # use built-in struct module

stream.stop_stream()
stream.close()
p.terminate()