import subprocess
import os
import inspect
import sys

path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

def createAudioTrack(fileName):
    command = "ffmpeg -i " + path + "/" + fileName + " -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    subprocess.call(command, shell=True)

