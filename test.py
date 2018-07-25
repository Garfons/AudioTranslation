import speech_recognition as sr # pip install speech_recognition , pip install pyAudio
import win32com.client # pip install win32
from googletrans import Translator # pip install googletrans
translator = Translator()
# Record Audio

r = sr.Recognizer()
audioFile = sr.AudioFile("audio.wav")

with audioFile as source:
    print("Getting audio text...")
    audio = r.record(source)

print("connecting voice...")
speaker = win32com.client.Dispatch("SAPI.SpVoice")

try:
    myWords = r.recognize_google(audio, language="ru-RU").lower() # getting audio text in russian
    engWords = translator.translate(myWords, src='ru', dest='en').text # translation ru to en
    speaker.Speak(engWords)

    print(engWords)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

