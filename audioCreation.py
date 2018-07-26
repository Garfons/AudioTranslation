# ffpeg download on https://ffmpeg.zeranoe.com/builds/
import subprocess
import os
import inspect


path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
fileName = "video.mp3"

command = "ffmpeg -i " + path + "/" + fileName + " -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)

