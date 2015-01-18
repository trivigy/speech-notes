#!/usr/bin/python
import alsaaudio
import wave
import numpy
import threading
import sys
import subprocess

def timed_loop():
    threading.Timer(5.0, timed_loop).start()
    w.close()
    subprocess.call(["ffmpeg", "-i", filename_wav, "-y", "-vn", "-acodec", "libfaac", filename_mp4])
    i = (i + 1) % 10
    w = wave.open(filename, 'w')

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

i = 0
filename_wav = 'output' + i + '.wav'
filename_mp4 = 'output' + i + '.mp4'
w = wave.open(filename, 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

timed_loop()
while True:
    l, data = inp.read()
    w.writeframes(data)