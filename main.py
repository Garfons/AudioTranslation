import speech_recognition as sr # pip install SpeechRecognition , pip install pyAudio
from googletrans import Translator # pip install googletrans
from voiceOver import VoiceOver
from audioCreation import createAudio

translator = Translator()

# Record Audio

r = sr.Recognizer()

def createAudioTrack(path):
    createAudio(path)

    audioFile = sr.AudioFile("audio.wav")

    with audioFile as source:
        print("Getting audio text...")
    #   audio = r.listen(source)
        audio = r.record(source)
        return audio
    
#createAudioTrack("audio.wav")

print("Сonnecting windows voice...")
speaker = VoiceOver(lang='en')

def textReading(audio):
    try:
        print("Starting recognizing audio...")
        myWords = r.recognize_google(audio, language="ru-Ru").lower() # getting audio text in russian
        print("Translating text...")
        engWords = translator.translate(myWords, src='ru', dest='en').text # translation ru to en
        print("Voice-over...")
        speaker.speak(engWords)
    
        print(engWords)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

