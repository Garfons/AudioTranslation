# coding: utf-8
# ffpeg download on https://ffmpeg.zeranoe.com/builds/
import subprocess


def createAudio(fileName):
    command = "ffmpeg -i " + fileName + " -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    subprocess.call(command, shell=True)

