#!/usr/bin/python
import alsaaudio
import time
import wave
import numpy
import threading
import sys
import subprocess

def timed_loop():
    global event, w
    event.clear()
    threading.Timer(2.0, timed_loop).start()
    subprocess.call(["ffmpeg", "-loglevel", "panic", "-i", filename_wav, "-y", "-vn", "-acodec", "libfaac", filename_mp4])
    w.close()
    subprocess.call(['curl -X POST --form "file=@output.mp4" --form "apikey=e5ca0d01-0fb2-4dc1-9ed7-20ee8873721f" https://api.idolondemand.com/1/api/sync/recognizespeech/v1'], shell = True)
    print
    # data = urllib.urlencode({'file': '@output.mp4', 'apikey':'e5ca0d01-0fb2-4dc1-9ed7-20ee8873721f'})
    # r = urllib2.urlopen('https://api.idolondemand.com/1/api/sync/recognizespeech/v1', data)
    # print r.read()
    # sys.stdout.flush()
    w = wave.open(filename_wav, "w")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    event.set()

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)
event = threading.Event()
event.set()

filename_wav = 'output.wav'
filename_mp4 = 'output.mp4'
w = wave.open(filename_wav, 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

threading.Timer(2.0, timed_loop).start()
while True:
    event.wait()
    l, data = inp.read()
    w.writeframes(data)